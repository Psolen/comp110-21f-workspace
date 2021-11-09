"""Example of writing a function to process a list."""

# Define a function named contains, two parameters (needle: (str), haystack: (list)), returns true if needle is found in haystack.
# Move through each item in list until needle is found, as soon as needle is found return true, if all items have been checked the return false.

def main() -> None:
    """Entrypoint of program."""
    names: list[str] = ["Kris", "Phil"]
    print(contains("Phil", names))

def contains(needle: str, haystack: list[str]) -> bool:
    """Return true is needle is found in haystack, otherwise return false."""
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1
    return False

if __name__ == "__main__":
    main()