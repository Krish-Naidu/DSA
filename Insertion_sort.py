# Insertion Sort Algorithm
# Builds the final sorted array one item at a time
# Works like sorting playing cards in your hand
# Time Complexity: O(n²) - Worst case, O(n) - Best case (already sorted)
# Space Complexity: O(1) - In-place sorting

# Test array with unsorted numbers
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

# Get the length of the array
n = len(mylist)

# Start from second element (index 1) since first element is considered sorted
for i in range(1, n):
  # Remember where to insert the current element
  insert_index = i
  
  # Remove current element from list to find its correct position
  current_value = mylist.pop(i)
  
  # Look backwards through the sorted portion (left side)
  # Start from position before current, go to beginning
  for j in range(i-1, -1, -1):
    
    # If element in sorted portion is larger than current value
    if mylist[j] > current_value:
      # This is where we should insert (keep looking left)
      insert_index = j
    # If we find smaller element, we can stop looking
  
  # Insert the current value at its correct position
  mylist.insert(insert_index, current_value)

# Print the sorted array
print("Sorted array:", mylist)