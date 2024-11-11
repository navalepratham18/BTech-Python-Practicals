sample_dict = {"a": 1, "b": 2, "c": 3}

sample_dict["d"] = 4
print("After Adding:", sample_dict)

sample_dict.pop("b")
print("After Removing 'b':", sample_dict)

value = sample_dict.get("c")
print("Get value for 'c':", value)

keys = sample_dict.keys()
print("Keys:", keys)

values = sample_dict.values()
print("Values:", values)

items = sample_dict.items()
print("Items:", items)

sample_dict.clear()
print("After Clear:", sample_dict)
