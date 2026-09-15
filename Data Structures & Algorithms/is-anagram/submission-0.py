class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a = sorted(s)
        b = sorted(t)

        if len(a) != len(b):
            return False

        for i in range(len(a)):
            if a[i] != b[i]:
                return False

        return True