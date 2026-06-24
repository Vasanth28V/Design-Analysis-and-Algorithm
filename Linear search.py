# Linear Search in an array of 7 elements

# Step 1: Create an array with 7 elements
arr = [12, 45, 7, 23, 56, 89, 34]

# Step 2: Take target element from user
target = int(input("Enter the element to search: "))

# Step 3: Linear Search
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element found at index {i}")
        found = True
        break

# Step 4: If not found
if not found:
    print("Element not found in the array")