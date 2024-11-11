sample_list = [10, 20, 30, 40, 50]

sample_list.append(60)
print("After Append:", sample_list)

sample_list.insert(2, 25)
print("After Insert:", sample_list)

sample_list.remove(40)
print("After Remove:", sample_list)

sample_list.pop()
print("After Pop:", sample_list)

index = sample_list.index(30)
print("Index of 30:", index)

count = sample_list.count(10)
print("Count of 10:", count)

sample_list.sort()
print("After Sort:", sample_list)

sample_list.reverse()
print("After Reverse:", sample_list)

sample_list.clear()
print("After Clear:", sample_list)
