#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy
from findblas.distutils import build_ext_with_blas


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()



ext_modules = [
    Extension(
        "bonnndit.utilc.blas_lapack",
        ["src/bonnndit/utilc/blas_lapack.pyx"],
        include_dirs=[numpy.get_include()],
        extra_compile_args=["-Wall", "-m64", "-Ofast"],
        extra_link_args=["-Wl,--no-as-needed"]
    ),
    Extension(
        "bonnndit.utilc.cython_helpers",
        ["src/bonnndit/utilc/cython_helpers.pyx"],
        include_dirs=[numpy.get_include()],
        extra_compile_args=["-Wall", "-m64", "-Ofast"],
        extra_link_args=["-Wl,--no-as-needed"]
    ),
    Extension(
        "bonnndit.utilc.hota",
        ["src/bonnndit/utilc/hota.pyx"],
        extra_compile_args=["-Ofast"],
    ),
    Extension(
        "bonnndit.utilc.trilinear",
        ["src/bonnndit/utilc/trilinear.pyx"],
        extra_compile_args=["-Ofast"],
    ),
    Extension(
        "bonnndit.utilc.structures",
        ["src/bonnndit/utilc/structures.pyx"],
        extra_compile_args=["-Ofast"],
    ),
    Extension(
        "bonnndit.utilc.penalty_spherical",
        ["src/bonnndit/utilc/penalty_spherical.pyx"],
        extra_compile_args=["-Ofast"],
    ),
    Extension(
        "bonnndit.utilc.lowrank",
        ["src/bonnndit/utilc/lowrank.pyx"],
        extra_compile_args=["-Ofast"],
    ),
    Extension(
        "bonnndit.directions.fodfapprox",
        ["src/bonnndit/directions/fodfapprox.pyx"],
        include_dirs=[numpy.get_include(), '.'],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        extra_compile_args=['-fopenmp', '-Ofast'],
        extra_link_args=['-fopenmp'],
    ),
    Extension(
        "bonnndit.tracking.ItoW",
        ["src/bonnndit/tracking/ItoW.pyx"],
        extra_compile_args=["-Ofast"],
    ),
    Extension(
        "bonnndit.tracking.alignedDirection",
        ["src/bonnndit/tracking/alignedDirection.pyx"],
        include_dirs=[numpy.get_include()],
        extra_compile_args=["-Wall", "-m64", "-Ofast"],
        extra_link_args=["-Wl,--no-as-needed"]
    ), Extension(
        "bonnndit.tracking.kalman.model",
        ["src/bonnndit/tracking/kalman/model.pyx"],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        libraries=["pthread", "m", "dl"],
        extra_compile_args=["-Wall", "-m64", "-Ofast"],
        extra_link_args=["-Wl,--no-as-needed"]

    ),
    Extension(
        "bonnndit.tracking.kalman.kalman",
        ["src/bonnndit/tracking/kalman/kalman.pyx"],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        include_dirs=[numpy.get_include()],
        libraries=["pthread", "m", "dl"],
        extra_compile_args=["-Wall", "-m64", '-Ofast'],
        extra_link_args=["-Wl,--no-as-needed"]

    ),
    Extension(
        "bonnndit.tracking.interpolation",
        ["src/bonnndit/tracking/interpolation.pyx"],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        include_dirs=[numpy.get_include()],
        libraries=[ "pthread", "m", "dl"],
        extra_compile_args=["-Wall", "-m64", "-Ofast"],
        extra_link_args=["-Wl,--no-as-needed"]
    ),
    Extension(
        "bonnndit.tracking.integration",
        ["src/bonnndit/tracking/integration.pyx"],
        include_dirs=[numpy.get_include()],
        libraries=["pthread", "m", "dl"],
        extra_compile_args=["-Wall", "-m64", "-Ofast"],
        extra_link_args=["-Wl,--no-as-needed"]
    ),
    Extension(
        "bonnndit.tracking.stopping",
        ["src/bonnndit/tracking/stopping.pyx"],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        include_dirs=[numpy.get_include()],
        libraries=[ "pthread", "m", "dl"],
        extra_compile_args=["-Wall", "-m64", "-Ofast"],
        extra_link_args=["-Wl,--no-as-needed"]
    ),
    Extension(
        "bonnndit.tracking.tracking_prob",
        ["src/bonnndit/tracking/tracking_prob.pyx"],
        extra_compile_args=['-fopenmp', "-Ofast"],
        extra_link_args=['-fopenmp'],
    ),
    Extension(
        "bonnndit.pmodels.means",
        ["src/bonnndit/pmodels/means.pyx"],
        extra_compile_args=["-Ofast"],
    ),
    Extension(
        "bonnndit.pmodels.model_avg",
        ["src/bonnndit/pmodels/model_avg.pyx"],
        extra_compile_args=["-Ofast"],
    ),
    Extension(
        "bonnndit.filter.filter",
        ["src/bonnndit/filter/filter.pyx"],
        extra_compile_args=["-Ofast"],
    ),
    Extension(
        "bonnndit.filter.filter",
        ["src/bonnndit/filter/filter.pyx"],
        extra_compile_args=["-Ofast"],
    ),
    Extension(
        "bonnndit.directions.csd_peaks",
        ["src/bonnndit/directions/csd_peaks.pyx"],
        include_dirs=[numpy.get_include()],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        extra_compile_args=["-Ofast"],
    ),
]

requirements = ['nibabel', 'numpy', 'pandas',  'scipy', 'tqdm',
                'cvxopt', 'mpmath', 'plyfile', 'Cython', 'pynrrd']

setup_requirements = ['pytest-runner', 'cython']

test_requirements = ['pytest', 'nibabel', 'numpy', 'dipy', 'scipy', 'tqdm',
                     'cvxopt', 'mpmath', 'pynrrd']
print(find_packages('src'))
setup(
    author="Johannes Gruen",
    author_email='jgruen@uni-bonn.de',
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="The bonnndit package contains the latest diffusion imaging tools developed at the University of Bonn.",
  #  install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bonnndit',
    name='bonnndit',

    packages=find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    scripts=['scripts/mtdeconv',
             'scripts/stdeconv',
             'scripts/kurtosis',
             'scripts/dtiselectvols',
             'scripts/low-rank-k-approx',
             'scripts/peak-modelling',
             'scripts/prob-tracking',
             'scripts/bundle-filtering',
             'scripts/csd-peaks',
             'scripts/data2fodf'],
    ext_modules=cythonize(ext_modules, compiler_directives={'boundscheck': False, 'wraparound': False,
                                                            'optimize.unpack_method_calls': False}),
    cmdclass = {'build_ext': build_ext_with_blas},
    package_data={"": ['*.pxd', '*.npz']},
    url='https://github.com/MedVisBonn/bonnndit',
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    version='0.2.5',
    zip_safe=False,
)
