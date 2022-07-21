from typing import (
    Callable,
    Union,
)

import numpy as np

from pandas._typing import ArrayLike

from pandas.core.dtypes.inference import (
    is_array_like as is_array_like,
    is_bool as is_bool,
    is_complex as is_complex,
    is_dict_like as is_dict_like,
    is_file_like as is_file_like,
    is_float as is_float,
    is_hashable as is_hashable,
    is_integer as is_integer,
    is_interval as is_interval,
    is_iterator as is_iterator,
    is_list_like as is_list_like,
    is_named_tuple as is_named_tuple,
    is_number as is_number,
    is_re as is_re,
    is_re_compilable as is_re_compilable,
    is_scalar as is_scalar,
)

ensure_float64 = ...
ensure_float32 = ...

def ensure_float(arr): ...

ensure_uint64 = ...
ensure_int64 = ...
ensure_int32 = ...
ensure_int16 = ...
ensure_int8 = ...
ensure_platform_int = ...
ensure_object = ...

def ensure_str(value) -> str: ...
def ensure_categorical(arr): ...
def ensure_python_int(value: Union[int, np.integer]) -> int: ...
def classes(*klasses) -> Callable: ...
def classes_and_not_datetimelike(*klasses) -> Callable: ...
def is_object_dtype(arr_or_dtype) -> bool: ...
def is_sparse(arr) -> bool: ...
def is_scipy_sparse(arr) -> bool: ...
def is_categorical(arr) -> bool: ...
def is_datetime64_dtype(arr_or_dtype) -> bool: ...
def is_datetime64tz_dtype(arr_or_dtype) -> bool: ...
def is_timedelta64_dtype(arr_or_dtype) -> bool: ...
def is_period_dtype(arr_or_dtype) -> bool: ...
def is_interval_dtype(arr_or_dtype) -> bool: ...
def is_categorical_dtype(arr_or_dtype) -> bool: ...
def is_string_dtype(arr_or_dtype) -> bool: ...
def is_period_arraylike(arr) -> bool: ...
def is_datetime_arraylike(arr) -> bool: ...
def is_dtype_equal(source, target) -> bool: ...
def is_any_int_dtype(arr_or_dtype) -> bool: ...
def is_integer_dtype(arr_or_dtype) -> bool: ...
def is_signed_integer_dtype(arr_or_dtype) -> bool: ...
def is_unsigned_integer_dtype(arr_or_dtype) -> bool: ...
def is_int64_dtype(arr_or_dtype) -> bool: ...
def is_datetime64_any_dtype(arr_or_dtype) -> bool: ...
def is_datetime64_ns_dtype(arr_or_dtype) -> bool: ...
def is_timedelta64_ns_dtype(arr_or_dtype) -> bool: ...
def is_datetime_or_timedelta_dtype(arr_or_dtype) -> bool: ...
def is_numeric_v_string_like(a, b): ...
def is_datetimelike_v_numeric(a, b): ...
def needs_i8_conversion(arr_or_dtype) -> bool: ...
def is_numeric_dtype(arr_or_dtype) -> bool: ...
def is_string_like_dtype(arr_or_dtype) -> bool: ...
def is_float_dtype(arr_or_dtype) -> bool: ...
def is_bool_dtype(arr_or_dtype) -> bool: ...
def is_extension_type(arr) -> bool: ...
def is_extension_array_dtype(arr_or_dtype) -> bool: ...
def is_complex_dtype(arr_or_dtype) -> bool: ...
def infer_dtype_from_object(dtype): ...
def pandas_dtype(dtype): ...