# netlify-lfs-resize-url

![PyPI - License](https://img.shields.io/pypi/l/lektor-netlify-lfs-resize-url) [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit) ![PyPI - Downloads](https://img.shields.io/pypi/dw/lektor-netlify-lfs-resize-url)

This plugin provides a filter that allows the user to generate [Netlify Image Transformation](https://www.netlify.com/docs/image-transformation/) resize URL parameters when working with [Netlify Large Media](https://www.netlify.com/docs/large-media/).

## Installation

You can install this plugin by running the following command in your project's directory:

```sh
lektor plugins add netlify-lfs-resize-url
```

## Usage

The `nf_resize` filter works in conjunction with the `url` filter as follows:

```jinja
{% for image in this.attachments.images %}
    <img src="{{ image|url|nf_resize(w=720) }}">
{% endfor %}
```

The above will return the following:

```html
<img src="/images/example.png?nf_resize=fit&w=720">
```

### Arguments

Arguments correspond to [Netlify transformation parameters](https://www.netlify.com/docs/image-transformation/#parameters-for-transformation).

| Argument | Accepts | Default |
|-------------|--------------------|---------|
| `nf_resize` | 'fit', 'smartcrop' | 'fit' |
| `h` | Positive integers | `null` |
| `w` | Positive integers | `null` |

## Development

### Testing

All of the tests can be run by executing `test.sh` with the pipenv shell activated.

#### Static analysis and checking

`mypy` is used for static analysis, and `flake8` is used for checking:

```sh
python -m mypy lektor_netlify_lfs_resize_url.py
python -m mypy test.py
python -m flake8 lektor_netlify_lfs_resize_url.py
python -m flake8 test.py
```

#### Unit testing

Python's built-in `unittest` framework is used for unit testing:

```sh
python -m unittest
```

#### Security

`bandit` is used for security testing:

```sh
python -m bandit lektor_netlify_lfs_resize_url.py
```

### Uploading the plugin to PyPI

```sh
python -m build
python -m twine upload dist/*
```
