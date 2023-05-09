# Sea of Thieves Offset Finder

This script helps you find memory offsets in Sea of Thieves data files using the SDK in the form of JSON files. It supports updating, archiving, and reverting SDK files for more convenient usage.

## Dependencies

- Python 3.x
- requests library (install with `pip install requests`)

## Usage

### Basic usage

To find offsets in a data file using a local SDK JSON file:

python offset_finder.py <sdk_json_file_path> <data_file_path>

### Updating the SDK JSON file

To update the SDK JSON file from a URL and archive the current one:

python offset_finder.py <sdk_json_file_path> <data_file_path> --update <URL> --archive <archive_dir>

### Reverting to the latest archived SDK JSON file

To revert the SDK JSON file to the latest archived version:

python offset_finder.py <sdk_json_file_path> <data_file_path> --revert --archive <archive_dir>

## Command Line Arguments

- `sdk_json_file_path`: Path to the SDK JSON file.
- `data_file_path`: Path to the data file.
- `--update`: (Optional) URL to update the SDK JSON file. If specified, the script will download the JSON file from the given URL and save it to the local path specified in `sdk_json_file_path`.
- `--archive`: (Optional) Directory to store archived SDK JSON files. Must be specified when using `--update` or `--revert` options.
- `--revert`: (Optional) Revert to the latest archived SDK JSON file. If specified, the script will replace the current JSON file with the latest archived version.

## SDK JSON File Format

The SDK JSON files should contain the necessary data to identify specific elements in the game, such as class names, functions, and offsets. The JSON-SDK directory in the repository contains multiple JSON files that make up the SDK data.
