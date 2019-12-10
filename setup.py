import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sorted",
    version="0.0.2",
    author="Anatoly Scherbakov",
    author_email="altaisoft@gmail.com",
    description=(
        "Merge, subtract, deduplicate and otherwise manipulate Python iterators"
        " that are known to be sorted."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/anatoly-scherbakov/sorted',
    packages=setuptools.find_packages(),
    install_requires=[

    ],
    extras_require={
        'dev': [
            'pytest',
            'coverage'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
