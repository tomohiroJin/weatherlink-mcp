from setuptools import setup, find_packages

setup(
    name="devcontainer-python",
    version="0.1.0",
    description="A sample Python project",
    author="tomohiro.jin",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    tests_require=["pytest"],
)
