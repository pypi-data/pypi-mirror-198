from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name = "binboy",
    version = "0.1.0",
    description = "A beautiful binary code printer",
    author_email="aitzazimtiaz855@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AitzazImtiaz/Bin-Boy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author = "AitzazImtiaz",
    packages = ["binboy"],
    entry_points = {
        'console_scripts': [
            'binboy = binboy.__main__:main'
        ]
    },
)
