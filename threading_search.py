import threading
from typing import Dict, List
from concurrent.futures import ThreadPoolExecutor, as_completed
from file_manager import search_in_file
import pathlib
import logging

logging.basicConfig(level=logging.INFO)


class FileSearcher(threading.Thread):
    def __init__(self, files: List[pathlib.PosixPath], search: str, res: List[str], max_workers: int = 1):
        super().__init__()
        self.files = files
        self.search = search
        self.res = res
        self.max_workers = max_workers

    def run(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_file = {executor.submit(search_in_file, file, self.search, self.res): file for file in self.files}
            for future in as_completed(future_to_file):
                file = future_to_file[future]
                try:
                    future.result()
                except Exception as e:
                    logging.error(f"Error searching in file {file}: {e}")


class ThreadSearcher(threading.Thread):
    def __init__(self, files: List[pathlib.PosixPath], search: List[str], res: Dict[str, List[str]],
                 max_workers: int = 1):
        super().__init__()
        self.files = files
        self.search = search
        self.res = res
        self.max_workers = max_workers

    def run(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_searcher = {}
            for pattern in self.search:
                self.res[pattern] = []
                searcher = FileSearcher(self.files, pattern, self.res[pattern], self.max_workers)
                future = executor.submit(searcher.run)
                future_to_searcher[future] = searcher

            for future in as_completed(future_to_searcher):
                searcher = future_to_searcher[future]
                try:
                    future.result()
                except Exception as e:
                    logging.error(f"Error in searcher {searcher}: {e}")
