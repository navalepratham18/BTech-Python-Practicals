# Function to perform binary search
def binary_search(words, target):
    low = 0
    high = len(words) - 1

    while low <= high:
        mid = (low + high) // 2
        if words[mid] == target:
            return mid  
        elif words[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1  
    return -1  

words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

words.sort()

print("Sorted List of Words:", words)

target = input("Enter a word to search for: ")

result = binary_search(words, target)

if result != -1:
    print(f"Word '{target}' found at index {result}")
else:
    print(f"Word '{target}' not found.")
