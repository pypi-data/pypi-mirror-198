"""This module provides caching related utilities.

.. note:: This module is only supported with Python >= 3.9

.. versionadded:: 1.5
"""
from __future__ import annotations


__all__ = ("cached_call",)

import sys  # isort: skip

if not (sys.version_info.major == 3 and sys.version_info.minor >= 9):
    raise ImportError('The caching module is only available with Python >= 3.9')

import contextlib
import functools
import inspect
from collections import OrderedDict, abc
from typing import TYPE_CHECKING

from super_hash import super_hash


if TYPE_CHECKING:
    from types import ClassMethodDescriptorType
    from typing import Any, Callable


class _CachedCall:
    __slots__ = ("__wrapped__", "__signature__", "__cache__", "__dict__", "_maxsize")

    def __new__(cls, func: Callable | ClassMethodDescriptorType, *, maxsize: int = None) -> functools.partial:
        if inspect.ismethod(func):
            raise TypeError("Callable must not be an instant method.")
        elif inspect.isclass(func):
            raise TypeError("Callable must not be a class.")
        return functools.wraps(func)(super().__new__(cls))

    def __init__(self, func: functools.partial, maxsize: int) -> None:
        self.__wrapped__ = func
        self.__signature__ = inspect.signature(self)
        self.__cache__ = OrderedDict()

        # Ensure the cache`s size is at least 1
        self._maxsize = 1 if maxsize is not None and maxsize < 1 else maxsize

    def __get__(self, instance, owner=None) -> Callable:
        if instance is None:
            return self

        @functools.wraps(self.__wrapped__)
        def cached_call_proxy(cls, *args, **kwargs):
            return self(cls, *args, **kwargs)

        @functools.wraps(self.clear_call)
        def clear_call_proxy(cls, *args, **kwargs):
            return self.clear_call(cls, *args, **kwargs)

        cached_call_proxy.clear = self.clear
        cached_call_proxy.clear_call = clear_call_proxy.__get__(instance, owner)

        return cached_call_proxy.__get__(instance, owner)

    def __call__(self, *args, **kwargs) -> Any:
        hash_key = self._hash_parameters(*args, **kwargs)
        if hash_key in self.__cache__:
            return self.__cache__[hash_key]
        if len(self.__cache__) == self._maxsize:
            self.__cache__.pop(next(iter(self.__cache__)))  # Remove the first cache item if maxsize has been reached

        return self.__cache__.setdefault(hash_key, self._call_wrapped(*args, **kwargs))

    def __str__(self) -> str:
        return str(self.__wrapped__)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} object at 0x{id(self):x}: {repr(self.__wrapped__)}>"

    def _call_wrapped(self, *args, **kwargs) -> Any:
        """Calls the wrapped function directly without caching the call."""
        return getattr(self.__wrapped__, "__func__", self.__wrapped__)(*args, **kwargs)

    def _hash_parameters(self, *args, **kwargs) -> str:
        """Calculates a hash value for the given parameters"""
        bound_parameters = self.__signature__.bind(*args, **kwargs)
        bound_parameters.apply_defaults()
        return super_hash(bound_parameters.arguments)

    def clear_call(self, *args, **kwargs) -> None:
        """Clearing the callable`s cache for a specific call."""
        with contextlib.suppress(KeyError):
            self.__cache__.pop(self._hash_parameters(*args, **kwargs))

    def clear(self) -> None:
        """Clearing the callable`s complete cache."""
        self.__cache__.clear()


@functools.singledispatch
def cached_call(maxsize: int = 128):
    """Decorator to wrap a function with a memoizing callable similar to the :func:`functools.lru_cache` decorator.

    You can use the decorator on lambdas, functions, methods, classmethods and staticmethods.

    .. note:: Some callables may not be cachable in certain implementations of Python. For example, in CPython,
          built-in functions defined in C provide no metadata about their arguments.

    Unlike :func:`functools.lru_cache`, :func:`cached_call` provides the possibility to invalidate the cache for a
    specific call. The cache keeps references to the arguments and return values until they age out of the cache
    or until the cache is cleared via :meth:`clear_call` or :meth:`clear`.

    To cache the result :func:`cached_call` uses the positional and keyword arguments and creates a hash value using the
    `super_hash <https://github.com/jeff-hykin/super_hash>`_ library. Hence, the positional and keyword arguments must
    be hashable with `super_hash <https://github.com/jeff-hykin/super_hash>`_.

    If a method is cached, the ``self`` instance attribute is included in the cache. The same applies for the ``cls``
    attribute of a cached ``classmethod``.

    Distinct argument patterns does not result in separate cache entries, i.e. :code:`f(a=1, b=2)` and
    :code:`f(b=2, a=1)` have the same cache entry. You should consider that arguments with a default value are taken
    also into account for caching. I.e. a function with a signature :code:`f(a=None, b=True)` results in the same cache
    entry for the calls :code:`f(a=None)` and :code:`f(b=True)`. For methods, the calls
    :code:`Foo.bar(foo, *args, **kwargs)` and :code:`foo.bar(*args, **kwargs)` will be considered the same and thus also
    result in the same cache entry.

    If *user_function* is specified, it must be a callable. This allows the :func:`cached_call` decorator to be applied
    directly to a user function, leaving the *maxsize* at its default value of 128:

    .. code-block::

        @cached_call(maxsize=32)
        def foo(*args):
            ...

        @cached_call
        def bar(*args):
            ...

    If *maxsize* is set to ``None``, the cache can grow without bound.

    The original underlying callable is accessible through the :attr:`__wrapped__` attribute.

    To clear a cache entry for a specific call you can use :func:`clear_call` with passing the arguments, for which call
    the cache entry shall be cleared. To reset the complete cache, call :meth:`clear`:

    .. code-block::

        @cached_call
        def foo(*args):
            return uuid.uuid4()

        >>> foo(1)  # returns a new UUID
        UUID('9306c73b-ff0a-439b-901c-c347ac548904')
        >>> foo(1)  # returns the cached value
        UUID('9306c73b-ff0a-439b-901c-c347ac548904')
        >>> foo(2)  # returns a new UUID
        UUID('2e7ca126-7943-46cc-a81b-0fbd30b07969')
        >>> foo.clear_call(1)  # clear the cache only for the call foo(1)

        >>> foo(1)  # returns a new UUID
        UUID('3b3cc8b2-6ec5-4582-8314-926aa625b1fc')
        >>> foo(2)  # returns the cached value
        UUID('2e7ca126-7943-46cc-a81b-0fbd30b07969')
        >>> foo.clear()  # clear the cache for all calls
    """
    if type(maxsize) not in (int, type(None)):
        raise TypeError("cached_call() requires a callable, integer or None.")
    return functools.partial(_CachedCall, maxsize=maxsize)


@cached_call.register
def _(user_function: abc.Callable):
    return _CachedCall(user_function, maxsize=128)
