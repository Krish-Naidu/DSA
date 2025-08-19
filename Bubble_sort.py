# Bubble Sort Algorithm
# Sorts array by repeatedly swapping adjacent elements if they are in wrong order
# Time Complexity: O(n²) - Worst and Average case
# Space Complexity: O(1) - In-place sorting

# Test array with unsorted numbers
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

# Get the length of the array
n = len(mylist)

# Outer loop: controls number of passes
# We need (n-1) passes to sort n elements
for i in range(n-1):
  
  # Inner loop: compares adjacent elements
  # After each pass, the largest element "bubbles up" to the end
  # So we reduce the range by i (already sorted elements)
  for j in range(n-i-1):
    
    # Compare adjacent elements
    if mylist[j] > mylist[j+1]:
      # Swap elements if they are in wrong order
      # Python swap: left side gets right side values
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

# Print the sorted array
print("Sorted array:", mylist)