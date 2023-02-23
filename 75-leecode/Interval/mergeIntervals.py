'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.


Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

input = [[]]
input = [ [1,3]]
input = [ [3,3] ]


'''

# def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#     res = []
#     intervals.sort()
#     last_min = intervals[0][0]
#     last_max = intervals[0][1]
#     for interval in intervals[1:]:
#         if interval[0] <= last_max:
#             last_max = max(last_max, interval[1])
#         else:
#             res.append([last_min, last_max])
#             last_min = interval[0]
#             last_max = interval[1]
#     res.append([last_min, last_max])
#     return res

def insert_intervals(intervals, newIntervals):

    res = []

    for i, interval in enumerate(intervals):

        if newIntervals[1] < interval[0]:
            res.append(newIntervals)
            return res + intervals[i:]

        elif newIntervals[0] > interval[1]:
            res.append(interval)

        else:
            newIntervals = [min(newIntervals[0], interval[0]), max(newIntervals[1], interval[1])]

    res.append(newIntervals)

    return res


def mergeIntervals(input):

    if len(input) < 2:
        return input


    result = [input[0]]

    for i in range(1, len(input)):

        result = insert_intervals(result, input[i])

    return result


print(mergeIntervals( [[1,3],[2,6],[8,10],[15,18]]))
print(mergeIntervals([[1,3],[4,5]]))
print(mergeIntervals([[1,3]]))

input = [[1,3],[2,6],[8,10],[15,18], [7,12]]
input.sort()
for x in input:
    print(x)


