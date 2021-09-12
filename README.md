# practice-python

First starting off, create a pip environment:

- Ensure we're on Python 3 with `pip --version`
- Run `pip install pipenv` or use `pip3` if necessary
- Use `pipenv shell` to enter the shell
- Confirm the virtual env is on Python 3 using `python --version`


## Utilizing pipenv
- Install packages with `pipenv install <package>`
- Create lockfile with `pipenv lock`

## Creating tests
- Install pytest with `pip install pytest`
- Create `tests` folder and create `__init__.py`
- Create a `test_unit.py` file to store the tests
- Tests and test files must be functions prefixed with `test_`
  - The `assert` keyword is available without imports
- Create a `test_assertions` function to check the length of an empty list, or something trivial just for now to verify that everythings working
- Run `pytest` to see our single test pass
