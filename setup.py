from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize(
        ["py_sum_of_squares.py", "dot_product.pyx"], annotate=True
    ),
    include_dirs=[np.get_include()],
)
