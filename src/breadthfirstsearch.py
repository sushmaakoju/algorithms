from collections import deque

def breadth_first_search(graph, node):
    q = deque()
    bfs_marker(node, q, graph)

def bfs_marker(node, q, graph):
    visited = set()
    q.append(node)
    visited.add(node)
    while q:
        node = q.popleft()
        print(node, end = ' ')
        for g in graph[node]:
            if g not in visited:
                q.append(g)
                visited.add(g)

def bfs(start):
    #queue FIFO
    visited = set()
    s = deque()
    s.append(start)
    visited.add(start)
    print(start.data)
    while len(s) >0:
        node = s.popleft()
        if node not in visited:
            visited.add(node)
            print(node.data)
        if node.left:
            s.append(node.left)
            visited.add(node.left)
            print(node.left.data)
        if node.right:
            s.append(node.right)
            visited.add(node.right)
            print(node.right.data)
        print(node)
        
    
