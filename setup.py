#!/usr/bin/env python
import sys
from pathlib import Path
from setuptools import setup, find_packages

# ensure the current directory is on sys.path
# so versioneer can be imported when pip uses
# PEP 517/518 build rules.
# https://github.com/python-versioneer/python-versioneer/issues/193
sys.path.append(Path(__file__).resolve(strict=True).parent.as_posix())
import versioneer  # noqa: E402

if __name__ == "__main__":
    setup(
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        packages=find_packages(include="alphalens.*"),
        package_data={"alphalens": ["examples/*"]},
    )
