from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="VSsetup",
    long_description=long_description,
    long_description_content_type='text/markdown',
    description = ("Use this tools to change the color of the outputs in the terminal"),
    version="1.1",
    license="MIT",
    author="Ruben Hinojar",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "colorama"
    ],
)
