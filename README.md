# Bisection Method

[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/sandialabs/sibl#license)

[![codecov](https://codecov.io/gh/Lejeune-Lab-Graduate-Course-Materials/bisection-method/graph/badge.svg?token=p5DMvJ6byO)](https://codecov.io/gh/Lejeune-Lab-Graduate-Course-Materials/bisection-method)
[![tests](https://github.com/Lejeune-Lab-Graduate-Course-Materials/bisection-method/actions/workflows/tests.yml/badge.svg)](https://github.com/Lejeune-Lab-Graduate-Course-Materials/bisection-method/actions)
---

To install the package, set up a conda environment:

conda create --name newtons-method-env python=3.12

Once it is created, activate it:

conda activate newtons-method-env

Double check that Python is version 3.12 in the environment:

python --version

Ensure that pip is using the most updated version of setuptools:

pip install --upgrade pip setuptools wheel

Create an editable install of the newtons method code:

pip install -e .

Test that the code is working with pytest:

pytest -v --cov=newtonsmethod --cov-report term-missing

To run the examples:

pip install jupyter

cd tutorials/

jupyter notebook tutorial.ipynb