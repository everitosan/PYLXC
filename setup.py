import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="lxcpy",
    version="0.0.5",
    description="Automate lxc containers",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.sat.gob.mx/sat-dev/lxcpy.git",
    author="everitosan",
    author_email="eve.san.dev@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["lxcpy"],
    include_package_data=True,
    install_requires=["colorama"],
    entry_points={
        "console_scripts": [
            "lxcpy=lxcpy.__main__:main",
        ]
    },
)
