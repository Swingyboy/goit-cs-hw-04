import pathlib
import threading
from typing import Dict, List
from concurrent.futures import ThreadPoolExecutor


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


class FileSearcher(threading.Thread):
    def __init__(self, files: List[pathlib.PosixPath], search: str, res: List[str], max_workers: int = 1):
        super().__init__()
        self.files = files
        self.search = search
        self.res = res
        self.max_workers = max_workers

    def run(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for file in self.files:
                executor.submit(search_in_file, file, self.search, self.res)


class ThreadSearcher(threading.Thread):
    def __init__(self, files: List[pathlib.PosixPath], search: List[str], res: Dict[str, List[str]], max_workers: int = 1):
        super().__init__()
        self.files = files
        self.search = search
        self.res = res
        self.max_workers = max_workers

    def run(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for pattern in self.search:
                self.res[pattern] = []
                searcher = FileSearcher(self.files, pattern, self.res[pattern], self.max_workers)
                executor.submit(searcher.run)

