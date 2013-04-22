# insertionsort

def insertion_sort(array):
    for j in range(1, len(array)): # looping through elements from second one.
        num = array[j]
        i = j - 1
        while i >= 0 and array[i] > num:
            array[i + 1] = array[i] # replacing smaller num with larger num.
            i = i - 1 # terminating case
        # when the process hits the first element in the array
        # or when the number is the smallest one as compared to what has been
        # compared...
        array[i + 1] = num
    return array

# main
A = [4, 5, 2, 1, 3]
print(insertion_sort(A))
