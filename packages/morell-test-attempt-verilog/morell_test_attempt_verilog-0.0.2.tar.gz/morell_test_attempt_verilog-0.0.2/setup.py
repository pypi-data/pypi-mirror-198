from setuptools import setup, find_packages
import os


VERSION = '0.0.2'
DESCRIPTION = 'A Verilog Class'

# Setting up
setup(
    name="morell_test_attempt_verilog",
    version=VERSION,
    author="Morteza Rezaalipour (MorellRAP)",
    author_email="<rezaalipour.usi@gmail.com>",
    description=DESCRIPTION,
    packages=['libname', 'libname.config'],
    install_requires=['numpy', 'scipy', 'pandas', 'matplotlib', 'networkx', 'python-dateutil', 'PyYAML'],
    keywords=['python', 'verilog', 'circuits', 'synthesis'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
) 
