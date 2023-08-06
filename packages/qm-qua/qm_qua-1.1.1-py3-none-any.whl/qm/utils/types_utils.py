from typing import TypeVar, Collection, Type, Iterable, Any, Set, Union, Optional, cast, Sequence

import numpy as np
import numpy.typing

from qm.type_hinting import Value, NumpySupportedValue


def fix_object_data_type(obj: Optional[NumpySupportedValue]) -> Optional[Value]:
    if isinstance(obj, (np.floating, np.integer, np.bool_)):
        obj_item = obj.item()
        if isinstance(obj_item, np.longdouble):
            return float(obj_item)
        else:
            return obj_item
    else:
        return obj


def get_all_iterable_data_types(it: Iterable[Any]) -> Set[Type[Any]]:
    return {type(e) for e in it}


C = TypeVar("C")


def collection_has_type(collection: Collection[C], type_to_check: Type[C], include_subclasses: bool) -> bool:
    if include_subclasses:
        return any([isinstance(i, type_to_check) for i in collection])
    else:
        return any([type(i) is type_to_check for i in collection])


def collection_has_type_bool(collection: Collection[C]) -> bool:
    return collection_has_type(collection, bool, False) or collection_has_type(collection, np.bool_, True)


def collection_has_type_int(collection: Collection[C]) -> bool:
    return collection_has_type(collection, int, False) or collection_has_type(collection, np.integer, True)


def collection_has_type_float(collection: Collection[C]) -> bool:
    return collection_has_type(collection, float, False) or collection_has_type(collection, np.floating, True)


def is_iter(x: Any) -> bool:
    try:
        iter(x)
    except TypeError:
        return False
    else:
        return True


def get_iterable_elements_datatype(it: Union[numpy.typing.NDArray[Any], Sequence[Any], Any]) -> Optional[Type[Any]]:
    if isinstance(it, np.ndarray):
        return type(it[0].item())
    elif is_iter(it):
        sequence = cast(Sequence[Any], it)
        if len(get_all_iterable_data_types(sequence)) > 1:
            raise ValueError("Multiple datatypes encountered in iterable object")
        if isinstance(sequence[0], np.generic):
            return type(sequence[0].item())
        else:
            return type(sequence[0])
    else:
        return None
