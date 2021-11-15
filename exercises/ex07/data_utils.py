"""Utility functions."""

__author__ = "730247598"

from csv import DictReader

# Define your functions below
DATA_DIRECTORY = "../../data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:

    """Read the rows of a csv file."""
    result: list[dict[str, str]] = []
    
    """Open a handle to the data file."""
    file_handle = open(filename, "r", encoding="utf8")

    """Prepare to read the data in the file as CSV instead of just strings."""
    csv_reader = DictReader(file_handle)

    """Read each row of the CSV line by line."""
    for row in csv_reader:
        result.append(row)

    """Close file."""
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of str of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(data_col_main: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for row_one in data_col_main:
        emp_list: list[str] = []
        i: int = 0
        while i < N:
            emp_list.append(row_one)
            i += 1
        result[row_one] = emp_list
    return result