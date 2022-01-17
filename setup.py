from setuptools import setup
from Cython.Build import cythonize


res = cythonize('src/imppkg/harmonic_mean.pyx')

setup(ext_modules=res)

