from setuptools import find_packages, setup

setup(
    name="announce-server",
    packages=find_packages(),
    setup_requires=[
        "setuptools_scm",
    ],
    use_scm_version=True,
    python_requires=">=3.6",
)
