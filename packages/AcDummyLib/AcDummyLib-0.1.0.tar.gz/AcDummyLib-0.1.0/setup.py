from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Assetto Corsa dummy library.'
LONG_DESCRIPTION = 'Assetto Corsa dummy library for "ac" object.'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="AcDummyLib",
    version=VERSION,
    author="Kirby Rs",
    author_email="<andkirby@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'AC', 'Assetto Corsa'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Games/Entertainment :: Simulation",
    ]
)