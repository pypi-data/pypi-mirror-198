from __future__ import annotations

import sys
from copy import deepcopy
from typing import TYPE_CHECKING, Any, Dict, Iterable, Tuple, Type

if sys.version_info < (3, 11):
    from typing_extensions import Self
else:
    from typing import Self

if TYPE_CHECKING:
    from .hooks import hook


def _intersection(*keys: Iterable[str]):
    """Calculate intersection of the given str iterables.

    :meta private:
    """
    u, i = set(), set()
    for s in keys:
        i.update(u.intersection(s))
        u.update(s)
    return i


class ScopeMeta(type):
    """Metaclass for scopes. This handles inheritance of scope classes, or more precisely, the inherit logic
    of the hooks.
    """

    def __new__(
        cls,
        name: str,
        bases: Tuple[Type[BaseScope], ...],
        namespace: Dict[str, Any],
        **kwds,
    ):
        """Create new :class:`BaseScope` type. :obj:`~BaseScope.__hooks__` field will be copied or
        created.

        If a multi-inheritance happens, all :obj:`~BaseScope.__hooks__` filed from
        :class:`BaseScope` bases are collected. If base classes have hooks that are registered with
        the same name, it will raise for name conflict.

        :meta public:
        """
        scopes = [c for c in bases if issubclass(c, BaseScope)]
        # metaclass will ensure bases have __hooks__ as a dict
        if itsc := _intersection(*(c.__hooks__ for c in scopes)):
            raise TypeError("Cannot merge hooks: hook name conflict.", list(itsc))

        ty: Type[BaseScope] = super().__new__(cls, name, bases, namespace, **kwds)  # type: ignore

        hooks = list(ty.__hooks__)
        for c in scopes:
            for name in c.__hooks__:
                hooks.append(name)
                b = ty if name in ty.__dict__ else c
                setattr(ty, name, deepcopy(b.__dict__[name]))
        ty.__hooks__ = tuple(hooks)
        return ty


class BaseScope(metaclass=ScopeMeta):
    """One hook must belongs to a scope. :class:`BaseScope` is the base class for all scopes.

    A scope records hook names in its :obj:`.__hooks__` field.

    Scopes can be inherited. Their :obj:`.__hooks__` filed will be copied. See :meth:`ScopeMeta.__new__`.

    Once a scope is initialized, hooks in their :obj:`.__hooks__` field will get their :obj:`~hook.__owner__`
    field be changed to this scope object. This makes a hook callable.
    """

    __hooks__: Tuple[str, ...] = ()
    """A field to record registered hook name.

    .. note::

        This is a variable stored in class. The instance of this class will not have
        this variable stored in its field. But they can access this field **as if**
        they own this variable.

    :meta public:
    """

    def __new__(cls, *args, **kwds) -> Self:
        """Copy hooks from :obj:`.__hooks__` to instance field, hooks set to instance field will have an
        initialized `~hook.__owner__` field. This makes the hooks callable.

        :meta public:
        """
        self = super().__new__(cls, *args, **kwds)
        for name in self.__hooks__:
            o = getattr(self, name)  # type: hook
            o = deepcopy(o)
            o.__owner__ = self
            setattr(self, name, o)
        return self
