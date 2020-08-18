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