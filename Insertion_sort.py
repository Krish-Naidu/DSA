# Insertion Sort Algorithm
# Builds the final sorted array one item at a time
# Works like sorting playing cards in your hand
# Time Complexity: O(n²) - Worst case, O(n) - Best case (already sorted)
# Space Complexity: O(1) - In-place sorting

def insertionSort(array):
    # Start from second element (index 1)
    for i in range(1, len(array)):
        # Store current element as temp
        temp = array[i]
        # Start from previous element
        j = i - 1
        
        #  ------ OPTION 1 -------
        # Shift elements greater than temp one position to the right
        # while j >= 0 and array[j] > temp:
        #     array[j + 1] = array[j]
        #     j -= 1

        #  ------ OPTION 2 -------
        while j >= 0:
          if array[j] > temp:
            array[j + 1] = array[j]
            j = j - 1 
          else:
             break
          
          
        # Insert temp at correct position
        array[j + 1] = temp

# Test array with unsorted numbers
data = [64, 34, 25, 12, 22, 11, 90, 5]

# Call the insertion sort function
insertionSort(data)

# Print sorted array
print("Sorted array:", data)