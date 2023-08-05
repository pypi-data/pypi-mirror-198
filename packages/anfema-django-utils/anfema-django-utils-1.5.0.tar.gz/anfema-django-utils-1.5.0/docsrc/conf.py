# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import importlib
import os
import sys


sys.path.insert(0, os.path.abspath('..'))  # noqa

from anfema_django_utils import __version__  # noqa


# -- Project information -----------------------------------------------------
project = 'anfema-django-utils'
copyright = '2022, anfema GmbH'
author = 'anfema GmbH'
version = __version__
release = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',
    "sphinx.ext.intersphinx",
    'sphinx_copybutton',
    "sphinx_rtd_theme",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_css_files = [
    "extend-rtd-style.css",
]
add_module_names = False
autodoc_preserve_defaults = True
autodoc_docstring_signature = True
autosummary_generate = True  # Turn on sphinx.ext.autosummary

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Intersphinx
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": ("https://docs.djangoproject.com/en/stable/", "https://docs.djangoproject.com/en/stable/_objects/"),
}

# For objects which cannot be resolved by intersphinx
qualname_overrides = {
    "django.contrib.auth.base_user.BaseUserManager": "django.contrib.auth.models.BaseUserManager",
    "django.contrib.auth.base_user.AbstractBaseUser": "django.contrib.auth.models.AbstractBaseUser",
    "builtins.object": "object",
}


def get_canonical(obj: type) -> str:
    modules = obj.__module__.split(".")
    if canonical_fullname := qualname_overrides.get(f"{obj.__module__}.{obj.__qualname__}", None):
        return canonical_fullname
    for i in range(n_modules := len(modules)):
        if not (canonical_name := ".".join(modules[: n_modules - i - 1])):
            break
        canonical_module = importlib.import_module(canonical_name)
        if getattr(canonical_module, obj.__qualname__, None) is obj:
            return ".".join([canonical_name, obj.__qualname__])
    return f"{obj.__module__}.{obj.__qualname__}"


def adapt_base_classes(app, name, obj, options, bases) -> None:
    for idx, base in enumerate(bases):
        main_package, *_ = base.__module__.split(".")
        if main_package == "lys":
            continue  # Don`t try to adapt lys classes

        # If the base is not a lys project class display the full class name
        bases[idx] = f":py:class:`{get_canonical(base)}`"


def setup(app):
    app.connect("autodoc-process-bases", adapt_base_classes)
