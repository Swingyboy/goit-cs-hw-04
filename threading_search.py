import argparse
from file_manager import get_files, ThreadSearcher


def main():
    parser = argparse.ArgumentParser(description="Search some files")
    parser.add_argument("-f", "--file-path", required=True)
    parser.add_argument("-p", "--patterns", nargs="*", required=True)
    parser.add_argument("-n", "--num-threads", type=int, default=1)
    args = parser.parse_args()

    files = get_files(args.file_path)

    results = {}
    searcher = ThreadSearcher(files, args.patterns, results, args.num_threads)
    searcher.start()
    searcher.join()
    for results in results.items():
        print(f"Pattern: {results[0]}")
        for file in results[1]:
            print(f"File: {file}")



if __name__ == "__main__":
    main()
