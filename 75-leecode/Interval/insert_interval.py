'''

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.

You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]


Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


constraints:
- 0 <= intervals.length <= 104
- intervals[i].length == 2
- 0 <= starti <= endi <= 105
- intervals is sorted by starti in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 105
'''


def insert(intervals, newInterval):

    res = []

    for i, interval in enumerate(intervals):

        #if end of new interval is less than curr start, then it must be less than everything in front.

        if newInterval[1] < interval[0]:
            res.append(newInterval)
            return res + intervals[i:]

        #if start of new interval is greater than curr then no merging is needed.
        elif newInterval[0] > interval[1]:
            res.append(interval)

        else:
            newInterval = [ min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

    res.append(newInterval)

    return res



# print(insert([[3,6],[9,12]], [5,7]))
# print(insert([[3,6]], [4,5]))
# print(insert([[1,5]], [2,7]))
# print(insert([[3,6],[9,12]], [7,10]))
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))