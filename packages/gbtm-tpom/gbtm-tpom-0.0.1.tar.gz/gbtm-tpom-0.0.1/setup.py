import pathlib
from setuptools import setup, find_packages

# The directory containing this file
dir = pathlib.Path(__file__).parent

# README file
README = (dir / "README.md").read_text()

# Dependencies
with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='gbtm-tpom',
    version="0.0.01",
    packages=["gbtmtpom"],
    author="Walid Ghariani",
    author_email="walid11ghariani@gmail.com",
    description=("wood class"),
    long_description=README,
    license="MIT",
    keywords="spatial",
    url="https://github.com/WalidGharianiEAGLE/spatial-kfold",

    #packages=find_packages(),
    package_data={'gbtmtpom': ['data/*.geojson']},
    include_package_data=True,

    # Dependencies
    install_requires = requirements,
    python_requires='>=3.7',

    # testing
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)