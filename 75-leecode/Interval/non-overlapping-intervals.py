'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

[1,2]
   [2,3]
     [3,4]
[1,   3]

sort = [[1,2], [1,3], [2,3],[3,4]]

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''


def eraseOverLapIntervals(intervals):

    intervals.sort()

    count = 0
    left = 0
    right = 1

    while right  < len(intervals):

        if intervals[left][1] <= intervals[right][0]:
            left += 1
            right += 1
            continue
        elif intervals[left][1] <= intervals[right][1]:
            right += 1
            count += 1

        else:
            count += 1
            left = right
            right += 1

    return count



intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverLapIntervals(intervals))

intervals = [[1,2],[2,3]]
print(eraseOverLapIntervals(intervals))

intervals = [[1,2],[1,2],[1,2]]
print(eraseOverLapIntervals(intervals))

intervals = [[1,2],[2,3],[3,4],[2,5], [1,3]]
print(eraseOverLapIntervals(intervals))