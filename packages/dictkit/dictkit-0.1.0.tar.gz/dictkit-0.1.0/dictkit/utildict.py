from __future__ import annotations
import sys
from collections import ChainMap
from typing import overload, Iterable, Mapping, TypeVar
from copy import copy

PANDAS_AVAILABLE = "pandas" in sys.modules
if PANDAS_AVAILABLE:
    from pandas import DataFrame, Series


def is_valid_normal_iterable(item) -> bool:
    if not isinstance(item, Iterable):
        return False
    if isinstance(item, Mapping):
        return False
    if isinstance(item, (str, bytes, bytearray)):
        return False
    return True


K = TypeVar("K")
V = TypeVar("V")
K2 = TypeVar("K2")
V2 = TypeVar("V2")


class UtilDict(dict[K, V]):
    """
    A better dictionary. Allows getting, setting, adding, and dropping items in useful ways,
    supporting dot notation item access, and getting/setting multiple keys and values at once.
    ----

    Get items with dot notation, if you wish

    Get multiple items at a time: `my_dict[['a', 'b']]` -> {'a': x, 'b': y}
      - Returns new, filtered instance

    Set multiple items at a time: `my_dict[['a', 'b']] = 10, 11`

    Set same value to multiple items: `my_dict[['a', 'b']] = 10`

    Add items, while returning a modified copy of self
      - `my_dict.add(a=5)` -> {<existing key/values>, 'a': 5}

    Drop items, while returning a modified copy of self
      - `my_dict.drop('a', 'b')` -> {<key/values excluding 'a' and 'b'>}

    Accepts a variety of argument types at creation
      - Accepts other dictionaries, 2-column dataframes, or iterables (lists or tuples) of
        length 2, to make key-value pairs from.
      - 2-column dataframes will be converted to key/value pairs using the first
        column as values
      - 2-element iterables will be converted to dictionaries with one key/value pair
        before being combined with other arguments

    Examples
    --------

    GPT-4 came up with and wrote all of these, given nothing other than the source code

    Initialize with a variety of types
    >>> sd = UtilDict({"a": 1}, [("b", 2)], c=3)
    >>> sd
    {'a': 1, 'b': 2, 'c': 3}

    Dot notation access
    >>> sd = UtilDict(a=1, b=2, c=3)
    >>> sd.a
    1

    Get multiple items at once
    >>> sd = UtilDict(a=1, b=2, c=3)
    >>> selected_items = sd[["a", "c"]]
    >>> selected_items
    {'a': 1, 'c': 3}

    Set multiple items at once
    >>> sd = UtilDict(a=1, b=2, c=3)
    >>> sd[["a", "c"]] = 10, 30
    >>> sd
    {'a': 10, 'b': 2, 'c': 30}

    Set the same value to multiple keys at once
    >>> sd = UtilDict(a=1, b=2, c=3)
    >>> sd[["a", "c"]] = 99
    >>> sd
    {'a': 99, 'b': 2, 'c': 99}

    Add items from a variety of types
    >>> sd = UtilDict(a=1, b=2)
    >>> sd2 = sd.add({"c": 3}, ("d", 4), e=5)
    >>> sd2
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    Add items from a 2-column dataframe
    >>> import pandas as pd
    >>> sd = UtilDict(a=1, b=2)
    >>> df = pd.DataFrame({"key": ["c", "d"], "value": [3, 4]})
    >>> df
      key  value
    0   c      3
    1   d      4
    >>> sd2 = sd.add(df)
    >>> sd2
    {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    Drop multiple items at once
    >>> sd = UtilDict(a=1, b=2, c=3, d=4)
    >>> sd2 = sd.drop("a", "c")
    >>> sd2
    {'b': 2, 'd': 4}
    """

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) == 2:
                # Special case. If two normal iterables, zip em together
                if is_valid_normal_iterable(args[0]) and is_valid_normal_iterable(
                    args[1]
                ):
                    return super().__init__(zip(*args), **kwargs)  # type:ignore

            args = [self._iterable_to_dict(arg) for arg in args]
            args = (ChainMap(*list(reversed(args))),)
        super().__init__(*args, **kwargs)

    def add(
        self, *args: Mapping[K2, V2] | Iterable, **kwargs: V2
    ) -> UtilDict[K | K2, V | V2]:
        """
        Add items, returning a copy with the new items.

        Parameters
        ----------
        *args
            Dictionaries or 2-element iterables
            to make key-value pairs from.
        **kwargs
            Key-value pairs to update.

        Returns
        -------
        Self
            A new UtilDict instance containing the original items and the added items.

        Examples
        --------
        >>> sd = UtilDict(a=1, b=2)
        >>> sd.add(c=3)
        {'a': 1, 'b': 2, 'c': 3}
        >>> sd.add({"d": 4}, e=5)
        {'a': 1, 'b': 2, 'd': 4, 'e': 5}
        """
        new = self.copy()

        args = [self._iterable_to_dict(arg) for arg in args]  # type:ignore
        for mapping in args:
            new.update(mapping)

        new.update(kwargs)
        return new

    @overload
    def drop(self, *keys, inplace: bool) -> None:
        ...

    @overload
    def drop(self, *keys) -> UtilDict:
        ...

    def drop(self, *keys, inplace=False):
        """
        Remove items by key, returning a copy with the items dropped.

        Parameters
        ----------
        *keys
            Keys of the items to remove.
        inplace : bool, optional, default: False
            If True, the items are removed from the UtilDict inplace, modifying the original instance.

        Returns
        -------
        Self or None
            A new updated instance, or None if inplace=True.

        Examples
        --------
        >>> sd = UtilDict(a=1, b=2, c=3)
        >>> sd.drop("a")
        {'b': 2, 'c': 3}
        >>> sd.drop("b", "c", inplace=True)
        >>> sd
        {'a': 1}
        """
        new = self if inplace else self.copy()

        if len(keys) == 1:
            if isinstance(keys[0], list):
                keys = keys[0]

        for k in keys:
            new.pop(k)

        if not inplace:
            return new

    def __getattr__(self, k):
        return self.__getitem__(k)

    def __setitem__(self, key, val):
        special_key_types = (list, type(...))
        if not isinstance(key, special_key_types):
            return super().__setitem__(key, val)

        if isinstance(key, type(...)):
            if PANDAS_AVAILABLE and isinstance(val, DataFrame):
                for c in val:
                    super().__setitem__(c, val[c])
            elif PANDAS_AVAILABLE and isinstance(val, Series):
                for k, v in val.to_dict():
                    super().__setitem__(k, v)
            elif isinstance(val, dict):
                for k, v in val.items():
                    super().__setitem__(k, v)
            else:
                raise ValueError(val)
            return

        assert isinstance(key, list), type(key)

        if isinstance(val, tuple) or (PANDAS_AVAILABLE and isinstance(val, Series)):
            if len(val) == len(key):
                for k, v in zip(key, val):
                    super().__setitem__(k, v)
            else:
                raise ValueError(
                    "Number of values assigned must equal number of keys assigning to"
                )
            return

        if PANDAS_AVAILABLE and isinstance(val, DataFrame):
            if len(val.columns) == len(key):
                for i, k in enumerate(key):
                    super().__setitem__(k, val[val.columns[i]])
            else:
                raise ValueError("DataFrame must have same number of columns as key")
            return

        for k in key:
            super().__setitem__(k, copy(val))

    @overload
    def __getitem__(self, key: K) -> V:
        ...

    @overload
    def __getitem__(self, key: list[K]) -> UtilDict[K, V]:
        ...

    def __getitem__(self, key):
        if not isinstance(key, list):
            return super().__getitem__(key)

        new = type(self).__new__(type(self))
        new.update(
            {k: super(type(self), self).__getitem__(k) for k in key}
        )  # Note: `super()` won't work inside comprehensions, so we have to pass type and instance directly
        return new

    def copy(self) -> UtilDict:
        new = type(self).__new__(self.__class__)
        new.update({k: copy(v) for k, v in self.items()})
        return new

    def __copy__(self) -> UtilDict:
        return self.copy()

    def _iterable_to_dict(self, arg) -> dict:

        if PANDAS_AVAILABLE:
            if isinstance(arg, DataFrame):
                if len(arg.columns) == 2:
                    return dict(zip(arg[arg.columns[0]], arg[arg.columns[1]]))
                if len(arg.columns) == 1:
                    return arg[arg.columns[0]].to_dict()
                raise ValueError(
                    "DataFrame must have one or two columns, to make key/val pairs from"
                )

            if isinstance(arg, Series):
                return arg.to_dict()

        if isinstance(arg, Mapping):
            return dict(arg)

        if not isinstance(arg, Iterable):
            # Let dict throw the error if not hashable
            return {arg: self.get(arg)}

        try:
            return dict(arg)
        except Exception:
            pass

        try:
            # When it's an iterable with valid keys but no values,
            # Set each key to None, but don't override where self already contains
            # a value for the key
            return {x: self.get(x) for x in arg}
        except Exception:
            pass

        # Ah, so we've got values that aren't valid keys. Use them as values instead lmao
        return {i: self.get(v) for i, v in enumerate(arg)}
