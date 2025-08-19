# Binary Search Algorithm
# Works only on sorted arrays
# Time Complexity: O(log n)

def binarySearch(arr, targetVal):
  # Set initial boundaries
  left = 0                    # Start of search range
  right = len(arr) - 1        # End of search range

  # Continue searching while there are elements to check
  while left <= right:
    # Find middle point (avoid overflow)
    mid = (left + right) // 2

    print("midpoint is: " + str(arr[mid]))
    # Target found at middle position
    if arr[mid] == targetVal:
      return mid

 
    # Target is in right half
    if arr[mid] < targetVal:
      left = mid + 1          # Move left boundary
    else:
      # Target is in left half
      right = mid - 1         # Move right boundary

  # Target not found in array
  return -1

# Test the binary search function
mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Sorted array
x = 88                                        # Value to search for

# Perform the search
result = binarySearch(mylist, x)

# Display the result
if result != -1:
  print("Found at index", result)
else:
  print("Not found")