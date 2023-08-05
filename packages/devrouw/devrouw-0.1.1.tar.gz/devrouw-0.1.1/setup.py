from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="devrouw",
    version="0.1.1",
    author="Aitzaz Imtiaz",
    author_email="aitzazimtiaz855@gmail.com",
    description="A Python library for data analysis and visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://devrouw.readthedocs.io/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "matplotlib",
        "scipy",
    ],
)
