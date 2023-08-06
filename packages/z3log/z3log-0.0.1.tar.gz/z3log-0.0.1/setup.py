from setuptools import setup, find_packages
import os


VERSION = '0.0.1'
DESCRIPTION = 'A Verilog to Z3PY/GV Convertor'
INSTALL_REQUIREMENTS_FILE = 'install_requiremnets.txt'
INSTALL_REQUIREMENTS = []
with open(INSTALL_REQUIREMENTS_FILE, 'r') as IR:
    lines = IR.readlines()
    for line in lines:
        INSTALL_REQUIREMENTS.append(line.replace('\n', ""))


# Setting up
setup(
    name="z3log",
    version=VERSION,
    author="Morteza Rezaalipour (MorellRAP)",
    author_email="<rezaalipour.usi@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=INSTALL_REQUIREMENTS,
    keywords=['python', 'verilog', 'circuits', 'synthesis', 'graphviz', 'z3', 'smt-solver', 'sat-solver', 'gv'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
) 
