#!/usr/bin/python3

import unittest
import collections as clt

from heap import *


log_level=1

def log( string, level=1):
	global log_level
	if log_level >= level:
		print(string)

class LabelException( Exception ): pass



class Vertex():
	""" A vertex definition."""

	# These constants can be referred to afterwards as follows:
	#	Vertex.WHITE, Vertex.GRAY...
	WHITE = 0
	GRAY = 1
	BLACK = 2
	INFTY = 2**15
	
	def __init__(self, label=''):
		"""
		Initialize a vertex
		
		:param index: position in the vertex array
		:param label: human-friendly label
		:type index: int
		:type label: str
		"""

		# a label (the index itself, or a letter)		
		self.label = label
		self.short_label = label[0]

		# distance = infinity by default
		self.distance = Vertex.INFTY
		self.pi = None
		self.color = Vertex.WHITE
		
		# for depth-first search
		self.discovery = 0
		self.finish = 0


	# overriding the > operator (for comparisons internal to the min-queue)
	def __gt__(self, other):
		if isinstance(other, Vertex):
			return self.distance > other.distance
		return NotImplemented
	
	def __str__(self):
		return '({}:{} dist={} )'.format(self.label, self.distance, self.pi)

class Graph():
	""" A graph definition """

	def __init__(self,v=(),e=()):
		""" Create graph with given vertices 

		:param v: labels, i.e. integers, or alphabetical labels
		:param e: edges, i.e pairs of labels
		:type v: tuple
		:type e: tuple	
		"""
	
		# Reads the vertex labels and create corresponding Vertex objects in V
		# Note: this is an ordered dictionary: pairs (key, value) are listed
		# in the order they were inserted, which is convenient for testing
		self.V = clt.OrderedDict()

		for label in v:
			self.V[label] = Vertex( label ) 
			
		# List of adjacency lists:  list containg |V| lists
		self.Adj  =  { vertex: [] for label, vertex in self.V.items() }

		# matrix representation
		self.Matrix = { v1: { v2: None for v2 in self.V.values() } for v1 in self.V.values() } 

		# Read the edges (pairs of labels) and create corresponding entries
		# in Adj
		for edge in e:
			v1, v2 = ( self.V[ edge[0] ], self.V[ edge[1] ])
			self.Adj[ v1 ].append( v2 )
			self.Matrix[ v1 ][ v2 ] = 1

			# storing weights in the matrix
			if (len(edge)>2):
				self.Matrix[v1][v2] = edge[2]
		
		self.time = 0

		self.myMinQueue = MinHeap( self.V.values() )
		 

###################################### TO BE IMPLEMENTED ########################
	def dijkstra(self, s):
		""" Dijkstra's shortest path algorithm

		:param s: starting vertex (a label)
		:type s: str
		"""

		self.initialize_single_source( self.V[s] )

		S = clt.OrderedDict()
		Q = self.V

		while ( len(Q) > 0 ):

			ux = self.myMinQueue.extract_min()

			if ux not in S:
				S[ux.label] = ux
				Q.pop(ux.label)

			for v in self.Adj[ ux ]:
				self.relax(ux, v)

		self.V = S


#################################################################################


	def initialize_single_source(self, s):
		""" Initialize the graph

		:param s: start vertex
		:type s: Vertex
		"""
		for label, v in self.V.items():
			v.distance = Vertex.INFTY
			v.pi = None
		s.distance = 0

	def relax(self, u, v):
		"""
		Relax vertex v through u

		:param u: vertex u
		:param v: vertex v
		:type u: Vertex
		:type v: Vertex
		"""
		if v.distance > (u.distance + self.Matrix[u][v] ):
			log('relax({},{}): {} --> {}'.format(u.label, v.label, v.distance, (u.distance + self.Matrix[u][v])),3)
			v.distance = (u.distance + self.Matrix[u][v] )

			# If the vertex is in a priority queue, ensure that it is floated down to its right
			# position in the queue after a change
			if hasattr(v,'heap') and v.heap is not None:
				v.float_key( v.heap_index )
			
			v.pi = u

	def __str__(self):
		output = 'V=['
		for v in self.V:
			output += str(v)+'\n'	
		output += ']\n'
		for u in range( 0, len(self.Adj)):
			output += '{}: '.format(u)
			for v in self.Adj[u]:
				output += ' {}'.format(v)
			output += '\n'
		return output




	
		
class GraphUnitTest( unittest.TestCase ):


	def test_dijkstra_1(self):
		""" Cormen Figure 24.6, p. 659 """
		g = self.make_dijkstra_graph()
		g.dijkstra( 's' )		

		self.assertEqual( g.V['s'].distance, 0)
		self.assertEqual( g.V['t'].distance, 8)
		self.assertEqual( g.V['x'].distance, 9)
		self.assertEqual( g.V['y'].distance, 5)
		self.assertEqual( g.V['z'].distance, 7)

	def test_dijkstra_2(self):
#		""" Cormen Figure 24.6, p. 659 """
		g = self.make_dijkstra_graph()
		g.dijkstra( 's' )		
#
		self.assertEqual( g.V['s'].pi, None)
		self.assertEqual( g.V['t'].pi, g.V['y'])
		self.assertEqual( g.V['x'].pi, g.V['t'])
		self.assertEqual( g.V['y'].pi, g.V['s'])
		self.assertEqual( g.V['z'].pi, g.V['y'])
#
	def test_dijkstra_3(self):
#		""" Gross & Yellen, p. 180 """
		g = self.make_dijkstra_graph_2()
		g.dijkstra( 's' )		
#
		self.assertEqual( g.V['s'].distance, 0)
		self.assertEqual( g.V['a'].distance, 5)
		self.assertEqual( g.V['b'].distance, 7)
		self.assertEqual( g.V['c'].distance, 13)
		self.assertEqual( g.V['d'].distance, 12)
		self.assertEqual( g.V['e'].distance, 4)
		self.assertEqual( g.V['f'].distance, 12)
		self.assertEqual( g.V['g'].distance, 5)
#
	def test_dijkstra_4(self):
#		""" Gross & Yellen, p. 180 """
		g = self.make_dijkstra_graph_2()
		g.dijkstra( 's' )		

		self.assertEqual( g.V['s'].pi, None)
		self.assertEqual( g.V['a'].pi, g.V['s'])
		self.assertEqual( g.V['b'].pi, g.V['s'])
		self.assertEqual( g.V['c'].pi, g.V['e'])
		self.assertEqual( g.V['d'].pi, g.V['e'])
		self.assertEqual( g.V['e'].pi, g.V['s'])
		self.assertEqual( g.V['f'].pi, g.V['e'])
		self.assertEqual( g.V['g'].pi, g.V['s'])
#
	def test_dijkstra_5(self):
#		""" Gross & Yellen, p. 180, directed version """
		g = self.make_dijkstra_graph_3()
		g.dijkstra( 's' )		

		self.assertEqual( g.V['s'].distance, 0)
		self.assertEqual( g.V['a'].distance, 4)
		self.assertEqual( g.V['b'].distance, 7)
		self.assertEqual( g.V['c'].distance, 7)
		self.assertEqual( g.V['d'].distance, 11)
		self.assertEqual( g.V['e'].distance, 3)
		self.assertEqual( g.V['f'].distance, 9)
		self.assertEqual( g.V['g'].distance, 8)
#
	def test_dijkstra_6(self):
#		""" Gross & Yellen, p. 180, directed version """
		g = self.make_dijkstra_graph_3()
		g.dijkstra( 's' )		

		self.assertEqual( g.V['s'].pi, None)
		self.assertEqual( g.V['a'].pi, g.V['e'])
		self.assertEqual( g.V['b'].pi, g.V['s'])
		self.assertEqual( g.V['c'].pi, g.V['e'])
		self.assertEqual( g.V['d'].pi, g.V['e'])
		self.assertEqual( g.V['e'].pi, g.V['s'])
		self.assertEqual( g.V['f'].pi, g.V['c'])
		self.assertEqual( g.V['g'].pi, g.V['a'])
#


	def make_dijkstra_graph(self):
		""" Cormen Figure 24.6, p. 659 """
		g = Graph(
			('s', 't', 'x', 'y', 'z'),
			(	('s','t',10), ('s','y',5),
				('t','x',1), ('t','y',2),
				('x','z',4),
				('y','t',3),('y','x',9),('y','z',2),
				('z','s',7),('z','x',6))
		)
		return g
	
	def make_dijkstra_graph_2(self):
		""" Gross & Yellen, p. 180 """
		g = Graph(
			('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g'),
			(	('s','a',5),('s','b',7), ('s','e',4),('s','g',5),
				('a','s',5),('a','g',4),
				('b','s',7),('b','c',9),('b','f',8),
				('c','b',9),('c','d',7),('c','e',9),('c','f',11),
				('d','e',8),('d','c',7),
				('e','s',4),('e','c',9),('e','d',8),('e','f',8),
				('f','b',8),('f','c',11),('f','e',8),
				('g','s',5),('g','a',4)))
		return g
	
	
	def make_dijkstra_graph_3(self):
		""" Gross & Yellen, p. 180, modified (directed) """
		g = Graph(
			('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g'),
			(	('s','a',5),('s','b',7), ('s','e',3),
				('a','g',4),
				('b','c',9),('b','f',8),
				('c','d',7),('c','f',2),
				('d','e',8),('d','c',1),
				('e','a',1),('e','c',4),('e','d',8),('e','f',12),
				('f','c',11),
				('g','s',5)))
		return g
	
	
def main():
        unittest.main()

if __name__ == '__main__':
        main()


