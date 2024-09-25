class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count = 0
        m, n = len(g), len(s)
        i, j = 0, 0

        while i < m and j < n:
            if g[i] <= s[j]:
                i += 1
                j += 1
                count += 1
            elif g[i] > s[j]:
                j += 1

        return count