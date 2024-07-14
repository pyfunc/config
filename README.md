# [config.pyfunc.com](http://config.pyfunc.com)

## START

Install required tools
```bash
pip install setuptools wheel build twine pip-tools setuptools-git-versioning
pip install --upgrade setuptools_scm
```
rm -rf build dist *.egg-info

## UPDATE

```bash
git tag 1.1.0
git push origin --tags
```

start
```bash
pip-compile pyproject.toml
pip-sync
```

Use the following commands to build and publish your package:

1. **Build the Package**:
```bash
rm -rf build dist *.egg-info
python -m build --sdist --wheel -n
python -m build
```

2. **Publish to PyPI**:
```bash
python -m pip install --upgrade twine
twine upload dist/*
```



```bash
pip-compile pyproject.toml
pip-sync
```


```bash
bumpver update --patch
```


Here's an updated GitHub Actions workflow to include the script execution:

```bash
py generate_init.py -p src/pyfunc-config
````

```bash
py -m build
```

```bash
twine check dist/*
```


```bash
twine upload -r testpypi dist/*
```

```bash
twine upload dist/*
```        


## Semantic versioning

The idea of semantic versioning (or SemVer) is to use 3-part version numbers, major.minor.patch, where the project author increments:

    major when they make incompatible API changes,

    minor when they add functionality in a backwards-compatible manner, and

    patch, when they make backwards-compatible bug fixes.
