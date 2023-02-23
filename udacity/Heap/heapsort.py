


def heapsort(arr):

    # First convert the array into a maxheap by calling heapify on each node, starting from the end
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted

    for i in range(len(arr)-1, -1, -1):
        heapify(arr, len(arr), i)

    print(arr)

    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

    print(arr)



def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top



    """
    largest_index = i
    left_child = (i * 2) + 1
    right_child = (i * 2) + 2

    if left_child < n and arr[left_child] > arr[i]:
        largest_index = left_child

    if right_child < n and arr[right_child] > arr[largest_index]:
        largest_index = right_child

    if largest_index != i:
        arr[largest_index], arr[i] = arr[i], arr[largest_index]

        heapify(arr, n, largest_index)





arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]

heapsort(arr)

#         3
#      7    4
#     6 1  0 9
#    89 43 5

