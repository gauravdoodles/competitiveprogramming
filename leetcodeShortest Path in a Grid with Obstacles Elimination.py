from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        nColumn = len(grid[0])
        nRow = len(grid)
        visited = {str(0): k}
        
        if nRow == 1 and nColumn == 1:
            return 0
        
        queue = deque([(0, 0, k, 0)]) #row column k steps
        directions = [(0,1), (-1,0), (1,0), (-1,0)]
        while len(queue):
            row, column, eliminate, steps = queue.popleft()
            for i in directions:
                newRow = i[0] + row
                newColumn = i[1] + column
                if 0 <= newRow < nRow and 0<=newColumn < nColumn:
                    newK = eliminate if grid[newRow][newColumn] == 0 else eliminate -1
                    if newK < 0:
                        continue
                    if newRow == nRow -1 and newColumn == nColumn -1:
                        return steps + 1

                    key = str(newRow*nColumn+newColumn)
                    if key not in visited.keys() or visited[key] < newK:
                        visited[key] = newK
                        queue.append((newRow, newColumn, newK, steps + 1))
        return -1
        
