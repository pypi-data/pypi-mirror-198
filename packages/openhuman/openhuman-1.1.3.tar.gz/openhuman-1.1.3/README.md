# OpenHuman.ai - Relastic virtual human assistant

Homepage: http://OpenHuman.ai/
Github: https://github.com/OpenHuman-ai/python-openhuman
Orgs: https://github.com/OpenHuman-ai

## Installation Steps

1. Create a setup.py file for your package, which includes information about your package such as its name, version, author, and dependencies.

2. Create a source distribution and a wheel distribution of your package by running the following commands in your terminal:

```bash
python3 setup.py sdist bdist_wheel
```

3. Create an account on PyPI if you haven't already done so. You can create an account by going to https://pypi.org/account/register/ and filling out the form.

4. Install the twine package, which is used to upload your package to PyPI:

```
pip install twine
```

5. Upload your package to PyPI using twine:

```
twine upload dist/*
```

6. Your package is now published on PyPI! Users can install it using pip install mypackage.
