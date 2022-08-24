from collections import defaultdict, deque
from .treenode import TreeNode
#use set instead of list for better time complexity on traversal on graph or tree
#list -> O(n) and for set -> avg case and worst case: O(1) and O(n)
#****************************recursive DFS******************************
def dfs_marker(node, visited, graph):
        visited.add(node)
        print(node, end = ' ')
        for i in graph[node]:
            if i not in visited:
                dfs_marker(i, visited, graph)

def depth_first_search_traversal(node, graph):
        visited = set()
        dfs_marker(node, visited, graph)
        print(visited)

#****************************iterative DFS******************************
def dfs(start : TreeNode):
    #stack LIFO
    visited = set()
    s = deque()
    s.append(start)
    visited.add(start)
    print(start.data)
    while len(s) > 0:
        node = s.pop()
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

        