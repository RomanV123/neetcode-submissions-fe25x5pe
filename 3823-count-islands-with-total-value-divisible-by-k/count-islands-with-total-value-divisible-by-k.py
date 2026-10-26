class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        directions = [
    (-1, 0),  # Up:    decrease row, same col
    (1, 0),  # Down:  increase row, same col
    (0, -1),  # Left:  same row, decrease col
    (0, 1),  # Right: same row, increase col
]
       
        visited = set()
        island_sum = 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and (i, j) not in visited:
                    island_sum = 0
                    queue = [(i,j)]
                    visited.add((i,j))

                    while queue:
                        row, col = queue.pop(0)
                        island_sum += grid[row][col]

                        for dr,dc in directions:
                            new_row = row + dr
                            new_col = col + dc
                            
                            if (
                                0 <= new_row < len(grid)
                                and 0 <= new_col < len(grid[0])
                                and grid[new_row][new_col] > 0
                                and (new_row, new_col) not in visited
                            ):

                                visited.add((new_row,new_col))
                                queue.append((new_row,new_col))


                    if island_sum % k == 0:
                        count +=1
        return count 