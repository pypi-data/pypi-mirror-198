"""Generic response models."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Iterable, Type, Union

from pydantic import BaseModel
from typing_extensions import NoReturn, Self, TypeAlias

from combadge.core.typevars import ResponseT


class BaseResponse(ABC, BaseModel):
    """Base model representing any possible service response."""

    @abstractmethod
    def raise_for_result(self) -> Union[None, NoReturn]:
        """Raise an exception if the service call has failed."""
        raise NotImplementedError

    @abstractmethod
    def expect(self, exception_type: Type[BaseException], *args: Any) -> Union[None, NoReturn]:
        """Raise the specified exception if the service call has failed."""
        raise NotImplementedError

    @abstractmethod
    def unwrap(self) -> Union[Self, NoReturn]:
        """Return itself if the call was successful, raises an exception otherwise."""
        raise NotImplementedError


class SuccessfulResponse(BaseResponse):
    """
    Parent model for successful responses.

    Note:
        - May be used directly when no payload is expected.
    """

    def raise_for_result(self) -> None:
        """
        Do nothing.

        This call is a no-op since the response is successful.
        """

    def expect(self, _exception_type: Type[BaseException], *_args: Any) -> None:
        """Do nothing."""

    def unwrap(self) -> Self:
        """Return itself since there's no error."""
        return self


class ErrorResponse(BaseResponse, ABC):
    """
    Parent model for faulty responses (errors).

    Notes:
        - Useful when server returns errors in a free from (for example, an `<error>` tag).
        - Must be subclassed.
        - For SOAP Fault use or subclass the specialized `GenericSoapFault`.
    """

    class Error(Generic[ResponseT], Exception):
        """
        Dynamically derived exception class.

        For each model inherited from `ErrorResponse` Combadge generates an exception
        class, which is accessible through the `<ModelClass>.Error` attribute.

        Examples:
            >>> class InvalidInput(ErrorResponse):
            >>>     code: Literal["INVALID_INPUT"]
            >>>
            >>> try:
            >>>     service.call(...)
            >>> except InvalidInput.Error:
            >>>     ...

        Notes:
            - The problem with `pydantic` is that you can't inherit from `BaseModel` and `Exception`
              at the same time. Thus, Combadge dynamically constructs a derived exception class,
              which is available via the class attribute and raised by `raise_for_result()` and `unwrap()`.
        """

        def __init__(self, response: ResponseT) -> None:
            """
            Instantiate the error.

            Args:
                response: original response that caused the exception.
            """
            super().__init__(response)

    def __init_subclass__(cls, exception_bases: Iterable[Type[BaseException]] = (), **kwargs: Any) -> None:
        """
        Build the derived exception class.

        Args:
            exception_bases: additional bases for the derived exception class
            kwargs: forwarded to the superclass
        """

        super().__init_subclass__(**kwargs)

        exception_bases = (
            # Inherit from the parent models' errors:
            *(base.Error for base in cls.__bases__ if issubclass(base, ErrorResponse)),
            # And from the user-provided ones:
            *exception_bases,
        )

        class DerivedException(*exception_bases):  # type: ignore
            """
            Derived exception class.

            Notes:
                - This docstring is overridden by the corresponding model docstring.
            """

        DerivedException.__name__ = f"{cls.__name__}.Error"
        DerivedException.__qualname__ = f"{cls.__qualname__}.Error"
        DerivedException.__doc__ = cls.__doc__ or DerivedException.__doc__
        cls.Error = DerivedException  # type: ignore

    def raise_for_result(self) -> NoReturn:
        """Raise the derived exception."""
        raise self.Error(self)

    def expect(self, exception_type: Type[BaseException], *args: Any) -> NoReturn:
        """Raise the specified exception with the derived exception context."""
        raise exception_type(*args) from self.Error(self)

    def unwrap(self) -> NoReturn:
        """Raise the derived exception."""
        raise self.Error(self)


BaseError: TypeAlias = ErrorResponse.Error
"""Base exception class for all errors derived from `ErrorResponse`."""
