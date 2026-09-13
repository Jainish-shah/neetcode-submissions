class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # path = set()

        def dfs(r,c):
            # invalid cases
            if (r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]=="0"):
                return

            # path.add((r,c))
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count

        