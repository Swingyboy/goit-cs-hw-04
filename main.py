import argparse
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

    results = {}
    searcher = ProcessSearcher(files, args.patterns, results, args.num_threads)
    searcher.run()
    for results in results.items():
        print(f"Pattern: {results[0]}")
        for file in results[1]:
            print(f"File: {file}")



if __name__ == "__main__":
    main()
