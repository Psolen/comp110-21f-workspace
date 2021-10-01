"""List diagram examples."""

a: list[str] = ["one"]
b: list[str] = a
a.append("two")

print(b[1])

"""Lists and functions."""

def dup(xs: list[int]) -> None:
    """Duplicate a lists values."""
    start_len: int = len(xs)
    i: int = 0
    while i < start_len:
        xs.append(xs[i])
        i += 1

nums: list[int] = [10, 20]
dup(nums)
print(nums)

"""Example producing a function."""

def odds(min: int, max: int) -> list[int]:
    """Construct a list of odds, inclusive."""
    xs: list[int] = list()
    i: int =(min//2) *2 + 1
    while i <= max:
        xs.append(i)
        i += 2
    return xs

ys: list[int] = odds(3, 6)
print(ys)