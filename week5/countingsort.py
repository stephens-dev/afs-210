def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                
    
    # Creates an array to count the numbers
    for a in array1:
    
        count[a] += 1             
    i = 0
    # Conrols the new array count
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1

print(counting_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))