
from setuptools import setup, find_packages

setup(
    name="exercises_py",
    description="Different exercises in Python",
    url="https://github.com/marriyay/exercises_py",
    maintainer="Mariia Antonova",
    setup_requires=["flake8"],
    tests_require=["pytest"],
    classifiers=[
        # https://pypi.org/classifiers/
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=find_packages(exclude=["*.tests"])
)
