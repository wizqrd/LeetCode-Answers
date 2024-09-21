class Solution:
    def lexicalOrder(self, n):
        result = []
        
        def dfs(curr):
            if curr > n:
                return
            result.append(curr)
            for i in range(10):
                dfs(curr * 10 + i)
        
        for i in range(1, 10):
            dfs(i)
        
        return result