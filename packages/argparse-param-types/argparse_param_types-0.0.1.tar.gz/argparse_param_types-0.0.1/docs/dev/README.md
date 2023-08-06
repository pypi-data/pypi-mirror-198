# Dev guide for argparese_param_types
## How to package the project
### Dependencies
```
pip install build twine
```

### Build & upload
#### Production environment
```
python -m build
python -m twine upload --repository-url https://upload.pypi.org/legacy/ --repository argparse-param-types dist/*
```

#### Test environment
```
python -m build
python -m twine upload --repository-url https://test.pypi.org/legacy/ --repository argparse-param-types dist/*
```