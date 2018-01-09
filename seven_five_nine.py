# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        intervals = [interval for employee_schedule in schedule for interval in employee_schedule]
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        free_intervals = []
        last_interval = intervals[0]
        for interval in intervals[1:]:
            if interval.start > last_interval.end:
                free_intervals.append(Interval(last_interval.end, interval.start))
            if interval.start > last_interval.end or interval.end > last_interval.end:
                last_interval = interval
        return free_intervals

