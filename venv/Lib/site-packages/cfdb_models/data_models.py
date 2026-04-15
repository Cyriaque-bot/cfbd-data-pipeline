#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:23:18 2025

@author: mike
"""
import msgspec
import enum
from typing import Set, Optional, Dict, Tuple, List, Union, Any


####################################################
### Parameters





###################################################
### Models


class Type(enum.Enum):
    """

    """
    grid = 'grid'
    ts_ortho = 'ts_ortho'


class Compressor(enum.Enum):
    """

    """
    zstd = 'zstd'
    lz4 = 'lz4'


class Axis(enum.Enum):
    """

    """
    x = 'x'
    y = 'y'
    z = 'z'
    t = 't'
    xy = 'xy'
    xyz = 'xyz'


class DataType(msgspec.Struct):
    """

    """
    name: str
    precision: Union[int, float, None] = None
    dtype_encoded: Union[str, None] = None
    offset: Union[int, float, None] = None
    fillvalue: Union[int, None] = None


class DatasetAttrs(msgspec.Struct):
    """
    CF convention dataset (global/group) attributes (CF-1.12).
    See https://cfconventions.org/Data/cf-conventions/cf-conventions-1.12/cf-conventions.html#attribute-appendix
    """
    comment: Union[str, None] = None
    conventions: Union[str, None] = None
    external_variables: Union[str, None] = None
    feature_type: Union[str, None] = None
    history: Union[str, None] = None
    institution: Union[str, None] = None
    references: Union[str, None] = None
    source: Union[str, None] = None
    title: Union[str, None] = None


class VarAttrs(msgspec.Struct):
    """
    CF convention variable attributes (CF-1.12).
    See https://cfconventions.org/Data/cf-conventions/cf-conventions-1.12/cf-conventions.html#attribute-appendix
    """
    actual_range: Union[Tuple[float, float], None] = None
    add_offset: Union[int, float, None] = None
    ancillary_variables: Union[str, None] = None
    axis: Union[str, None] = None
    bounds: Union[str, None] = None
    calendar: Union[str, None] = None
    cell_measures: Union[str, None] = None
    cell_methods: Union[str, None] = None
    cf_role: Union[str, None] = None
    climatology: Union[str, None] = None
    comment: Union[str, None] = None
    compress: Union[str, None] = None
    computed_standard_name: Union[str, None] = None
    coordinate_interpolation: Union[str, None] = None
    coordinates: Union[str, None] = None
    dimensions: Union[str, None] = None
    fillvalue: Union[int, float, str, None] = None
    flag_masks: Union[Tuple[int, ...], None] = None
    flag_meanings: Union[str, None] = None
    flag_values: Union[Tuple[int, ...], None] = None
    formula_terms: Union[str, None] = None
    geometry: Union[str, None] = None
    geometry_type: Union[str, None] = None
    grid_mapping: Union[str, None] = None
    institution: Union[str, None] = None
    interior_ring: Union[str, None] = None
    leap_month: Union[int, None] = None
    leap_year: Union[int, None] = None
    location: Union[str, None] = None
    location_index_set: Union[str, None] = None
    long_name: Union[str, None] = None
    mesh: Union[str, None] = None
    missing_value: Union[int, float, str, None] = None
    month_lengths: Union[Tuple[int, ...], None] = None
    node_coordinates: Union[str, None] = None
    node_count: Union[str, None] = None
    nodes: Union[str, None] = None
    part_node_count: Union[str, None] = None
    positive: Union[str, None] = None
    quantization: Union[str, None] = None
    quantization_nsb: Union[int, None] = None
    quantization_nsd: Union[int, None] = None
    references: Union[str, None] = None
    scale_factor: Union[int, float, None] = None
    select: Union[str, None] = None
    source: Union[str, None] = None
    standard_error_multiplier: Union[int, float, None] = None
    standard_name: Union[str, None] = None
    units: Union[str, None] = None
    units_metadata: Union[str, None] = None
    valid_max: Union[int, float, None] = None
    valid_min: Union[int, float, None] = None
    valid_range: Union[Tuple[float, float], None] = None
    odm2_variable_name: Union[str, None] = None


class DataVarDef(msgspec.Struct, tag='data_var'):
    """
    Used to define the values that could be assigned before cfdb initializes a variable. It does not use VarAttrs for now...maybe I'll use it to restrict the attributes at a later time...
    """
    dtype: DataType
    attrs: Union[Dict, None] = None


class CoordVarDef(msgspec.Struct, tag='coord'):
    """
    Used to define the values that could be assigned before cfdb initializes a variable. It does not use VarAttrs for now...maybe I'll use it to restrict the attributes at a later time...
    """
    dtype: DataType
    step: Union[float, int, None] = None
    auto_increment: bool = False
    attrs: Union[Dict, None] = None




























































































