# Neutron

Neutron scattering physics simulation

<div align="center">
    <img src="./resources/images/distance.png" width="512" height="512" />
</div>

## Installation

### Dependencies

-   [Rust](https://www.rust-lang.org/tools/install)

### Quickstart

Downloading the release tool should be as simple as:

```shell
cargo install neutrons
```

Create a directory called `input`, and within it add a parameters file called `parameters.json`:

```shell
mkdir input
touch input/parameters.json
```

The parameters file should look something like [this](./input/parameters.json).

You can then run the program with:

```shell
neutrons parameters.json
```
