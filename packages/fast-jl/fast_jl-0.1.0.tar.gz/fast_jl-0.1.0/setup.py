#!/usr/bin/env python

from os import environ

environ['TORCH_CUDA_ARCH_LIST']="7.0+PTX"

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='fast_jl',
    version="0.1.0",
    description="Fast JL: Compute JL projection fast on a GPU",
    author="MadryLab",
    author_email='krisgrg@mit.edu',
    ext_modules=[
        CUDAExtension('fast_jl', [
            'fast_jl.cu',
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    },
    setup_requires=["torch>=1.13"])
