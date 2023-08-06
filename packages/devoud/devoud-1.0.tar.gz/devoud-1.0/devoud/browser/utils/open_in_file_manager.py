from pathlib import Path
from subprocess import Popen
from sys import platform


def open_in_file_manager(path):
    path = Path(path)
    """Открывает путь через системный файловый менеджер"""
    command = {'win32': ["explorer", path],
               'darwin': ["open", path],
               'linux': ["xdg-open", path]}
    Popen(command.get(platform, ["xdg-open", path]))
