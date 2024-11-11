set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
print("Union:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

difference_set = set1.difference(set2)
print("Difference:", difference_set)

symmetric_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_diff_set)

set1.add(6)
print("After Add:", set1)

set1.remove(6)
print("After Remove:", set1)

set1.pop()
print("After Pop:", set1)

set1.clear()
print("After Clear:", set1)
