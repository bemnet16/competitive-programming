class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        new_interval = [intervals[0]]

        for s, e in intervals[1:]:
            last = new_interval[-1][1]

            if s <= last:
                new_interval[-1][1] = max(last,e)
            else:
                new_interval.append([s,e])

        return new_interval
