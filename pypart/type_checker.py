from types import UnionType
from typing import Any, ClassVar, Iterable


class TypeChecker:
    _ITERABLES: ClassVar[list[Iterable]] = [
        list,
        tuple,
        dict,
        set,
    ]

    @classmethod
    def raise_for(
        cls,
        value: Any,
        expec_type: Any,
    ) -> None:
        # Control the root type
        if hasattr(expec_type, '__origin__'):
            if type(value) != expec_type.__origin__:
                cls._raise(type(value), expec_type)
        else:
            if type(value) != expec_type:
                cls._raise(type(value), expec_type)

        # Control the subtypes if exists
        if hasattr(expec_type, '__args__') and expec_type.__args__:
            if expec_type.__origin__ == list:
                for item in value:
                    cls.raise_for(item, expec_type.__args__[0])
            elif expec_type.__origin__ == tuple:
                for i, type_ in enumerate(expec_type.__args__):
                    try:
                        cls.raise_for(value[i], type_)
                    except IndexError:
                        raise cls._raise(type(None), type_)
            elif expec_type.__origin__ == dict:
                key_type: Any = expec_type.__args__[0]
                value_types: tuple[Any] = (expec_type.__args__[1],)

                if type(expec_type.__args__[1]) == UnionType:
                    value_types = expec_type.__args__[1].__args__

                for key, val in value.items():
                    if type(key) != key_type:
                        cls._raise(type(key), key_type)

                    if not type(val) in value_types:
                        cls._raise(type(val), value_types)

    @classmethod
    def _raise(cls, value_type: Any, expec_type: Any) -> None:
        raise TypeError(f'Expected {expec_type}, got {value_type}.')
