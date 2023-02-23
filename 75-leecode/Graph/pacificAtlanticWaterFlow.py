'''

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west
if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Input: heights =
[
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]]


Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]


Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]

Given a cell:
- (value >= left or value >= top) and (value >= right or value >= bottom)

'''

from _collections import deque

def pacificAtlantic(heights):


    '''
    time: O( m * n )
    space: O( m * n )

    '''

    nrows = len(heights)
    ncols = len(heights[0])

    pacific_set, atlantic_set = set(), set()

    def bfs(r, c, visited):

        queue = deque()
        queue.append((r,c))
        visited.add((r,c))

        while queue:
            qr, qc = queue.popleft()

            for nr, nc in [ (qr + 1, qc ), (qr - 1, qc), (qr, qc + 1), ( qr, qc -1 ) ]:
                if (
                    nr <0
                    or nr >= nrows
                    or nc < 0
                    or nc >= ncols
                    or (nr, nc) in visited
                    or heights[nr][nc] < heights[qr][qc]
                ):
                    continue
                visited.add((nr, nc))
                queue.append((nr, nc))

    #pacific top
    for col in range(0, ncols):
        bfs(0, col, pacific_set)

    # pacific left
    for row in range(0, nrows):
        bfs(row, 0, pacific_set)

    # atlantic right
    for row in range(0, nrows):
        bfs(row, ncols - 1, atlantic_set)

    # atlantic bottom
    for col in range(0, ncols):
        bfs(nrows - 1, col, atlantic_set)

    res = []
    for (r, c) in pacific_set:
        if (r, c) in atlantic_set:
            res.append([r, c])

    return res


print(
    pacificAtlantic(
        heights=[
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
)
print(pacificAtlantic(heights=[[2, 1], [1, 2]]))