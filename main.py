import argparse
import timeit
from file_manager import get_files
from threading_search import ThreadSearcher
from process_search import ProcessSearcher


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def main():
    parser = argparse.ArgumentParser(description="Search some files")
    parser.add_argument("-f", "--file-path", required=True)
    parser.add_argument("-p", "--patterns", nargs="*", required=True)
    parser.add_argument("-w", "--workers", type=int, default=5)
    args = parser.parse_args()

    files = get_files(args.file_path)

    for Searcher in [ThreadSearcher, ProcessSearcher]:
        try:
            searcher = Searcher(files, args.patterns, {}, args.workers)
            time_taken = timeit.timeit(lambda: searcher.run(), number=5)
        except Exception as e:
            print(RED + f"Error occurred while running {Searcher.__name__}: {e}" + RESET)
            continue
        results = searcher.res
        print("-" * 50)
        print(GREEN + f"Time taken for {Searcher.__name__}: {time_taken}" + RESET)
        print("-" * 50)
        print(GREEN + f"Results for {Searcher.__name__}:" + RESET)
        for pattern, res in results.items():
            print(YELLOW + f"Pattern: {pattern}" + RESET)
            for file in res:
                print(f"\t{file}")
        print("-" * 50)


if __name__ == "__main__":
    main()
