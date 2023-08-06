from copy import copy
from functools import singledispatchmethod
from typing import Any, Callable, Generic, List, Optional, Type, TypeVar, Union, overload

from typing_extensions import Concatenate, ParamSpec, Self

from .scope import BaseScope

_retval = TypeVar("_retval")
_params = ParamSpec("_params")
_owner = TypeVar("_owner", bound=BaseScope)


class hook(Generic[_owner, _params, _retval]):
    """The :class:`hook` class provides a flexible way to define and override specific functions.

    A hook can be created with or without an initial defination, where later ones are called
    :obj:`.anonymous`.

    A hook saves all of its override history in its :obj:`.__stack__`. So it is possible to access
    its :meth:`.super` as what you can do in a method.

    Note that we assume hooks are all **methods**. Hooks MUST be a method of :class:`BaseScope`.
    """

    __slots__ = ("__owner__", "__def__", "__stack__")
    __owner__: Union[Type[_owner], _owner]
    """This is an attribute that will be set by :class:`BaseEvent`.
    """

    __def__: Union[Callable[Concatenate[_owner, _params], _retval], str]
    """The original defination of this hook.

    - If this hook is anonymous, this is a str **after it is first assigned to a class**.
    - If this hook is created with a defination, this is a ref to the defination method.
    """

    __stack__: List[Callable[Concatenate[_owner, _params], _retval]]
    """The override stack. Once the hook is overrided, the function will be pushed into this stack.
    Current ref is the top of the stack.
    """

    @singledispatchmethod
    def __set_name__(self, owner, name: str):
        return

    @__set_name__.register(type(BaseScope))
    def _(self, owner: Type[_owner], name: str):
        if not issubclass(owner, BaseScope):
            return

        self.__owner__ = owner
        if not hasattr(self, "__def__"):
            self.__def__ = owner.__qualname__ + "." + name
        if self.overrided and name != self.name:
            setattr(owner, self.name, self)
        if not self.overrided and name not in owner.__hooks__:
            hooks = list(owner.__hooks__)
            hooks.append(name)
            setattr(owner, "__hooks__", tuple(hooks))

    def __new__(
        cls,
        defination: Optional[Callable[Concatenate[_owner, _params], _retval]] = None,
    ):
        """Create a hook with an optional defination. If the defination is not given,
        then this will be an anonymous hook.

        :param defination: an optional defination of this hook.
        """
        self = super().__new__(cls)
        self.__stack__ = []
        if defination is not None:
            self.__def__ = defination
            self.__stack__.append(defination)
        return self

    def __deepcopy__(self, *_) -> Self:
        o = copy(self)
        o.__stack__ = o.__stack__.copy()
        return o

    def __call__(self, *args: _params.args, **kwds: _params.kwargs) -> _retval:
        """
        :raise TypeError: if owner of the hook is not initialized.
        """
        # we assume that a hook always belongs to an instance
        # so if __owner__ is a class we will raise exception
        if not hasattr(self, "__owner__") or isinstance(self.__owner__, type):
            raise TypeError("Initialize an instance before calling its hook!")
        if not self.__stack__:
            # for hooks has empty __stack__, it is defined w/o return type
            # it is expected that the hook is called with its retval being discard.
            # so we can return None since whatever we return, it is dropped.
            return  # type: ignore
        return self.__stack__[-1](self.__owner__, *args, **kwds)

    @property
    def name(self):
        """Get hook name.

        - If this hook is anonymous, its name is its attribute name.
        - If this hook has a defination, its name is its defination method name.
        """
        if isinstance(self.__def__, str):
            return self.__def__.rsplit(".", maxsplit=1)[-1]
        return self.__def__.__name__

    @property
    def overrided(self):
        """Check whether this hook is overrided.

        - If the hook is anonymous, when :obj:`__stack__` is not empty, it is overrided.
        - If the hook is created with a defination, when :obj:`__stack__` has the second element, it's overrided.
        """
        return len(self.__stack__) > (0 if self.anonymous else 1)

    @property
    def anonymous(self):
        """A hook is anonymous if it is created without a defination.

        If so, the hook object will hold its qualname instead of a ref to the defination method.
        Thus if :obj:`.__def__` is a str, the hook is anonymous.
        """
        return not hasattr(self, "__def__") or isinstance(self.__def__, str)

    @overload
    def override(self, method: Callable[Concatenate[_owner, _params], _retval], /) -> Self:
        ...

    @overload
    def override(
        self, /, *, inplace: bool
    ) -> Callable[[Callable[Concatenate[Any, _params], _retval]], Self]:
        # BUG: we use Any instead of _owner since this overload is typically used in
        # override defined in subclass. They are called through superclass.hookname.override(inplace=True),
        # so _owner will be resolved as superclass, which is incompatible with subclass.
        ...

    def override(
        self,
        method: Callable[Concatenate[_owner, _params], _retval] = ...,
        /,
        *,
        inplace=True,
    ) -> Union[Self, Callable[[Callable[Concatenate[_owner, _params], _retval]], Self]]:
        """Override a hook.

        :param method: the new callable.
        :param inplace: whether this hook is overrided inplace. Default is True.
            If not, a new hook instance will be constructed. Note that in this case you should make sure
            this new hook instance is set back to the class.
        :return: a hook that is overrided by the given method.
        """

        def wrap(method) -> Self:
            if inplace:
                self.__stack__.append(method)
                return self

            o = self.__deepcopy__()
            return o.override(method)

        if method is ...:
            return wrap

        return wrap(method)

    def super(self) -> Self:
        """Get super of this hook. If the hook is not overrided, it will raise exception.

        :return: super of this hook
        :raise AttributeError: if hook is not overrided.
        """
        if not self.overrided:
            raise AttributeError(f"No super defination found for {self}")

        o = self.__deepcopy__()
        o.__stack__.pop()
        return o

    def __repr__(self) -> str:
        root = self.__def__ if isinstance(self.__def__, str) else self.__def__.__qualname__
        return f'<hook {self.name} defined at "{root}">'
