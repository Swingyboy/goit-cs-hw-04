# File Searcher

File Searcher is a command-line tool designed to search for specific patterns in files using either threading or multiprocessing. This tool allows you to specify a directory of files, a list of search patterns, and the number of threads or processes to use for the search.
There are two implemented classes ThreadSearch and ProcessSearch. The first one uses threading and the second one uses multiprocessing. Both classes have the same interface and can be used interchangeably.
Interface of the classes:
 - **init**(self, patterns: List[str], files: List[pathlib.PosixPath], max_workers: int = 1)
    - patterns: List of patterns to search for.
    - files: List of files to search in.
    - max_workers: Number of threads or processes to use for the search.
 - **run**(self) -> Dict[str, List[str]]

## Features

- Search for multiple patterns in files within a specified directory.
- Choose between threading and multiprocessing for parallel search.
- Measure and display the time taken for searches using both methods.
- Output the search results for each pattern.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
    ```sh
    git https://github.com/Swingyboy/goit-cs-hw-04.git
    cd goit-cs-hw-04
    ```

## Usage

```sh
python main.py -f <file-path> -p <patterns> [-n <num-threads>]
```


## Output
   The time of the search and the results for each pattern are displayed in the console.