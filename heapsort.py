#!/usr/bin/python3

import unittest
import math

""" A HeapSort module. For more information on how to implement the functions, refer to CLRS3, chapter 6: the module's organization follows the text's exposition faithfully.

"""

########### DO NOT MODIFY ####################
class Heap(list):
	"""
	A Heap object is just a normal Python list, with an extra `size` field. For conveniency, this type is used throughout the module for all arrays, even if they are not actually max-heaps.

	.. warning:: The class `Heap` is not meant to be modified.
	"""
	def __init__(self, lst):
		"""
		Initializes a new heap from a list.
		"""
		super().__init__(lst) # calling the superclass (list) constructor
		self.size = len(self)


############ ASSIGNMENT STARTS HERE #########

def left(i):
	"""
	Return the left child of the given node.
	
	The procedure is just an arithmetical computation of the L child's index. Checking that such a child exists is left to the caller function.

 	.. warning:: Because Python arrays are numbered from 0 to 1, the pseudo-code shown in CLRS3, chapter 6 needs to be adapted. Draw a small tree on scratch paper, with nodes numbered from 0 to n, and, working from a few example nodes, try to figure out a formula to compute the index of the L child.
 
	:param i: index of the node in the heap
	:type i: int
	:return: the index of the given node's left child
	:rtype: int
	"""
	return 2 * i + 1

def right(i):
	"""
	Return the right child of the given node.

	The procedure is just an arithmetical computation of the R child's index. Checking that such a child exists is left to the caller function.

 	.. warning:: Because Python arrays are numbered from 0 to 1, the pseudo-code shown in CLRS3, chapter 6 needs to be adapted. Draw a small tree on scratch paper, with nodes numbered from 0 to n, and, working from a few example nodes, try to figure out a formula to compute the index of the L child.
	
	:param i: index of the node in the heap
	:type i: int
	:return: the index of the given node's right child
	:rtype: int
	"""
	return 2 * i + 2

def parent(i):
	"""
	Return the parent of the given node.

	The procedure is just an arithmetical computation of the parent's index. Checking that such a parent exists is left to the caller function.
	
 	.. warning:: Because Python arrays are numbered from 0 to 1, the pseudo-code shown in CLRS3, chapter 6 needs to be adapted. Draw a small tree on scratch paper, with nodes numbered from 0 to n, and, working from a few example nodes, try to figure out a single formula that relate the L and R children indices and their parent's.

	:param i: index of the node in the heap
	:type i: int
	:return: the index of the given node's parent
	:rtype: int
	"""
	return math.floor((i- 1) / 2)

# def heap_size(A):
# 	return len(A) - 1


def max_heapify(A,i):
	"""
	Given an array A, and assuming that the subtrees rooted at A[i]'s L and R children are max-heaps, restore the max-heap property.

	.. note:: The procedure does not return a new tree and simply modifies the array in place.
	
	:param A: an array.
	:param i: the index of the  node to be floated down
	:type A: heapsort.Heap
	:type i: int
	"""

	l = left(i)
	r = right(i)
	if l <= A.size - 1 and A[l] > A[i]:
		largest = l
	else:
		largest = i
	if r <= A.size - 1 and A[r] > A[largest]:
		largest = r
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		max_heapify(A,largest)



def build_max_heap(A):
	""" Build a max-heap, from an unsorted array. 

	.. note:: The first node to be processed is the parent of the last leaf.
	
	:param A: the array to be sorted.
	:type A: heapsort.Heap
	"""

	A.size = len(A)
	for i in range(math.floor(len(A)/2), 0, -1):
		max_heapify(A, i-1)




def HeapSort(A):
	""" Sort the array in place.
	
	.. note:: The function sorts in place, and therefore does not return anything.

	:param A: an array, with values in random order - do not assume that the array is already a max-heap! The `build_max_heap` procedure needs to be run on A before the actual sorting takes place.
	:type A: heapsort.Heap
	"""

	build_max_heap(A)
	for i in range(len(A)-1, 0, -1):
		A[i], A[0] = A[0], A[i]
		A.size = A.size - 1
		max_heapify(A,0)





############# DO NOT MODIFY ##############################
class testHeapSort(unittest.TestCase):

	
	def test_left_1(self):
		self.assertEqual( left(0), 1 )

	def test_left_2(self):
		self.assertEqual( left(2), 5 )

	def test_left_3(self):
		self.assertEqual( left(3), 7 )

	def test_right_1(self):
		self.assertEqual( right(0), 2 )

	def test_right_2(self):
		self.assertEqual( right(2), 6 )

	def test_right_3(self):
		self.assertEqual( right(3), 8 )

	def test_parent_1(self):
		self.assertEqual( parent(1), 0 )
	
	def test_parent_2(self):
		self.assertEqual( parent(2), 0 )
	
	def test_parent_3(self):
		self.assertEqual( parent(3), 1 )
	
	def test_parent_4(self):
		self.assertEqual( parent(4), 1 )

	def test_max_heapify_general_case(self):
		""" 
		CLRS3, exercise 6.2-1
		"""
		A = Heap([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])
		max_heapify(A,2)
		self.assertEqual( A, [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0])

	def test_max_heapify_untouched(self):
		""" 
		MaxHeapify() does not change the array if A[i] is larger than its two children
		"""
		A = Heap([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])
		max_heapify(A, 1)
		self.assertEqual(A, [ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])


	def test_buildmaxheap_unique_values(self):
		"""
		BuildMaxHeap: general case, with non-repeated values
		"""
		A = Heap([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
		build_max_heap(A)
		self.assertEqual(A, [19, 17, 18, 16, 10, 6, 12, 13, 1, 8, 5, 4, 2, 3])

	def test_buildmaxheap_repeated_values(self):
		"""
		BuildMaxHeap: general case, with repeated values
		"""
		A = Heap([7, 16, 7, 4, 8, 13, 18, 3, 10, 7, 12, 8, 17, 3])
		build_max_heap(A)
		self.assertEqual(A, [18, 16, 17, 10, 12, 13, 7, 3, 4, 7, 8, 8, 7, 3])

	def test_buildmaxheap_1_element_array(self):
		"""
		BuildMaxHeap: special case - 1-element array
		"""
		A = Heap([7])
		build_max_heap(A)
		self.assertEqual(A, [7])

	def test_heapsort_unique_values(self):
		"""
		HeapSort: general case, with unique values
		"""
		A = Heap([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
		HeapSort(A)
		self.assertEqual(A, [1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 16, 17, 18, 19])

	def test_heapsort_repeated_values(self):
		"""
		HeapSort: general case, with repeated values
		"""
		A = Heap([7, 16, 7, 4, 8, 13, 18, 3, 10, 7, 12, 8, 17, 3])
		HeapSort(A)
		self.assertEqual(A, [3, 3, 4, 7, 7, 7, 8, 8, 10, 12, 13, 16, 17, 18])

	def test_heapsort_1_element_array(self):
		"""
		HeapSort: special case - 1-element array
		"""
		A = Heap([7])
		HeapSort(A)
		self.assertEqual(A, [7])





def main():
        unittest.main()

if __name__ == '__main__':
        main()


