# Binary Search Algorithm
# Works only on sorted arrays
# Time Complexity: O(log n)

def binary_search(list:list, item:any) -> int:

  # You put index as -1 as the default value - if not found 
  index = -1 
  # the idea is u keep changing the start, mid and end index 
  start = 0
  end = len(list) - 1

  while start <= end:
    mid = (start + end) // 2
    if list[mid] == item:
      found = True
      index = mid
      break
    # If item is on the right-hand side, only change the start index. 
    elif list[mid] < item:
      start = mid + 1
    else: 
    #If item is on the left-hand side, only change the end index.   
      end = mid - 1
  

  return index

# Test the binary search function
mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Sorted array
x = 1                                        # Value to search for

# Perform the search
result = binary_search(mylist, x)

# Display the result
if result != -1:
  print("Found at index", result)
else:
  print("Not found")