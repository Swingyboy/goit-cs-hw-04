import pathlib
from typing import Dict, List
from concurrent.futures import ProcessPoolExecutor


def check_path(path):
    path = pathlib.Path(path)
    if path.exists():
        return True
    return False


def get_files(path):
    path = pathlib.Path(path)
    if check_path(path):
        return [f for f in path.iterdir() if f.is_file()]
    return None


def search_in_file(file: pathlib.PosixPath, search: str, res: list) -> bool:
    with open(file, 'r') as f:
        for line in f:
            if search in line:
                res.append(str(file))
                return True
    return False









