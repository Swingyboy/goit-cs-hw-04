import argparse
import timeit
from file_manager import get_files
from threading_search import ThreadSearcher
from process_search import ProcessSearcher


def main():
    parser = argparse.ArgumentParser(description="Search some files")
    parser.add_argument("-f", "--file-path", required=True)
    parser.add_argument("-p", "--patterns", nargs="*", required=True)
    parser.add_argument("-n", "--num-threads", type=int, default=5)
    args = parser.parse_args()

    files = get_files(args.file_path)

    for Searcher in [ThreadSearcher, ProcessSearcher]:
        searcher = Searcher(files, args.patterns, {}, args.num_threads)
        time_taken = timeit.timeit(lambda: searcher.run(), number=5)
        results = searcher.res

        print(f"Time taken for {Searcher.__name__}: {time_taken}")
        print(f"Results for {Searcher.__name__}:")
        for pattern, res in results.items():
            print(f"Pattern: {pattern}")
            for file in res:
                print(f"\t{file}")


if __name__ == "__main__":
    main()
