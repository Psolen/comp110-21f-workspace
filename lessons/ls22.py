"""Diagram 1"""
square_to_root: dict[int, int] = {}

i: int = 1
while i < 5:
    square_to_root[i ** 2] = i
    i += 1

print(square_to_root)


"""Diagram 2"""
a: dict[str, int] = {"k" : 1}
b: dict[str, int] = a
c: dict[str, int] = b
a["k"] = 2
b = {"k" : 3}
print(a["k"])
print(b["k"])
print(c["k"])


"""Diagram 3"""
row_data: list[dict[str, str]] = [
{"name": "UNC", "city": "Chapel Hill"},
{"name": "Duke", "city": "Durham"}
]

col_data: dict[str, list[str]] = {
    "name": ["UNC", "Duke"],
    "city": ["Chapel Hill", "Durham"]
}


"""Diagram 4"""
def invert(kvs: dict[str, int]) -> dict[int, str]:
    result: dict[int, str] = {}
    for key in kvs:
        result[kvs[key]] = key 
    return result

counts: dict[str, int] = {"a": 1, "b": 2, "c": 1}
print(len(counts))

freqs: dict[int, str] = invert(counts)
print(freqs[1])
print(len(freqs))