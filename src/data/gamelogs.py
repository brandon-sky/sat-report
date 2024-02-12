import os 

PATH="data"

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