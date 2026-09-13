class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = set() # visited cell

        def dfs(r,c):
            if (r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in path or grid[r][c] == 0):
                return 0 
            path.add((r,c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) not in path or grid[r][c] == "1"):
                    area = dfs(r,c)
                    max_area = max(max_area, area)    
        return max_area
