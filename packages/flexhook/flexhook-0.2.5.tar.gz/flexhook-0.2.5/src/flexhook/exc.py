from __future__ import annotations

from contextlib import AbstractContextManager, ContextDecorator
from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from .hooks import hook


class HookError(Exception):
    """Means an error was raised from a hook. This hook is saved in :obj:`.hook` field.

    Note that in order to debug the reason of this error, you should always use the raise-from syntax:
    >>> raise HookError(hook=error_hook) from raised_exc
    """

    def __init__(self, *args: object, hook: hook) -> None:
        super().__init__(*args, hook)
        self.hook = hook
        """The hook that raised an error."""


class hook_guard(AbstractContextManager, ContextDecorator):
    """A context manager to catch specific exceptions and raise :exc:`HookError` instead.

    This is useful if you want to dismiss all error raised from a hook. Then any exception
    will be transformed to :exc:`HookError` which is easy to catch.
    """

    def __init__(self, hook, *catch: Type[BaseException]) -> None:
        """
        :param hook: The hook you used in this context.
        :param catch: What exceptions to catch. If not given, all exceptions are caught.
        """
        self._hook = hook
        self._catch = catch

    def _recreate_cm(self):
        return self.__class__(self._hook, *self._catch)

    def __enter__(self):
        """
        :return: the hook that is passed in
        """
        return self._hook

    def __exit__(self, exctype: Type[BaseException], excinst: BaseException, exctb):
        if exctype is None:
            # no exception
            return
        if not self._catch or issubclass(exctype, self._catch):
            raise HookError(hook=self._hook) from excinst
