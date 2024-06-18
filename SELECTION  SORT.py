# PRACTICAL 5 DAA 
 # selection sort 
def selection_sort(array):
    array = list(array)   # convert tupie into list 
    size = len(array)
    for ind in  range(size):
        min_index = ind
        for j in range(ind + 1 , size):
            if array[j] <array[min_index]:
                min_index = j
        array[ind] , array[min_index] = array[min_index] , array[ind]
    return tuple(array)      # Convet back to typle before returing

arr = (-2 , 45 ,0 ,0, 11, -9 , 88 , -97, -202, 747)
sorted_arr = selection_sort(arr)
print(sorted_arr)