from setuptools import setup
from Cython.Build import cythonize

setup(name="gman app", ext_modules=cythonize("gman.pyx"))
