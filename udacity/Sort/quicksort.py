

def sort(input):

    end_index = len(input) - 1

    sort_all(input, 0, end_index)

    return input


def sort_all(input, left_index, end_index):

    if left_index >= end_index:
        return

    pivot = quicksort(input, left_index, end_index)
    sort_all(input, left_index, pivot - 1)
    sort_all(input, pivot + 1, end_index)


def quicksort(input, left_index, pivot_index):


    while left_index < pivot_index:

        pivot_value = input[pivot_index]
        left_value = input[left_index]

        if pivot_value < left_value:
            input[left_index] = input[pivot_index-1]
            input[pivot_index-1] = pivot_value
            input[pivot_index] = left_value

            pivot_index -= 1
        else:
            left_index += 1

    return pivot_index


items = [8, 3, 1, 7, 0, 10, 2]

print(sort(items))

items = [1, 0]
sort(items)
print(items)

items = [96, 97, 98]
sort(items)
print(items)