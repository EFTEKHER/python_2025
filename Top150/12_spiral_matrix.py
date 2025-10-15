class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        tasks.sort()
        curr_time = 0
        for start, duration in tasks:
            if curr_time < start:
                curr_time = start
            curr_time += duration
        return curr_time