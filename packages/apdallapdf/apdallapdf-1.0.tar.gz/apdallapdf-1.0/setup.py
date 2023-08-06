import setuptools
from pathlib import Path
setuptools.setup(
    name="apdallapdf",
    version=1.0,
    long_descreption=Path("README.MD").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])


)
