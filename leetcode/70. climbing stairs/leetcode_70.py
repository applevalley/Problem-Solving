class Solution:
    def climbStairs(self, n: int) -> int:
        cnt = 0    
        
        def climbingStairs(temp):
            nonlocal cnt
            if (temp > n): return
            if (temp == n): 
                cnt += 1
                return

            climbingStairs(temp + 1)
            climbingStairs(temp + 2)

        climbingStairs(0)
        return cnt
