# Bubble Sort Algorithm
# Sorts array by repeatedly swapping adjacent elements if they are in wrong order
# Time Complexity: O(n²) - Worst and Average case
# Space Complexity: O(1) - In-place sorting

# Test array with unsorted numbers
mylist = [1064, 34, 25, 12, 22, 11, 90, 955]

# Get the length of the array
length = len(mylist)
#swapped = True
while length > 0: #and swapped == True:
   # swapped = False
    # reduce the number of comparasions by 1 every iteration  
    length = length - 1
    # compare and swap 
    for index in range(0, length):
        first_element = mylist[index]
        second_element = mylist[index + 1]
        if first_element > second_element:
            mylist[index] = second_element
            mylist[index + 1] = first_element
            #swapped = True
print(mylist)