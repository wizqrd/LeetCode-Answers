class Solution:
    def shortestPalindrome(self, s):  # OOP , storing self and s 
        def computeKMPTable(s): # Found KMP on the Web
            n = len(s) 
            table = [0] * n
            j = 0
            for i in range(1, n): 
                while j > 0 and s[i] != s[j]:
                    j = table[j - 1]
                if s[i] == s[j]:
                    j += 1
                table[i] = j
            return table

        rev_s = s[::-1]
        combined = s + '#' + rev_s
        kmp_table = computeKMPTable(combined)
        longest_palindromic_prefix = kmp_table[-1]
        return rev_s[:len(s) - longest_palindromic_prefix] + s