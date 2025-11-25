
# Merge Sort Algorithm
# Recursively splits the array and merges sorted halves
def mergeSort(arr):
  # Base case: arrays with 0 or 1 element are already sorted
  if len(arr) <= 1:
    return arr

  # Find the midpoint and split the array
  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  # Recursively sort both halves
  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  # Merge the sorted halves
  return merge(sortedLeft, sortedRight)


# Merge two sorted arrays into one sorted array
def merge(left, right):
  result = []
  i = j = 0

  # Compare elements from both arrays and add the smaller one
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  # Add any remaining elements from left or right
  result.extend(left[i:])
  result.extend(right[j:])

  return result


# Example usage
mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)

