class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        f = 1
        prev = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            curr = pair[i]
            curtime = (target - curr[0])/curr[1]
            if curtime > prev:
                f += 1
                prev = curtime
        return f