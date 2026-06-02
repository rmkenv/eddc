"""
EDDC — Energy Degree Day Calculator

A Python library for calculating Heating Degree Days (HDD) and Cooling Degree Days (CDD)
using multiple weather data sources:

    - U.S. National Weather Service (NWS) API
    - Open-Meteo historical weather API (no API key required)

Also includes:
    * Coordinate validation and temperature conversion utilities
    * CSV utilities for reading and aligning energy consumption data
    * Unified multi-source API
    * Linear regression analysis between degree days and energy consumption
    * Visualization support for regression results
"""

# NWS data source
from .calculator import (
    get_degree_days_for_location,
    get_degree_days_for_period,
    DegreeDaysResult,
)

# Open-Meteo data source
from .meteostat_api import fetch_meteostat_data

# Unified multi-source access
from .data_sources import get_degree_days

# Regression analysis
from .regression import perform_regression

# Visualization
from .visualization import plot_regression

# CSV utilities
from .csv_utils import (
    read_energy_data_from_csv,
    read_energy_data_with_dates,
    align_energy_with_degree_days,
)

# Utilities
from .utils import (
    validate_coordinates,
    calculate_degree_days,
    fahrenheit_to_celsius,
    celsius_to_fahrenheit,
    mean_temperature,
)

# Exceptions
from .exceptions import (
    NWSAPIError,
    InvalidCoordinatesError,
)

__version__ = "0.1.5"

__all__ = [
    "get_degree_days_for_location",
    "get_degree_days_for_period",
    "fetch_meteostat_data",
    "get_degree_days",
    "perform_regression",
    "plot_regression",
    "read_energy_data_from_csv",
    "read_energy_data_with_dates",
    "align_energy_with_degree_days",
    "DegreeDaysResult",
    "validate_coordinates",
    "calculate_degree_days",
    "fahrenheit_to_celsius",
    "celsius_to_fahrenheit",
    "mean_temperature",
    "NWSAPIError",
    "InvalidCoordinatesError",
]
