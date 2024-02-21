from typing import Literal

import pandas as pd

import data.gamelogs as data

PHASES = "ODK"
EXPECTED_POINTS = "xP"
SERIES = "SERIES"


def get_games_map() -> dict:
    return data.get_gamelog_path_map()


def calculate_cumulative_xp(data: pd.DataFrame, phase: Literal["O", "D"] = "O") -> pd.Series:
    """
    Perform cumulative sum transformation on the expected points (xp) column of a DataFrame,
    considering only data for a specific phase (either "O" for Offensive or "D" for Defensive).

    Parameters:
    - data (pd.DataFrame): DataFrame containing the data.
    - phase (Literal["O", "D"], optional): Phase to consider, either "O" for Offensive or "D" for Defensive.
      Defaults to "O".

    Returns:
    - pd.Series: Series representing the cumulative sum of expected points for the specified phase,
      padded with forward-filled values and filled NaNs with 0.

    Notes:
    - This function assumes the presence of constants 'PHASES', 'SERIES', and 'EXPECTED_POINTS' in the namespace.
      These constants are used as column names for phase indicator, series identifier, and expected points, respectively.
    """
        
    xp_by_phase = data[data[PHASES] == phase].copy()

    indices_of_max_values = xp_by_phase.groupby(SERIES)[EXPECTED_POINTS].idxmax()

    id_mask = pd.Series(index=data.index, data=data.index.isin(indices_of_max_values))

    return xp_by_phase[id_mask][EXPECTED_POINTS].reindex(data.index).cumsum().ffill().fillna(0)

def unified_view_yard_ln(value: int) -> int:
    if value < 0:
            return (50 + value) + 50
    else:
        return value
    
import numpy as np
from scipy.interpolate import interp1d

# Define the function that will calculate the expected point value
def expected_point_value(current_position):
    
    positions = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85, 95])
    point_values = np.array([6.041, 4.572, 3.681, 3.167, 2.392, 1.538, 0.923, 0.236, -0.637, -1.245])

    interpolation_function = interp1d(positions, point_values, kind='linear', fill_value='extrapolate')

    return interpolation_function(current_position)