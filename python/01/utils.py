import os
import platform

from time import sleep


def clear_terminal(sleep_seconds=None) -> None:
    system = platform.system().lower()

    if sleep_seconds:
        sleep(sleep_seconds)

    if (system == "windows"):
        os.system("cls")
    else:
        os.system("clear")
