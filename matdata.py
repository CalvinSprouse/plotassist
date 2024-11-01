# matdata.py

# A class to help with loading and accessing data from MATLAB mat files.
# TODO: Add docstrings
# TODO: Refine comments

# imports
from os import PathLike
from pathlib import Path
from typing import Sequence

import numpy.typing as npt
import scipy.io as sio


class MatData:

    def __init__(self, mat_file: PathLike, variable_names: Sequence = None):
        # convert to Path and check that file exists
        self.mat_file = Path(mat_file)
        if not mat_file.exists():
            raise FileNotFoundError(f"File {mat_file} not found")

        # load the data file with scipy
        self.data = sio.loadmat(
            mat_file,
            squeeze_me=True,
            simplify_cells=True,
            variable_names=variable_names,
        )


    def get_file(self) -> Path:
        return self.mat_file


    def get(self, var: str) -> npt.ArrayLike:
        # check that var is in self.data
        if var not in self.data:
            raise KeyError(f"Variable '{var}' not found in data")

        return self.data[var]


    def get_keys(self) -> Sequence[str]:
        return self.data.keys()


    def __repr__(self):
        # return the file location and keys
        file_location = self.mat_file.resolve()
        keys = list(self.data.keys())
        repr_str = f"MatData:\n\tmat_file={file_location}\n\tkeys={keys}"
        return repr_str
