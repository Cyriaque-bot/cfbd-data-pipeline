"""Data variable definitions for cfdb."""

from cfdb_models.data_models import DataType, DataVarDef

data_var_defs = {
    'modified_date': DataVarDef(
        dtype=DataType(name='datetime64[us]', dtype_encoded='int64', offset=1756684800000000),
        attrs={
            'long_name': 'last modified date',
        },
    ),
    'band': DataVarDef(
        dtype=DataType(name='uint8'),
        attrs={
            'long_name': 'band number',
        },
    ),
    'censor_code': DataVarDef(
        dtype=DataType(name='uint8'),
        attrs={
            'long_name': 'data censor code',
            'standard_name': 'status_flag',
            'flag_values': '0 1 2 3 4 5',
            'flag_meanings': 'greater_than less_than not_censored non-detect present_but_not_quantified unknown',
        },
    ),
    'precipitation': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'precipitation',
            'units': 'mm',
            'standard_name': 'precipitation_amount',
            'odm2_variable_name': 'precipitation',
        },
    ),
    'air_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'air temperature',
            'units': 'K',
            'standard_name': 'air_temperature',
        },
    ),
    'wind_speed': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'wind speed',
            'units': 'm/s',
            'standard_name': 'wind_speed',
            'odm2_variable_name': 'windSpeed',
        },
    ),
    'wind_direction': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'wind direction',
            'units': 'deg',
            'standard_name': 'wind_to_direction',
            'odm2_variable_name': 'windDirection',
        },
    ),
    'u_wind': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-101, fillvalue=0),
        attrs={
            'long_name': 'eastward wind component',
            'units': 'm/s',
            'standard_name': 'eastward_wind',
        },
    ),
    'v_wind': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-101, fillvalue=0),
        attrs={
            'long_name': 'northward wind component',
            'units': 'm/s',
            'standard_name': 'northward_wind',
        },
    ),
    'relative_humidity': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'relative humidity',
            'units': 'm^3/m^3',
            'standard_name': 'relative_humidity',
            'odm2_variable_name': 'relativeHumidity',
        },
    ),
    'dew_point_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'dew point temperature',
            'units': 'K',
            'standard_name': 'dew_point_temperature',
            'odm2_variable_name': 'temperatureDewPoint',
        },
    ),
    'soil_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'soil temperature',
            'units': 'K',
            'standard_name': 'soil_temperature',
        },
    ),
    'lwe_soil_moisture': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'liquid water equivalent of soil moisture',
            'units': 'mm',
            'standard_name': 'lwe_thickness_of_soil_moisture_content',
        },
    ),
    'surface_pressure': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint32', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'surface pressure',
            'units': 'Pa',
            'standard_name': 'surface_air_pressure',
        },
    ),
    'specific_humidity': DataVarDef(
        dtype=DataType(name='float32', precision=6, dtype_encoded='uint16', offset=-0.000001, fillvalue=0),
        attrs={
            'long_name': 'specific humidity',
            'units': 'kg kg-1',
            'standard_name': 'specific_humidity',
        },
    ),
    'mixing_ratio': DataVarDef(
        dtype=DataType(name='float32', precision=6, dtype_encoded='uint16', offset=-0.000001, fillvalue=0),
        attrs={
            'long_name': 'water vapor mixing ratio',
            'units': 'kg kg-1',
            'standard_name': 'humidity_mixing_ratio',
        },
    ),
    'shortwave_radiation': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'downward shortwave radiation at surface',
            'units': 'W m-2',
            'standard_name': 'surface_downwelling_shortwave_flux_in_air',
            'odm2_variable_name': 'radiationIncomingShortwave',
        },
    ),
    'longwave_radiation': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'downward longwave radiation at surface',
            'units': 'W m-2',
            'standard_name': 'surface_downwelling_longwave_flux_in_air',
            'odm2_variable_name': 'radiationIncomingLongwave',
        },
    ),
    'snow_depth': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'physical snow depth',
            'units': 'm',
            'standard_name': 'surface_snow_thickness',
            'odm2_variable_name': 'snowDepth',
        },
    ),
    'mslp': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint32', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'mean sea level pressure',
            'units': 'Pa',
            'standard_name': 'air_pressure_at_mean_sea_level',
        },
    ),
    'vorticity': DataVarDef(
        dtype=DataType(name='float32', precision=5, dtype_encoded='uint16', offset=-0.300001, fillvalue=0),
        attrs={
            'long_name': 'relative vorticity',
            'units': 's-1',
            'standard_name': 'atmosphere_relative_vorticity',
        },
    ),
    'vertical_velocity': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-50.01, fillvalue=0),
        attrs={
            'long_name': 'vertical velocity',
            'units': 'm s-1',
            'standard_name': 'upward_air_velocity',
        },
    ),
    'sensible_heat_flux': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-300.1, fillvalue=0),
        attrs={
            'long_name': 'upward sensible heat flux',
            'units': 'W m-2',
            'standard_name': 'surface_upward_sensible_heat_flux',
            'odm2_variable_name': 'sensibleHeatFlux',
        },
    ),
    'moisture_flux': DataVarDef(
        dtype=DataType(name='float32', precision=6, dtype_encoded='uint16', offset=-0.010001, fillvalue=0),
        attrs={
            'long_name': 'upward moisture flux',
            'units': 'kg m-2 s-1',
            'standard_name': 'water_evapotranspiration_flux',
        },
    ),
    'albedo': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'surface albedo',
            'units': '1',
            'standard_name': 'surface_albedo',
            'odm2_variable_name': 'albedo',
        },
    ),
    'emissivity': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'surface emissivity',
            'units': '1',
            'standard_name': 'surface_longwave_emissivity',
        },
    ),
    'terrain_height': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'terrain height above sea level',
            'units': 'm',
            'standard_name': 'surface_altitude',
        },
    ),
    'potential_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'air potential temperature',
            'units': 'K',
            'standard_name': 'air_potential_temperature',
        },
    ),
    'equivalent_potential_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'equivalent potential temperature',
            'units': 'K',
            'standard_name': 'equivalent_potential_temperature',
        },
    ),
    'geopotential_height': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint32', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'geopotential height',
            'units': 'm',
            'standard_name': 'geopotential_height',
        },
    ),
    'land_sea_mask': DataVarDef(
        dtype=DataType(name='uint8'),
        attrs={
            'long_name': 'land sea mask',
            'units': '1',
            'standard_name': 'land_binary_mask',
        },
    ),
    'sea_ice': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'sea ice area fraction',
            'units': '1',
            'standard_name': 'sea_ice_area_fraction',
        },
    ),
    'sea_surface_temp': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'sea surface temperature',
            'units': 'K',
            'standard_name': 'sea_surface_temperature',
        },
    ),
    'snow_water_equiv': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'snow water equivalent',
            'units': 'kg m-2',
            'standard_name': 'lwe_thickness_of_surface_snow_amount',
        },
    ),
    'soil_moisture': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'volumetric soil moisture',
            'units': 'm3 m-3',
            'standard_name': 'volume_fraction_of_condensed_water_in_soil',
        },
    ),
    'soil_layer_temp': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'soil layer temperature',
            'units': 'K',
            'standard_name': 'soil_temperature',
        },
    ),
    'pwat': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'total precipitable water',
            'units': 'kg m-2',
            'standard_name': 'atmosphere_mass_content_of_water_vapor',
        },
    ),
    'vimf_u': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint32', offset=-5000.1, fillvalue=0),
        attrs={
            'long_name': 'eastward vertically integrated moisture flux',
            'units': 'kg m-1 s-1',
            'standard_name': 'eastward_atmosphere_water_transport_across_unit_distance',
        },
    ),
    'vimf_v': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint32', offset=-5000.1, fillvalue=0),
        attrs={
            'long_name': 'northward vertically integrated moisture flux',
            'units': 'kg m-1 s-1',
            'standard_name': 'northward_atmosphere_water_transport_across_unit_distance',
        },
    ),
    'land_use_modis': DataVarDef(
        dtype=DataType(name='uint8'),
        attrs={
            'long_name': 'land use category for modis',
            'flag_values': '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21',
            'flag_meanings': (
                'evergreen_needleleaf_forests evergreen_broadleaf_forests deciduous_needleleaf_forests'
                ' deciduous_broadleaf_forests mixed_forests closed_shrublands open_shrublands woody_savannas'
                ' savannas grasslands permanent_wetlands croplands urban_and_built_up'
                ' cropland_natural_vegetation_mosaics permanent_snow_and_ice barren water_bodies wooded_tundra'
                ' mixed_tundra barren_tundra lakes'
            ),
        },
    ),

    # --- Temperature / Energy ---

    'skin_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'skin temperature',
            'units': 'K',
            'standard_name': 'surface_temperature',
        },
    ),
    'snow_layer_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'temperature of snow layer',
            'units': 'K',
            'standard_name': 'temperature_in_surface_snow',
        },
    ),
    'ice_surface_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'ice surface temperature',
            'units': 'K',
            'standard_name': 'surface_temperature',
        },
    ),
    'cape': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'convective available potential energy',
            'units': 'J kg-1',
            'standard_name': 'atmosphere_convective_available_potential_energy',
        },
    ),

    # --- Snow / Surface ---

    'snow_density': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'snow density',
            'units': 'kg m-3',
            'standard_name': 'snow_density',
        },
    ),
    'snow_albedo': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'snow albedo',
            'units': '1',
            'standard_name': 'snow_albedo',
        },
    ),
    'skin_reservoir_content': DataVarDef(
        dtype=DataType(name='float32', precision=4, dtype_encoded='uint16', offset=-0.0001, fillvalue=0),
        attrs={
            'long_name': 'skin reservoir content',
            'units': 'm of water equivalent',
        },
    ),
    'surface_roughness': DataVarDef(
        dtype=DataType(name='float32', precision=4, dtype_encoded='uint16', offset=-0.0001, fillvalue=0),
        attrs={
            'long_name': 'forecast surface roughness',
            'units': 'm',
            'standard_name': 'surface_roughness_length',
        },
    ),
    'surface_roughness_heat': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-15.01, fillvalue=0),
        attrs={
            'long_name': 'forecast logarithm of surface roughness for heat',
            'units': '1',
        },
    ),
    'charnock': DataVarDef(
        dtype=DataType(name='float32', precision=5, dtype_encoded='uint16', offset=-0.00001, fillvalue=0),
        attrs={
            'long_name': 'charnock',
            'units': '1',
        },
    ),

    # --- Cloud cover ---

    'total_cloud_cover': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'total cloud cover',
            'units': '1',
            'standard_name': 'cloud_area_fraction',
        },
    ),
    'low_cloud_cover': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'low cloud cover',
            'units': '1',
            'standard_name': 'low_type_cloud_area_fraction',
        },
    ),
    'medium_cloud_cover': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'medium cloud cover',
            'units': '1',
            'standard_name': 'medium_type_cloud_area_fraction',
        },
    ),
    'high_cloud_cover': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'high cloud cover',
            'units': '1',
            'standard_name': 'high_type_cloud_area_fraction',
        },
    ),
    'cloud_cover': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'fraction of cloud cover',
            'units': '1',
            'standard_name': 'cloud_area_fraction_in_atmosphere_layer',
        },
    ),

    # --- Column-integrated ---

    'total_column_water': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'total column water',
            'units': 'kg m-2',
            'standard_name': 'lwe_thickness_of_atmosphere_mass_content_of_water',
        },
    ),
    'total_column_liquid_water': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-0.01, fillvalue=0),
        attrs={
            'long_name': 'total column cloud liquid water',
            'units': 'kg m-2',
            'standard_name': 'atmosphere_mass_content_of_cloud_liquid_water',
        },
    ),
    'total_column_ice_water': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-0.01, fillvalue=0),
        attrs={
            'long_name': 'total column cloud ice water',
            'units': 'kg m-2',
            'standard_name': 'atmosphere_mass_content_of_cloud_ice',
        },
    ),
    'total_column_rain_water': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-0.01, fillvalue=0),
        attrs={
            'long_name': 'total column rain water',
            'units': 'kg m-2',
            'standard_name': 'atmosphere_mass_content_of_rain_water',
        },
    ),
    'total_column_snow_water': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-0.01, fillvalue=0),
        attrs={
            'long_name': 'total column snow water',
            'units': 'kg m-2',
            'standard_name': 'atmosphere_mass_content_of_snow_water',
        },
    ),
    'total_column_ozone': DataVarDef(
        dtype=DataType(name='float32', precision=4, dtype_encoded='uint16', offset=-0.0001, fillvalue=0),
        attrs={
            'long_name': 'total column ozone',
            'units': 'kg m-2',
            'standard_name': 'equivalent_thickness_of_atmosphere_ozone_content',
        },
    ),

    # --- Dynamics (pressure level) ---

    'divergence': DataVarDef(
        dtype=DataType(name='float32', precision=5, dtype_encoded='uint16', offset=-0.300001, fillvalue=0),
        attrs={
            'long_name': 'divergence of wind',
            'units': 's-1',
            'standard_name': 'divergence_of_wind',
        },
    ),
    'potential_vorticity': DataVarDef(
        dtype=DataType(name='float32', precision=7, dtype_encoded='uint32', offset=-0.0200001, fillvalue=0),
        attrs={
            'long_name': 'potential vorticity',
            'units': 'K m2 kg-1 s-1',
            'standard_name': 'ertel_potential_vorticity',
        },
    ),
    'ozone_mixing_ratio': DataVarDef(
        dtype=DataType(name='float32', precision=8, dtype_encoded='uint16', offset=-0.00000001, fillvalue=0),
        attrs={
            'long_name': 'ozone mass mixing ratio',
            'units': 'kg kg-1',
            'standard_name': 'mass_fraction_of_ozone_in_air',
        },
    ),
    'cloud_liquid_water_content': DataVarDef(
        dtype=DataType(name='float32', precision=6, dtype_encoded='uint16', offset=-0.000001, fillvalue=0),
        attrs={
            'long_name': 'specific cloud liquid water content',
            'units': 'kg kg-1',
            'standard_name': 'mass_fraction_of_cloud_liquid_water_in_air',
        },
    ),
    'cloud_ice_water_content': DataVarDef(
        dtype=DataType(name='float32', precision=6, dtype_encoded='uint16', offset=-0.000001, fillvalue=0),
        attrs={
            'long_name': 'specific cloud ice water content',
            'units': 'kg kg-1',
            'standard_name': 'mass_fraction_of_cloud_ice_in_air',
        },
    ),
    'rain_water_content': DataVarDef(
        dtype=DataType(name='float32', precision=6, dtype_encoded='uint16', offset=-0.000001, fillvalue=0),
        attrs={
            'long_name': 'specific rain water content',
            'units': 'kg kg-1',
            'standard_name': 'mass_fraction_of_rain_water_in_air',
        },
    ),
    'snow_water_content': DataVarDef(
        dtype=DataType(name='float32', precision=6, dtype_encoded='uint16', offset=-0.000001, fillvalue=0),
        attrs={
            'long_name': 'specific snow water content',
            'units': 'kg kg-1',
            'standard_name': 'mass_fraction_of_snow_water_in_air',
        },
    ),

    # --- Boundary layer / Fluxes ---

    'boundary_layer_height': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'boundary layer height',
            'units': 'm',
            'standard_name': 'atmosphere_boundary_layer_thickness',
        },
    ),
    'surface_stress_east': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-10.001, fillvalue=0),
        attrs={
            'long_name': 'instantaneous eastward turbulent surface stress',
            'units': 'N m-2',
            'standard_name': 'surface_downward_eastward_stress',
        },
    ),
    'surface_stress_north': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-10.001, fillvalue=0),
        attrs={
            'long_name': 'instantaneous northward turbulent surface stress',
            'units': 'N m-2',
            'standard_name': 'surface_downward_northward_stress',
        },
    ),

    # --- Albedo sub-types ---

    'uv_albedo_direct': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'UV visible albedo for direct radiation',
            'units': '1',
        },
    ),
    'uv_albedo_diffuse': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'UV visible albedo for diffuse radiation',
            'units': '1',
        },
    ),
    'nir_albedo_direct': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'near IR albedo for direct radiation',
            'units': '1',
        },
    ),
    'nir_albedo_diffuse': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'near IR albedo for diffuse radiation',
            'units': '1',
        },
    ),

    # --- Vegetation ---

    'leaf_area_index_low': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-0.01, fillvalue=0),
        attrs={
            'long_name': 'leaf area index, low vegetation',
            'units': 'm2 m-2',
            'standard_name': 'leaf_area_index',
        },
    ),
    'leaf_area_index_high': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-0.01, fillvalue=0),
        attrs={
            'long_name': 'leaf area index, high vegetation',
            'units': 'm2 m-2',
            'standard_name': 'leaf_area_index',
        },
    ),
    'low_vegetation_cover': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'low vegetation cover',
            'units': '1',
            'standard_name': 'vegetation_area_fraction',
        },
    ),
    'high_vegetation_cover': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'high vegetation cover',
            'units': '1',
            'standard_name': 'vegetation_area_fraction',
        },
    ),
    'low_vegetation_type': DataVarDef(
        dtype=DataType(name='uint8'),
        attrs={
            'long_name': 'type of low vegetation',
            'units': '1',
        },
    ),
    'high_vegetation_type': DataVarDef(
        dtype=DataType(name='uint8'),
        attrs={
            'long_name': 'type of high vegetation',
            'units': '1',
        },
    ),

    # --- Lake ---

    'lake_cover': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'lake cover',
            'units': '1',
        },
    ),
    'lake_depth': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'lake depth',
            'units': 'm',
        },
    ),
    'lake_bottom_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'lake bottom temperature',
            'units': 'K',
        },
    ),
    'lake_total_layer_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'lake total layer temperature',
            'units': 'K',
        },
    ),
    'lake_shape_factor': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'lake shape factor',
            'units': '1',
        },
    ),
    'lake_ice_temperature': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-61, fillvalue=0),
        attrs={
            'long_name': 'lake ice temperature',
            'units': 'K',
        },
    ),
    'lake_ice_depth': DataVarDef(
        dtype=DataType(name='float32', precision=2, dtype_encoded='uint16', offset=-0.01, fillvalue=0),
        attrs={
            'long_name': 'lake ice depth',
            'units': 'm',
        },
    ),

    # --- Orography (invariant) ---

    'soil_type': DataVarDef(
        dtype=DataType(name='uint8'),
        attrs={
            'long_name': 'soil type',
            'units': '1',
            'standard_name': 'soil_type',
        },
    ),
    'std_dev_orography': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'standard deviation of orography',
            'units': '1',
        },
    ),
    'std_dev_filtered_orography': DataVarDef(
        dtype=DataType(name='float32', precision=1, dtype_encoded='uint16', offset=-1, fillvalue=0),
        attrs={
            'long_name': 'standard deviation of filtered subgrid orography',
            'units': 'm',
        },
    ),
    'orography_anisotropy': DataVarDef(
        dtype=DataType(name='float32', precision=3, dtype_encoded='uint16', offset=-0.001, fillvalue=0),
        attrs={
            'long_name': 'anisotropy of sub-gridscale orography',
            'units': '1',
        },
    ),
    'orography_angle': DataVarDef(
        dtype=DataType(name='float32', precision=4, dtype_encoded='uint16', offset=-0.0001, fillvalue=0),
        attrs={
            'long_name': 'angle of sub-gridscale orography',
            'units': 'radians',
        },
    ),
    'orography_slope': DataVarDef(
        dtype=DataType(name='float32', precision=5, dtype_encoded='uint16', offset=-0.00001, fillvalue=0),
        attrs={
            'long_name': 'slope of sub-gridscale orography',
            'units': '1',
        },
    ),
}
