import sys
from pathlib import Path


# Funzione per la gestione delle path con pyinstaller
def _path(relativePath):
    try:
        basePath = Path(sys._MEIPASS)
    except Exception:
        basePath = Path(".").absolute()

    return str(Path.joinpath(basePath, relativePath).absolute())
