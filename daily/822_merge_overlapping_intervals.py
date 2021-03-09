"""
[EASY]
Asked by Snapchat

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)]
"""

"""
Assumptions: each interval is in ascending order (min, max)

Sort the interval list based on their min value
initialize result collection
iterate over sorted intervals
compare current interval against the latest result interval, if there is one
    then, if the current interval's min value is less or equal to the latest result's interval max value
        then, if the current interval's max value is greater than the latest result's interval max value
            then, replace the latest result interval for one composed of the latest result's interval min value and the current interval max value
    otherwise, add the current interval to the result
"""

"""
For [(1, 3), (5, 8), (4, 10), (20, 25)]
1. Sort the interval list
    [(1, 3), (4, 10), (5, 8), (20, 25)]
2. initialize result
    result = []
3. iterate over sorted intervals
    i = 0
    restult = []
    current interval = (1, 3)
    is there a latest result interval? No.
    add current interval to result

    i = 1
    result = [(1, 3)]
    current interval = (4, 10)
    is there a latest result interval? Yes.
    compare current interval and latest result interval
    is 4 <= 3? No
    add current interval to result

    i = 2
    result = [(1, 3), (4, 10)]
    current interval = (5, 8)
    is there a latest result interval? Yes.
    compare current interval and the latest result interval
    is 5 <= 10? Yes
    is 8 > 10? No
    
    i = 3
    result = [(1, 3), (4, 10)]
    current interval = (20, 25)
    is there a latest result interval? Yes.
    compare current interval and latest result interval
    is 20 <= 10? No
    add current interval to result

    return result = [(1, 3), (4, 10), (20, 25)]
"""

from collections import Counter


def merge_intervals(intervals):
    result = []
    for interval in sorted(intervals, key=lambda i: i[0]):
        if result and interval[0] <= result[-1][1]:
            if interval[1] > result[-1][1]:
                result[-1] = (result[-1][0], interval[1])
        else:
            result.append(interval)
    return result


def compare(l1, l2):
    return Counter(l1) == Counter(l2)


assert compare(merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]), [(1, 3), (4, 10), (20, 25)])
assert compare(merge_intervals([(1, 3), (2, 4), (3, 5), (4, 6)]), [(1, 6)])
