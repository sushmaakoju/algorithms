import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
import unittest
from src.binarysearch import BinarySearch
from src.quicksort import *
from src.mergesort import *
from src.o_n_square_sorting import *
from src.timsort import *
from src.treesort import TreeSort
from src.graph import Graph
from src.depthfirstsearch import *
from src.breadthfirstsearch import *
from src.treenode import TreeNode
from src.max_heapify import *
from src.heapsort import *

class TestAlgorithms(unittest.TestCase):

    def test_binary_search(self):
        bs = BinarySearch()
        self.assertEqual(bs.binary_search([ 2, 3, 4, 10, 40 ] , 10), 3)
    
    def test_quicksort(self):
        arr = [10, 80, 30, 90, 40, 50, 70]
        quicksort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [10, 30, 40, 50, 70, 80, 90])
        arr = [10, 80, 30, 90, 40, 50, 70]
        quicksort_hp(arr, 0, len(arr)-1)
        self.assertEqual(arr, [10, 30, 40, 50, 70, 80, 90])
    
    def test_mergesort(self):
        arr = [10, 80, 30, 90, 40, 50, 70]
        self.assertEqual(mergesort(arr), [10, 30, 40, 50, 70, 80, 90])
    
    def test_bubblesort(self):
        arr = [10, 80, 30, 90, 40, 50, 70]
        bubblesort(arr)
        self.assertEqual(arr, [10, 30, 40, 50, 70, 80, 90])
    
    def test_cocktail_sort(self):
        arr = [10, 80, 30, 90, 40, 50, 70]
        cocktail_sort(arr)
        self.assertEqual(arr, [10, 30, 40, 50, 70, 80, 90])

    def test_insertion_sort(self):
        arr = [10, 80, 30, 90, 40, 50, 70]
        insertionsort(arr)
        self.assertEqual(arr, [10, 30, 40, 50, 70, 80, 90])
        arr = [10, 80, 30, 90, 40, 50, 70]
        inserstion_sort(arr)
        self.assertEqual(arr, [10, 30, 40, 50, 70, 80, 90])
    
    def test_selection_sort(self):
        arr = [10, 80, 30, 90, 40, 50, 70]
        selectionsort(arr)
        self.assertEqual(arr, [10, 30, 40, 50, 70, 80, 90])

    def test_tim_sort(self):
        arr = [10, 80, 30, 90, 40, 50, 70]
        timsort(arr)
        print(arr)
        self.assertEqual(arr, [10, 30, 40, 50, 70, 80, 90])
    
    def test_treesort(self):
        items = ['M', 'J', 'S', 'B', 'N', 'Z', 'A']
        treesort = TreeSort(items)
        sorted = treesort.inorder()
        self.assertEqual(sorted, ['A', 'B', 'J', 'M', 'N', 'S', 'Z'])
    
    def test_dfs(self):
        g = Graph()
        g.add_edge(0,1)
        g.add_edge(0,2)
        g.add_edge(1,2)
        g.add_edge(2,0)
        g.add_edge(2,3)
        g.add_edge(3,3)
        depth_first_search_traversal(2, g.graph)
                
        g = Graph()
        g.add_edge('a','b')
        g.add_edge('a','c')
        g.add_edge('b','c')
        g.add_edge('c','a')
        g.add_edge('c','d')
        g.add_edge('d','d')
        depth_first_search_traversal('c', g.graph)


    def test_bfs(self):
        g = Graph()
        g.add_edge(0,1)
        g.add_edge(0,2)
        g.add_edge(1,2)
        g.add_edge(2,0)
        g.add_edge(2,3)
        g.add_edge(3,3)
        breadth_first_search(g.graph, 2)
                
        g = Graph()
        g.add_edge('a','b')
        g.add_edge('a','c')
        g.add_edge('b','c')
        g.add_edge('c','a')
        g.add_edge('c','d')
        g.add_edge('d','d')
        breadth_first_search(g.graph, 'c')
    
    def test_bfs_tree(self):
        node = TreeNode(0, None, None)
        node.left = TreeNode(1, TreeNode(3, None, None), TreeNode(4, None, None))
        node.right = TreeNode(2, TreeNode(5, None, None), TreeNode(6, None, None))
        bfs(node)
    
    def test_dfs_tree(self):
        node = TreeNode(0, None, None)
        node.left = TreeNode(1, TreeNode(3, None, None), TreeNode(4, None, None))
        node.right = TreeNode(2, TreeNode(5, None, None), TreeNode(6, None, None))
        dfs(node)
    
    def test_max_heap(self):
        arr = [100, 19, 36, 17,3,2,7, 25,1]
        heapsort(arr, "max")
        arr = [100, 19, 36, 17,3,2,7, 25,1]
        heapsort(arr, "min")
        arr = [ 12, 11, 13, 5, 6, 7] 
        heapsort(arr, "max")
        arr = [ 12, 11, 13, 5, 6, 7] 
        heapsort(arr, "min")
