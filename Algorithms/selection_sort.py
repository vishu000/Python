def selection_sort(array,size):
    for step in range(size):
        minind = step

        for i in range(step +1,size):
            if array[i] < array[minind]:
              minind = i
        (array[step], array[minind]) = (array[minind], array[step])

l = [-2, 45, 0, 11, -9]
size = len(l)
print(size)
selection_sort(l,size)
print(l)