import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redmage",
    version="0.0.0",
    author="Scott Russell",
    author_email="me@scottrussell.net",
    description="Redmage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scrussell24/redmage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)