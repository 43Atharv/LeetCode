class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels = list(str(jewels))
        counts = []
        for i in range(len(jewels)):
            counts.append(stones.count(jewels[i]))
        total = sum(counts)
        return total