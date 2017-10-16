#!/usr/bin/python3
import unittest



def greedy_activity_selector_iterative(s,f):
	""" Iterative solution to the activity-selection problem, with the following greedy choice: the first activity to be selected in a given subproblem is the last activity to start. The function returns the list of activities for an optimal solution, sorted by start times. See CLRS3, p. 421 for an analog algorithm where the greedy selection is the first activity to finish.

	
	:param s: the array of start times, sorted by finish times.
	:param f: the array of finish times, sorted.
	:rtype: list
	"""

	f.sort()

	n = len(s)

	A = []

	k = 0

	for m in range(0, n):
		if s[m] >= f[k]:
			A.append(m)
			k = m


	return A


class ActivitySelection_UnitTest(unittest.TestCase):


	# Sorted by _start time _
	S_prime = [ 0, 0, 1, 2, 3, 3, 5, 5, 6, 8, 8, 12 ]
	F_prime = [ 0, 6, 4, 14, 5, 9, 7, 9, 10, 11, 12, 16 ]
	

	def test_greedy_strategy_iterative_1(self):
		activities = greedy_activity_selector_iterative( self.S_prime, self.F_prime)
		self.assertEqual(len(activities), 4)

	def test_greedy_strategy_iterative_2(self):
		activities = greedy_activity_selector_iterative( self.S_prime, self.F_prime)
		self.assertTrue(self.is_mutually_compatible_set(activities, self.S_prime, self.F_prime))

	def test_greedy_strategy_iterative_3(self):
		activities = greedy_activity_selector_iterative( self.S_prime, self.F_prime)
		self.assertEqual( activities, [4, 6, 10, 11])

	def is_mutually_compatible_set(self, a, s, f):
		""" Utility function: return True  if the given subset contains only non-overlapping activities, False otherwise.

		:param a: the subset of activities, i.e. a list of activity IDs, sorted by start time
		:param s: the start times, sorted
		:param f: the finish times, sorted by start times
		:type a: list
		:type s: list
		:type f: list
		:rtype: bool
		"""
		if len(a) == 1: return True
		finish = f[ a[0] ]
		for k in a[1:]:
			if s[ k ] < finish:
				return False
			finish = f[ k ]
		return True


def main():
        unittest.main()

if __name__ == '__main__':
        main()

