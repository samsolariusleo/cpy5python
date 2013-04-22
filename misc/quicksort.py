# quicksort

def quick_sort(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        less = []
        great = []

        for i in array[1:]:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                great.append(i)

        less = quick_sort(less)
        great = quick_sort(great)
    return less + [pivot] + great

# main
A = [4, 5, 2, 1, 3]
print(quick_sort(A))
