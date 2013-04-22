# bubblesort

def bubble_sort(array):
    passes = len(array) - 1
    swapped = True
    while swapped:
        swapped = False
        i = 1
        while i <= passes:
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                swapped = True
            i = i + 1
        passes = passes - 1
    return array

# main
A = [4, 5, 2, 1, 3]
print(bubble_sort(A))
