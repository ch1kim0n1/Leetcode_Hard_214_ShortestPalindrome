class Solution(object):
    def shortestPalindrome(self, s):
        rev = s[::-1]
        t = s + "#" + rev

        lps = [0] * len(t)

        for i in range(1, len(t)):
            j = lps[i - 1]

            while j > 0 and t[i] != t[j]:
                j = lps[j - 1]

            if t[i] == t[j]:
                j += 1

            lps[i] = j

        longest_pal_prefix = lps[-1]
        return rev[:len(s) - longest_pal_prefix] + s
