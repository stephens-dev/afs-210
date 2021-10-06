import time
import random

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionStart(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        

def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

def partition_last(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
    
def quicksort_last(arr, low, high):
     if len(arr) == 1:
        return arr
     if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quicksort_last(arr, low, pi-1)
        quicksort_last(arr, pi+1, high)
  

def partition_middle(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


    # Create a helper function that will be called recursively
def quicksort_middle(items, low, high):
    if low < high:
        # This is the index after the pivot, where our lists are split
        split_index = partition_middle(items, low, high)
        quicksort_middle(items, low, split_index)
        quicksort_middle(items, split_index + 1, high)

def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end
    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            
            break

    # Swap the values
    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high

def partition_random(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quicksort_random(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quicksort_random(array, start, p-1)
    quicksort_random(array, p+1, end)

print("Quick Sort:")
myList = [54,26,93,17,77,31]
myList1 = [54,26,93,17,77,31]
myList2 = [54,26,93,17,77,31]
myList3 = [54,26,93,17,77,31]


# myList = [x for x in range(1000)]
# random.shuffle(myList)

#print(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
#print()
#print("Sorted Listed: ")
print(myList)   
print(f"The execution time is: {end_time-start_time}")

start_time = time.time()
quicksort_last(myList1,0,len(myList1)-1)
end_time = time.time()
print(myList1)   
print(f"The execution time is: {end_time-start_time}")

start_time = time.time()
quicksort_middle(myList2,0,len(myList2)-1)
end_time = time.time()
print(myList2)   
print(f"The execution time is: {end_time-start_time}")

start_time = time.time()
quicksort_random(myList3,0,len(myList3)-1)
end_time = time.time()
print(myList3)   
print(f"The execution time is: {end_time-start_time}")

# start_time = time.time()
# quicksort_median(myList2,0,len(myList2)-1)
# end_time = time.time()
# print(myList2)   
# print(f"The execution time is: {end_time-start_time}")

# firstcomparison = 0
# lastcomparison = 0
# mediancomparison = 0

#A method for partition around the first element of the array
# def partition_first(array, leftend, rightend):
    # pivot = array[leftend]
    # i = leftend + 1
    # for j in range(leftend + 1, rightend):
    #     if array[j] < pivot:
    #         temp = array[j]
    #         array[j] = array[i]
    #         array[i] = temp
    #         i += 1

    # leftendval = array[leftend]
    # array[leftend] = array[i-1]
    # array[i-1] = leftendval
    # return i - 1 

#A method for partitioning around the last element of the array
# def partition_last(array, leftend, rightend):
    
#     pivot = array[rightend-1]

#     array[rightend-1] = array[leftend]
#     array[leftend] = pivot
    
#     i = leftend + 1
#     for j in range(leftend + 1, rightend):
#         if array[j] < pivot:
#             temp = array[j]
#             array[j] = array[i]
#             array[i] = temp
#             i += 1

#     leftendval = array[leftend]
#     array[leftend] = array[i-1]
#     array[i-1] = leftendval
#     return i - 1 

# #A method to calculate the median of three numbers using two comparisons
# def median(a, b, c):
#     if ( a - b) * (c - a) >= 0:
#         return a

#     elif (b - a) * (c - b) >= 0:
#         return b

#     else:
#         return c

# #A method to partition around the median
# def partition_median(array, leftend, rightend):
#     left = array[leftend]
#     right = array[rightend-1]
#     length = rightend - leftend
#     if length % 2 == 0:
#         middle = array[leftend + length//2 - 1]
#     else:
#         middle = array[leftend + length//2]
  
    

#     pivot = median(left, right, middle)

#     pivotindex = array.index(pivot) #only works if all values in array unique

#     array[pivotindex] = array[leftend]
#     array[leftend] = pivot

#     i = leftend + 1
#     for j in range(leftend + 1, rightend):
#         if array[j] < pivot:
#             temp = array[j]
#             array[j] = array[i]
#             array[i] = temp
#             i += 1

#     leftendval = array[leftend]
#     array[leftend] = array[i-1]
#     array[i-1] = leftendval
#     return i - 1 

    
# #Implement quicksort while partitioning around the first index
# def quick_sort1(array, leftindex, rightindex):
#     global firstcomparison
#     if leftindex < rightindex:
        
#         newpivotindex = partition_first(array, leftindex, rightindex)
        
#         firstcomparison += (rightindex - leftindex - 1)
        
#         quick_sort1(array, leftindex, newpivotindex) 
        
#         quick_sort1(array, newpivotindex + 1, rightindex)
        
# def quicksort_last(array, leftindex, rightindex):
#     global lastcomparison
#     if leftindex < rightindex:

#         newpivotindex = partition_last(array, leftindex, rightindex)

#         lastcomparison += (rightindex - leftindex - 1)

#         quicksort_last(array, leftindex, newpivotindex)
#         quicksort_last(array, newpivotindex + 1, rightindex)

 
# def quicksort_median(array, leftindex, rightindex):
#      global mediancomparison
#      if leftindex < rightindex:

#          newpivotindex = partition_median(array, leftindex, rightindex)

#          mediancomparison += (rightindex - leftindex - 1)
#          quicksort_median(array, leftindex, newpivotindex)
         

#          quicksort_median(array, newpivotindex + 1, rightindex)


# test3 = [1, 11, 5, 15, 2, 12, 9, 99, 77, 0]
# test4 = []
# for i in range(1, 101):
#     test4.append(i)

# f = open("IntegerArray.txt", "r")
# intarray = []
# for line in f:
#     intarray.append(int(line))
# f.close()

# myList = [x for x in range(1000)]
# random.shuffle(myList)
# start_time = time.time()
# quick_sort(myList,0,len(myList)-1)
# end_time = time.time()
# #print()
# #print("Sorted Listed: ")
# #print(myList)   
# print(f"The execution time is: {end_time-start_time}")

#test on an array of length 10000
# mediancomparison = 0
# quicksort_median(test3, 0, len(test3))
# print(test3)
# print(mediancomparison)
# quick_sort(myList,0,len(myList)-1)
