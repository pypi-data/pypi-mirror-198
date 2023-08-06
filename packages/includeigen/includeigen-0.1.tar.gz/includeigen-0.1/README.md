# includeigen

[![Actions Status][actions-badge]][actions-link][![PyPI version][pypi-version]][pypi-link][![Conda-Forge][conda-badge]][conda-link][![PyPI platforms][pypi-platforms]][pypi-link][![GitHub Discussion][github-discussions-badge]][github-discussions-link]

`includeigen` can be used by Python packages that require the C++ library
`Eigen`. It includes a version of `Eigen`, and a `get_include` function that
returns the path to the directory of the source code.

Currently, the version of Eigen is 3.4.0.

### Install

The `includeigen` is available on Pypi and conda-forge. Simply execute

```bash
python -m pip install includeigen
```

or

```bash
conda install includeigen -c conda-forge
```

### Developer's Corner

- To change Eigen's version, checkout the submodule to the corresponding tag
  (e.g. `3.4`) and commit the change.

- To release a new version, make a new github release. The chosen tag will be
  the version number.

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/changepoints/includeigen/workflows/CI/badge.svg
[actions-link]:             https://github.com/changepoints/includeigen/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/includeigen
[conda-link]:               https://github.com/conda-forge/includeigen-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/changepoints/includeigen/discussions
[pypi-link]:                https://pypi.org/project/includeigen/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/includeigen
[pypi-version]:             https://img.shields.io/pypi/v/includeigen

<!-- prettier-ignore-end -->
