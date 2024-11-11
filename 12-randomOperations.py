import random

random_int = random.randint(1, 10)

choices = ["apple", "banana", "cherry"]
random_choice = random.choice(choices)

random_float = random.random()

random_range = random.randrange(1, 10, 2)

sample_list = [1, 2, 3, 4, 5]
random.shuffle(sample_list)

random_sample = random.sample(sample_list, 3)

print("Random integer between 1 and 10:", random_int)
print("Random choice from list:", random_choice)
print("Random float between 0 and 1:", random_float)
print("Random range:", random_range)
print("Shuffled list:", sample_list)
print("Random sample of 3 elements from list:", random_sample)
