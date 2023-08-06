import pathlib
import numpy
from typing import TypeVar, Union, ClassVar
from typing_extensions import Protocol

PathLike = TypeVar("PathLike", str, pathlib.Path)
Number = Union[int, float]
Value = Union[Number, bool]

NumpyNumber = Union[numpy.floating, numpy.integer]
NumpyValue = Union[NumpyNumber, numpy.bool_]

NumpySupportedNumber = Union[Number, NumpyNumber]
NumpySupportedFloat = Union[float, numpy.floating]
NumpySupportedValue = Union[Value, NumpyValue]


class DataClassType(Protocol):
    __dataclass_fields__: ClassVar[dict]
