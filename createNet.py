import networkx as net
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import math
import time

def show(g):
	net.draw(g)
	plt.show()
	plt.close()

def createRefGraph():
	g = net.Graph()
	g.add_edges_from([('v','a'), ('v','b'), ('v','c'), ('v','d'), ('a','b'), ('a','e'), ('a','f'), ('a','g'), ('b','f'), ('c','d'), ('c','g'), ('c','h'), ('d','h'), ('d','i'), ('h','i'), ('i', 'l'), ('f', 'j'), ('f', 'k')])
	#g.add_edges_from([(0,1), (0,2), (0,3), (0,4), (1,2), (1,5), (1,6), (1,7), (2,6), (3,4), (3,7), (3,8), (4,8), (4,9), (8,9), (9, 12), (6, 10), (6, 11)])
	return g

def getNeighborGraph(g, center):
	g2 = net.Graph()
	neighbors = g.neighbors(center)
	for neighbor in neighbors:
		g2.add_edge(center, neighbor)
	return g2

def getEgoGraph(g, center):
	g2 = net.Graph()
	node2Index = {}
	index2Node = {}
	g2.add_node(center)
	firstNeighbors = g.neighbors(center)

	node2Index[center] = 0
	index2Node[0] = center

	i = 1;
	for neighbor in firstNeighbors:
		node2Index[neighbor] = i
		index2Node[i] = neighbor
		i += 1;

	for neighbor in firstNeighbors:
		g2.add_edge(neighbor, center)
		NeighborsOfNeighbors = g.neighbors(neighbor)
		for nneighbor in NeighborsOfNeighbors:
			if (nneighbor == center):
				continue
			if nneighbor in firstNeighbors:
				g2.add_edge(neighbor, nneighbor)
	return g2, firstNeighbors, node2Index, index2Node				
		
def getXEgoGraph(g, center):
	g2 = net.Graph()
	node2Index = {}
	index2Node = {}
	g2.add_node(center)
	firstNeighbors = g.neighbors(center)

	node2Index[center] = 0
	index2Node[0] = center
			
	i = 1;
	for neighbor in firstNeighbors:
		node2Index[neighbor] = i
		index2Node[i] = neighbor
		i += 1;

	secondNeighbors = []
	for neighbor in firstNeighbors:
		g2.add_edge(neighbor, center)
		secondNeighborsOfNode = g.neighbors(neighbor)
		for nneighbor in secondNeighborsOfNode:
			if (nneighbor == center):
				continue
			if nneighbor in firstNeighbors:
				g2.add_edge(neighbor, nneighbor)
			else:
				g2.add_edge(neighbor, nneighbor)
				if not (nneighbor in secondNeighbors):
					secondNeighbors.append(nneighbor)
					node2Index[nneighbor] = i
					index2Node[i] = nneighbor					
					i += 1
	return g2, firstNeighbors, secondNeighbors, node2Index, index2Node
