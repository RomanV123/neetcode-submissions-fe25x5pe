class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(len(intervals) - 1 ):
            current_interval = intervals[i]
            next_interval = intervals[i+1]

            if next_interval.start < current_interval.end:
                return False
        
        return True