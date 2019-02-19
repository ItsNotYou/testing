import setuptools

long_description = open("README.md").read()

setuptools.setup(
    name="maxima-tlange",
    version="0.0.2",
    author="Theresa Lange",
    author_email="tlange@math.tu-berlin.de",
    description="Find local maxima",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ItsNotYou/testing",
    packages=['maxima'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    tests_require=['numpy', 'pytest'],
)
