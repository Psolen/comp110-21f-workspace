"""Examples of importing in Python."""


# Import a module.
from lessons import helpers


# Alias a module / imported name as another name.
from lessons import helpers as hp


# Import only a function.
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(hp.powerful(1, 3))
    print(f"The answer: {helpers.THE_ANSWER}")
    print(powerful(2, 4))
    print(THE_ANSWER)


if __name__ == "__main__":
    main()