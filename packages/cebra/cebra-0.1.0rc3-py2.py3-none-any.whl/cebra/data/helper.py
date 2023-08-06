from typing import Union

import numpy as np
import numpy.typing as npt
import scipy.linalg
import torch


class OrthogonalProcrustesAlignment:
    """Aligns two embedding spaces with an orthogonal map.

    Note:
        The class can be used to align an embedding with a reference embedding.
        For that, the distance between the labels and reference labels is computed
        and only :py:attr:`top_k` samples where the distance is the smallest are kept
        from the reference data. Both the data to align and the reference data are then
        augmented to find the orthogonal matrix that best maps the augmented data to
        the augmented reference data. That reference matrix is then used for alignement.

    Args:
        top_k: Number of labels to consider for alignenement. The selected labels consist
            in the :py:attr:`top_k`th labels the closer from their corresponding reference label.
        subsample: Number of samples in the augmented data and reference data used in the
            orthogonal Procrustes problem.

    """

    def __init__(self, top_k: int = 5, subsample: int = 500):
        self.subsample = subsample
        self.top_k = top_k

    def _distance(self, label_i: npt.NDArray,
                  label_j: npt.NDArray) -> npt.NDArray:
        norm_i = (label_i**2).sum(1)
        norm_j = (label_j**2).sum(1)
        diff = np.einsum("nd,md->nm", label_i, label_j)
        diff = norm_i[:, None] + norm_j[None, :] - 2 * diff
        return diff

    def fit(
        self,
        ref_data: npt.NDArray,
        data: npt.NDArray,
        ref_label: npt.NDArray,
        label: npt.NDArray,
    ) -> npt.NDArray:
        """Compute the matrix solution to align a dataset to a reference dataset using the orthogonal Procrustes problem.

        Args:
            ref_data: reference data matrix on which to align the data.
            data: data matrix to align on the reference dataset.
            ref_label: set of indices associated to :py:attr:`ref_data`.
            label: set of indices associated to :py:attr:`data`.
        """

        distance = self._distance(label, ref_label)
        # Keep indexes of the {self.top_k} labels the closest to the reference labels
        target_idx = np.argsort(distance, axis=1)[:, :self.top_k]

        # Get the whole data to align and only the selected closest samples
        # from the reference data.
        X = data[:, None].repeat(5, axis=1).reshape(-1, 3)
        Y = ref_data[target_idx].reshape(-1, 3)

        # Augment data and reference data so that same size
        if self.subsample is not None:
            idc = np.random.choice(len(X), self.subsample)
            X = X[idc]
            Y = Y[idc]

        # Compute orthogonal matrix that most closely maps X to Y using the orthogonal Procrustes problem.
        self._transform, _ = scipy.linalg.orthogonal_procrustes(X, Y)

        return self

    def transform(self, data: Union[npt.NDArray, torch.Tensor]):
        """Transform the data using the matrix solution computed in py:meth:`fit`.

        Args:
            data: The 2D data matrix to align.

        Returns:
            The aligned input matrix.
        """
        if self.transform is None:
            raise ValueError("Call fit() first.")
        return data @ self._transform

    def fit_transform(
        self,
        ref_data: npt.NDArray,
        data: npt.NDArray,
        ref_label: npt.NDArray,
        label: npt.NDArray,
    ) -> npt.NDArray:
        """Compute the matrix solution to align a data array to a reference matrix.

        Note:
            Uses a combination of :py:meth:`fit` and py:meth:`transform`.

        Args:
            ref_data: reference data matrix on which to align the data.
            data: data matrix to align on the reference dataset.
            ref_label: set of indices associated to :py:attr:`ref_data`.
            label: set of indices associated to :py:attr:`data`.

        Returns:
            The data matrix aligned onto the reference data matrix.
        """
        self.fit(ref_data, data, ref_label, label)
        return self.transform(data)
