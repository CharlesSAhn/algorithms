'''

Given an unsorted array Arr with n positive integers. Find the  𝑘𝑡ℎ  smallest element in the given array, using Divide & Conquer approach.

Input: Unsorted array Arr and an integer k where  1 ≤ 𝑘 ≤ n
Output: The  𝑘𝑡ℎ  smallest element of array Arr

Example 1
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
Output = 99

Example 2
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 5
Output = 12

'''


def fastSelect(arr, k):

    n = len(arr)

    if k > 0 and k <= n:

        # Helper variables
        setOfMedians = []
        arr_less_p = []
        arr_equal_p = []
        arr_more_p = []
        i = 0

        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to setOfMedians
        while i < (n // 5):
            median = findMedian(arr, 5 * i, 5)
            setOfMedians.append(median)
            i += 1

        # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if i* 5 < n:
            median = findMedian(arr, i * 5, n % 5)
            setOfMedians.append(median)

        # Step 3 - Find the median of setOfMedians
        if len(setOfMedians) == 1:
            pivot = setOfMedians[0]
        elif len(setOfMedians) > 1:
            pivot = fastSelect(setOfMedians, len(setOfMedians) // 2)

        # Step 4 - Partition the original Arr into three sub-arrays
        for element in arr:

            if element < pivot:
                arr_less_p.append(element)
            elif element > pivot:
                arr_more_p.append(element)
            else:
                arr_equal_p.append(element)

        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if k <= len(arr_less_p):
            return fastSelect(arr_less_p, k)

        elif k > (len(arr_less_p) + len(arr_equal_p)):
            return fastSelect(arr_more_p, (k - len(arr_less_p) - len(arr_equal_p)))
        else:
            return pivot


def findMedian(arr, start, size):
    myList = []

    for i in range(start, start + size):
        myList.append(arr[i])

    myList.sort()

    return myList[size//2]


Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))