from __future__ import annotations

import includeigen


def test_version():
    assert includeigen.__version__


def test_get_eigen_version():
    assert isinstance(
        includeigen.get_eigen_version(), str
    ), f"The version is not a string: {includeigen.get_eigen_version()}"


def test_get_include():
    assert isinstance(
        includeigen.get_include(), str
    ), f"The include path is not a string: {includeigen.get_include()}"
