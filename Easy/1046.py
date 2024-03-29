class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            if stones[-1] == stones[-2]:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop(-1)
        if len(stones) == 0:
            return 0
        return stones[0]
