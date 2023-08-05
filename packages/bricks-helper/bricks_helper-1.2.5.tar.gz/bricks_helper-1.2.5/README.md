# Introduction

A python package for enhancing the experience of interacting with databricks

## Build process

```
py -m build
```

```
py -m twine upload --repository pypi dist/* --verbose
```

### To set your API token for PyPI, you can create a $HOME/.pypirc similar to:

```
[pypi]
username = __token__
password = <PyPI token>`
```
