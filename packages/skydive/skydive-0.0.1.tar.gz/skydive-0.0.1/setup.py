from setuptools import setup

with open("README.md") as f:
    readme = f.read()

setup(
    name="skydive",
    version="0.0.1",
    license="MIT",
    author="ly4k",
    url="https://github.com/ly4k/Skydive",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=[
    ],
    packages=[
        "skydive"
    ],
    entry_points={
        "console_scripts": ["skydive=skydive.entry:main"],
    },
    description="Tool for attacking Hybrid Active Directory",
)