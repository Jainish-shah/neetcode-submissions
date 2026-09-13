class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting
        # checking the condition 
        # appending to the List
        # return the output List

        intervals.sort(key= lambda i : i[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastV = result[-1][1]
            if start <= lastV:
                result[-1][1] = max(end, lastV)
            else:
                result.append([start, end])
        return result