from collections import deque
class GraphI():
    def __init__(self, matrix):
        self.graph = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        #there are 8 neighbors for a given i,j cell
        self.row_neighbors = [-1,-1,-1,0,0,1,1,1]
        self.col_neighbors = [-1,0,1,-1,1,-1,0,1]

    def is_valid(self, i, j, visited):
        return (i >=0 and i < self.rows and
                j >= 0 and j < self.columns and not visited[i][j]
                and self.graph[i][j])

    def dfs(self, i, j, visited):
        visited[i][j] =  True
        for k in range(8):
            if self.is_valid(i+self.row_neighbors[k], 
                    j+self.col_neighbors[k], visited):
                self.dfs(i+self.row_neighbors[k], j+self.col_neighbors[k], visited)

    def count_islands(self):
        count = 0
        visited = [[False for j in range(0,self.columns)] for i in range(0,self.rows)]
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                if visited[i][j] == False and self.graph[i][j] == 1:
                    self.dfs(i,j, visited)
                    count += 1
        return count
mat = [[1, 1, 0, 0,0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
g = GraphI(mat)
res = g.count_islands()
print(res)
