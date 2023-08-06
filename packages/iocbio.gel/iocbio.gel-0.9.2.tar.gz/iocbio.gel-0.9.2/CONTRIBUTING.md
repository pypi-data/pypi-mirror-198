# Contributing guide

## Make Changes

### Coding conventions

This project follows [PEP 8 Style Guide](https://peps.python.org/pep-0008/) in conjunction
with [The Black code style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#code-style).

In addition, the class attribute order should follow the list described in [setup.cfg](./setup.cfg).

### Before you commit

To reduce build pipeline usage, please check your style before pushing your code.
```bash
python -m pip install flake8
python -m pip install flake8-class-attributes-order
python -m pip install black
```

Run both the [Black formatter](https://black.readthedocs.io/en/stable/index.html) and
[Flake8 style checker](https://flake8.pycqa.org/en/latest/) via console `black iocbio` and `flake8`
or through your IDE and fix any issues they rise.
