from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="egancschallengeset3",
    version="0.0.1",
    author="caden",
    description="egancschallengeset3",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=['a'],
    url="",
    install_requires=[],
    python_requires=">=3.7",
    py_modules=["egancschallengeset3"]
)