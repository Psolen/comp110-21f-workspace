"""Demonstrating dictionaries capabilities."""

# Data Type = dict[key type, value type].
# Creation = name: Data Type = dict().
# Mutation = name[key type] = value type.


# Declaring and initializing the type of a dictionary.
schools: dict[str, int] = dict()


# Set a key value pairing in the dictionary.
schools["UNC"] = 19400
schools["Duke"] = 6700
schools["NCSU"] = 26150

# Print a dictionary literal.
print(schools)


# Access a value by its key. lookup a key.
print(schools["UNC"])


# Remove a key-value pair from a dictionary by its key.
schools.pop("Duke")


# Test for the existance of a key.
is_duke_present: bool = "Duke" in schools
print(is_duke_present)
print(schools)


# Update/Reassign a key-value pair.
schools["UNC"] = 2000
schools["NCSU"] += 200

print(schools)


# Demonstration of dictionary literals.


# Empty dictionary literal.
schools = {} # Same as dict()
print(schools)


# Alternatively print key-value pairs.
schools = {
    "UNC": 19400, 
    "Duke": 6717, 
    "NCSU": 26150
}

print(schools)


# print(schools["UNCC"])


# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")