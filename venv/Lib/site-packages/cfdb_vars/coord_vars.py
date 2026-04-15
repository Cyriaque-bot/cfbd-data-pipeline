"""Coordinate variable definitions for cfdb."""

from cfdb_models.data_models import CoordVarDef, DataType

coord_var_defs = {
    'longitude': CoordVarDef(
        dtype=DataType(name='float64', precision=6, dtype_encoded='uint32', offset=-180.000001, fillvalue=0),
        attrs={
            'long_name': 'longitude',
            'units': 'degrees_east',
            'standard_name': 'longitude',
            'axis': 'X',
            'odm2_variable_name': 'longitude',
        },
    ),
    'latitude': CoordVarDef(
        dtype=DataType(name='float64', precision=6, dtype_encoded='uint32', offset=-90.000001, fillvalue=0),
        attrs={
            'long_name': 'latitude',
            'units': 'degrees_north',
            'standard_name': 'latitude',
            'axis': 'Y',
            'odm2_variable_name': 'latitude',
        },
    ),
    'height': CoordVarDef(
        dtype=DataType(name='float64', precision=3, dtype_encoded='uint32', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'height',
            'units': 'm',
            'standard_name': 'height',
            'positive': 'up',
            'axis': 'Z',
            'odm2_variable_name': 'height',
        },
    ),
    'altitude': CoordVarDef(
        dtype=DataType(name='float64', precision=3, dtype_encoded='uint32', offset=-11000.001, fillvalue=0),
        attrs={
            'long_name': 'altitude',
            'units': 'm',
            'standard_name': 'altitude',
            'positive': 'up',
            'axis': 'Z',
            'odm2_variable_name': 'altitude',
        },
    ),
    'time': CoordVarDef(
        dtype=DataType(name='datetime64[m]', dtype_encoded='int32', offset=-36816481),
        attrs={
            'long_name': 'time',
            'standard_name': 'time',
            'axis': 'T',
        },
    ),
    'x': CoordVarDef(
        dtype=DataType(name='float32', precision=1),
        attrs={
            'long_name': 'x coordinate of projection',
            'units': 'metres',
            'standard_name': 'projection_x_coordinate',
            'axis': 'X',
        },
    ),
    'y': CoordVarDef(
        dtype=DataType(name='float32', precision=1),
        attrs={
            'long_name': 'y coordinate of projection',
            'units': 'metres',
            'standard_name': 'projection_y_coordinate',
            'axis': 'Y',
        },
    ),
    'depth': CoordVarDef(
        dtype=DataType(name='float64', precision=3, dtype_encoded='uint32', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'depth below surface',
            'units': 'm',
            'standard_name': 'depth',
            'positive': 'down',
            'axis': 'Z',
        },
    ),
    'pressure': CoordVarDef(
        dtype=DataType(name='float64', precision=1, dtype_encoded='uint32', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'pressure',
            'units': 'Pa',
            'standard_name': 'air_pressure',
            'axis': 'Z',
        },
    ),
    'point': CoordVarDef(
        dtype=DataType(name='point', precision=5),
        attrs={
            'long_name': 'location geometry as points',
            'axis': 'XY',
        },
    ),
    'line': CoordVarDef(
        dtype=DataType(name='line', precision=5),
        attrs={
            'long_name': 'location geometry as lines',
            'axis': 'XY',
        },
    ),
    'polygon': CoordVarDef(
        dtype=DataType(name='polygon', precision=5),
        attrs={
            'long_name': 'location geometry as polygons',
            'axis': 'XY',
        },
    ),
}
