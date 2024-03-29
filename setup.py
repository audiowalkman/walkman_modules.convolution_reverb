import setuptools  # type: ignore

MAJOR, MINOR, PATCH = 0, 3, 0
VERSION = f"{MAJOR}.{MINOR}.{PATCH}"
"""This project uses semantic versioning.
See https://semver.org/
Before MAJOR = 1, there is no promise for
backwards compatibility between minor versions.
"""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

extras_require = {"testing": ["nose"]}

setuptools.setup(
    name="walkman_modules.convolution_reverb",
    version=VERSION,
    license="GPL",
    description="Provides walkman module to send input through a convolution reverb",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Levin Eric Zimmermann",
    author_email="levin.eric.zimmermann@posteo.eu",
    packages=[
        package
        for package in setuptools.find_namespace_packages(include=["walkman_modules.*"])
        if package[:5] != "tests"
    ],
    setup_requires=[],
    install_requires=[
        # core package
        "audiowalkman>=0.11.0, <1.0.0",
        # for audio
        "pyo==1.0.4",
    ],
    extras_require=extras_require,
    python_requires="==3.8",
)
