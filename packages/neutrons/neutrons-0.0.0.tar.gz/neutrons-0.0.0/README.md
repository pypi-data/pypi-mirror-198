# Neutron

Neutron scattering physics simulation

## Installation

### Dependencies

-   [Git](https://git-scm.com/downloads)
-   [Python 3.8+](https://www.python.org/downloads/)
-   [Poetry](https://python-poetry.org/docs/#installation)
-   [Rust](https://www.rust-lang.org/tools/install)

### Quickstart

Clone the repository:

```shell
git clone https://github.com/FreddyWordingham/Neutron.git neutron
cd neutron
```

Install the dependencies:

```shell
poetry install
```

Build the package:

```shell
poetry run maturin develop --release
```

Install the package:

```shell
poetry run pip install .
```

Run the example script:

```shell
poetry run python scripts/run.py
```
