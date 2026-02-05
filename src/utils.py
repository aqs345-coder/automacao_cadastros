import time
from pathlib import Path

import pyautogui

ROOT_DIR = Path(__file__).parent
TABLE_PATH = ROOT_DIR / "produtos.csv"
LINK = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"


def get_coordinates():
    time.sleep(3)
    coordinates = pyautogui.position()

    return coordinates

