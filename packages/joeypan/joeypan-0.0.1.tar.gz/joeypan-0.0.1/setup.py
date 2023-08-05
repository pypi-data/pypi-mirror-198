import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="joeypan",
    version="0.0.1",
    author="elijahxb",
    author_email="elijahxb@outlook.com",
    description="A small package for web framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elijahxb/joey",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
