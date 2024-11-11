import sys

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Parse command line arguments
try:
    array = list(map(int, sys.argv[1:-1]))
    target = int(sys.argv[-1])
    result = binary_search(sorted(array), target)
    print(f"Index of {target}:", result if result != -1 else "Not found")
except ValueError:
    print("Please provide integers only.")
