from array import *

# This code imports everything from the array module.
# You can now use array functionalities directly, such as creating arrays, appending elements, etc.
# Example usage:
# Create an array of integers
arr = array('i', [1, 2, 3, 4, 5])
# Append an element to the array
arr.append(6)
print(f"Array after appending: {arr}")
for i in range(len(arr)):
    print(f"Element at index {i}: {arr[i]}")

arr.insert(2, 10)  # Insert 10 at index 2
print(f"Array after insertion: {arr}")
# insert list to array
arr.extend([7, 8, 9])
print(f"Array after extending: {arr}")

#  Remove an element from the array
arr.remove(3)
