from setuptools import setup, find_packages
from src.thermoreceptormodel import __version__

with open("README.md", "r") as fh:
    readme_description = fh.read()

setup(
    name="thermoreceptormodel",
    version=__version__,
    license="MIT",
    description=(
        "Package to calculate thermoreceptor activity in the human skin."
    ),
    long_description=readme_description,
    long_description_content_type="text/markdown",
    author="Akihisa Nomoto",
    author_email="monyo323232@gmail.com",
    url="https://github.com/AkihisaNomoto/thermoreceptormodel",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        # "Operating System :: Unix",
        # "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
    keywords=[
        "thermal comfort",
        "physiology"
        "building design",
        "thermal environment",
        "built environment",
    ],
    python_requires=">=3.8.0",
    install_requires=[
        "numpy",
        "pandas"
    ],  # eg: 'aspectlib==1.1.1', 'six>=1.7',
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
)