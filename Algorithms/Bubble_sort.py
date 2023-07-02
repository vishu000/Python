def bubble_sort(array,size):
    for i in range(size):
        for j in range(0,size - i - 1):
            if array[j] > array[j+1]:
              temp = array[j]
              array[j] = array[j+1]
              array[j+1] = temp

l = [-2, 45, 0, 11, -9]
size = len(l)
print(size)
bubble_sort(l,size)
print(l)