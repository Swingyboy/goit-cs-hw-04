from typing import Dict, List
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Manager
import logging
from file_manager import search_in_file
import pathlib


class ProcessFileSearcher:
    def __init__(self, files: List[pathlib.PosixPath], search: str, res: List[str], max_workers: int = 1):
        self.files = files
        self.search = search
        self.res = res
        self.max_workers = max_workers

    def run(self):
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for file in self.files:
                futures.append(executor.submit(search_in_file, file, self.search, self.res))

            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.error(f"Error occurred while searching in file: {e}")


class ProcessSearcher:
    def __init__(self, files: List[pathlib.PosixPath], search: List[str], res: Dict[str, List[str]], max_workers: int = 1):
        self.files = files
        self.search = search
        self.res = res
        self.max_workers = max_workers

    def run(self):
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for pattern in self.search:
                self.res[pattern] = Manager().list()
                searcher = ProcessFileSearcher(self.files, pattern, self.res[pattern], self.max_workers)
                futures.append(executor.submit(searcher.run))

            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.error(f"Error occurred while searching for pattern '{pattern}': {e}")
