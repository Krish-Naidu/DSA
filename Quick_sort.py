# Quick Sort Algorithm
# Divide and conquer approach - splits array around pivot
# Time Complexity: O(n log n) average, O(n²) worst case

# How it works:

# Choose a value in the array to be the pivot element.
# Order the rest of the array so that lower values than the pivot element 
# are on the left, and higher values are on the right.
# Swap the pivot element with the first element of the higher values 
# that the pivot element lands in between the lower and higher values.
# Do the same operations (recursively) for the sub-arrays on the left and
# right side of the pivot element.

def partition(array, low, high):
  # Choose last element as pivot
  pivot = array[high]
  
  # Index of smaller element (boundary of smaller elements)
  i = low - 1

  # Traverse through array elements
  for j in range(low, high):
     # If current element is smaller than or equal to pivot
     if array[j] <= pivot:
       i += 1    # Move boundary forward
       # Swap elements to move smaller element to left side
       array[i], array[j] = array[j], array[i]

  # Place pivot in its correct position
  array[i+1], array[high] = array[high], array[i+1]
  
  # Return position of pivot
  return i+1

def quicksort(array, low=0, high=None):
  # Set default high value for initial call
  if high is None:
    high = len(array) - 1

  # Base case: if low < high, there are elements to sort
  if low < high:
    # Partition array and get pivot position
    pivot_index = partition(array, low, high)
    
    # Recursively sort elements before pivot
    quicksort(array, low, pivot_index-1)
    
    # Recursively sort elements after pivot
    quicksort(array, pivot_index+1, high)

# Test array with unsorted numbers
mylist = [64, 34, 25, 5, 22, 11, 90, 12]

# Sort the array using quicksort
quicksort(mylist)

# Print the sorted result
print("Sorted array:", mylist)
