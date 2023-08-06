from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        long_desc = f.read()
        # strip out the raw html images?
        return long_desc


short_desc = (
    "Write backend agnostic numeric code "
    "compatible with any numpy-ish array library."
)

setup(
    name="autoray",
    description=short_desc,
    long_description=readme(),
    url="http://github.com/jcmgray/autoray",
    author="Johnnie Gray",
    author_email="johnniemcgray@gmail.com",
    license="Apache",
    packages=find_packages(exclude=["deps", "tests*"]),
    extras_require={
        "tests": [
            "numpy",
            "coverage",
            "pytest",
            "pytest-cov",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="array agnostic numeric numpy cupy dask tensorflow jax autograd",
    long_description_content_type="text/markdown",
)
