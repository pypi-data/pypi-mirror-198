# anfema-django-utils

Collection of various django related utilities, helpers & small apps.

https://anfema.github.io/anfema-django-utils/

## Documentation

To build the documentation from the local sources run: 
```bash
$ pip install tox && tox -e docs
```

## Tests

To run the unittests from the local sources run: 
```bash
$ pip install tox && tox
```

## Release process

Steps required to create a new release and publish the package on PyPI: 

1. Bump `__version__` in `anfema_django_utils/__ini__.py`
2. Create a new release on GitHub with the tag `v<version>`
