# [config.pyfunc.com](http://config.pyfunc.com)

## START
```bash
python -m pip install pip-tools
pip-compile pyproject.toml
pip-sync
```

## UPDATE

```bash
git tag 0.1.1
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
