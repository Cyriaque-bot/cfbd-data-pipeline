"""Time-resolution DataType definitions for datetime64 encoding."""

from cfdb_models.data_models import DataType

time_dtype_params = {
    'datetime64[M]': DataType(name='datetime64[M]', dtype_encoded='int16', offset=-841),
    'datetime64[D]': DataType(name='datetime64[D]', dtype_encoded='int32', offset=-25568),
    'datetime64[h]': DataType(name='datetime64[h]', dtype_encoded='int32', offset=-613609),
    'datetime64[m]': DataType(name='datetime64[m]', dtype_encoded='int32', offset=-36816481),
    'datetime64[s]': DataType(name='datetime64[s]', dtype_encoded='int64', offset=-2208988801),
    'datetime64[ms]': DataType(name='datetime64[ms]', dtype_encoded='int64', offset=-2208988800001),
    'datetime64[us]': DataType(name='datetime64[us]', dtype_encoded='int64', offset=-2208988800000001),
    'datetime64[ns]': DataType(name='datetime64[ns]', dtype_encoded='int64', offset=-631152000000000001),
}
