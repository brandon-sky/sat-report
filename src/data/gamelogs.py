import os 
import pandas as pd

PATH="data"

dtype_mapping = {
    'PLAY #': int, 
    'ODK': str, 
    'QTR': int, 
    'SERIES': int, 
    'DN': str, 
    'DIST': str, 
    'DOWN GROUP': str, 
    'YARD LN': str,
    'GN/LS': str, 
    'DOWN RESULT': str, 
    'HASH': str, 
    'PERSONNEL': str, 
    'OFF FORM': str, 
    'FORM FAM': str,
    'OFF STR': str, 
    'BACKFIELD': str, 
    'MOTION': str, 
    'SAFETY': str,
    'PLAY TYPE CALLED': str,
    'PLAY TYPE': str,
    'RESULT': str,
    'PLAY DIR': str,
    'PASS AREA': str, 
    'PASS ZONE': str, 
    'GAP': str,
    'PEN O/D': str, 
    'PENALTY': str, 
    'OFF PLAY': str, 
    'DEF FRONT': str, 
    'BLITZ': str, 
    'BLITZ DIR': str,
    'PR#': str, 
    'BLITZ YN': str, 
    'COVERAGE': str, 
    'COMMENT': str, 
    'QB PRESSURE': str, 
    'WTD': str,
    'SCORE DIFF': int, 
    'SCORE SCOUT': int, 
    'SCORE OPP': int, 
    'GAME #': int, 
    'LOCATION': str, 
    'SCOUT': str,
    'OPPONENT': str, 
    'RESULT 2': str
}

def _create_gamelog_key(file:str, gameday: int) -> str:
    away, home = file.split(".")[0].split("_")[-2:]
    gameday = str(gameday).zfill(2)
    return f"{gameday}-{away}@{home}"


def get_gamelog_path_map(path: str = PATH) -> dict:

    games = {}

    for gameday, file in enumerate(sorted(os.listdir(path)), start=1):
        file_path = os.path.join(path, file)
        
        if os.path.isfile(file_path):

            key = _create_gamelog_key(file, gameday)
            games[key] = os.path.abspath(file_path)

    return games


def get_gamelog(path: str) -> pd.DataFrame:
    return pd.read_excel(path)