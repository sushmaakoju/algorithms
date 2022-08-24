from .treenode import TreeNode
from .utils import *
from collections import deque
#Insert elements + sort as you insert same as done in Binary search tree and
#traverses using in-order traversal. o(n^2) - worst case and O(nlog(n))
#
class TreeSort():
    def __init__(self, items=list()):
        self.root = None
        self.nodecount = 0
        self.sorted = list()
        if len(items) > 0:
            for item in items:
                self.insert(item)
    
    def __insert__(self, node, element):
        if node == None:
            self.root = TreeNode(element, None, None)
            node = self.root
        else:
            if cmp(element, node.data) < 0:
                node.left = self.__insert__(node.left, element)
            else:
                node.right = self.__insert__(node.right, element)
        return node
    
    def insert(self, element):
        if self.contains(element):
            return False
        else:
            self.root = self.__insert__(self.root, element)
            self.nodecount += 1
            return True

    def inorder(self):
        return self.__inorder__(self.root)

    def __inorder__(self, node):
        if node == None:
            return None
        
        if node.left != None:
            self.__inorder__(node.left)
        self.sorted.append(node.data)
        print(node.data)
        if node.right != None:
            self.__inorder__(node.right)
        return self.sorted
    
    def contains(self, element):
        result = self.__contains__(self.root, element)
        return result

    def __contains__(self, node, element):
        if node == None:
            return False
        if cmp(element, node.data) < 0:
            self.__contains__(node.left, element)
        elif cmp(element, node.data) > 0:
            self.__contains__(node.right, element)
        else:
            return True
        
