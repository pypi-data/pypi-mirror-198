# flaregun

A simple helper package for PyTorch to get better visibility on real-time GPU usage, model params, etc.

## Installation

```bash
$ pip install flaregun
```

## Usage

Get real-time Nvidia GPU memory usage in Python:

```python
from flaregun import GPUStats

# Pretty print statistics for GPU #0
GPUStats(device=0).print()
> "GPU memory usage: 3061 / 32510 MB"
```

Get parameter count in any PyTorch compatible model (e.g. HuggingFace, etc.):

```python
from flaregun import ModelStats

# Get HuggingFace model
model = AutoModelForMaskedLM.from_pretrained("/path/to/Longformer-Model")

# Pretty print Model parameter count
ModelStats(model).print()
> "148711257 params (148711257 trainable | 0 non-trainable)"
```

## API

All features of the library are listed below.

### GPU memory utilization

```python
from flaregun import GPUStats

device = ...integer of GPU device...

# Free GPU memory (in MB)
free_mem = GPUStats(device).free()

# Total GPU memory (in MB)
total_mem = GPUStats(device).total()

# Used GPU memory (in MB)
used_mem = GPUStats(device).used()
```

### Model parameter count

```python
from flaregun import ModelStats

model = ...PyTorch-compatible model...

# Total params
total = ModelStats(model).total()

# Trainable params
trainable = ModelStats(model).trainable()

# Frozen (non-trainable) params
frozen = ModelStats(model).frozen()
```
## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

### Running Tests

```bash
poetry run pytest tests/
```

### Test PyPI

Create release:
```
git tag vXX.XX.XXX
git push --tags
# Then go to Github and link this tag to a Release
```

Publish:

```bash
poetry publish -r test-pypi --username XXX --password XXXX
```

Install:
```bash
pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple flaregun
```

### PyPI

### Building Docs

```bash
cd docs
poetry run make clean html && poetry run make html
```
## License

`flaregun` was created by Michael Wornow. It is licensed under the terms of the MIT license.

## Credits

`flaregun` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
