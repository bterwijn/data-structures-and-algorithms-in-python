# directed_weighted_graph.py : Program for directed graph with weight on edge using adjacency matrix.

class Vertex:
	def __init__(self, name):
		self.name = name

class DirectedWeightedGraph:
	def __init__(self, max_size=30):
		self.nvertices = 0
		self.nedges = 0
		self.adj = [ [0 for column in range(max_size)] for row in range(max_size) ]
		self.vertex_list = []
	
	def insert_vertex(self, vertex_name):
		self.vertex_list.append(Vertex(vertex_name))
		self.nvertices += 1
	
	def _get_index(self, vertex_name):
		index = 0
		for name in (vertex.name for vertex in self.vertex_list):
			if vertex_name == name:
				return index
			index += 1
		raise Exception("Invalid Vertex")

	def insert_edge(self, source, destination, weight):
		u = self._get_index(source)
		v = self._get_index(destination)

		if u == v:
			print("Not a valid edge")
		elif self.adj[u][v] != 0:
			print("Edge already present")
		else:
			self.adj[u][v] = weight
			self.nedges += 1
			
	def delete_edge(self, source, destination):
		u = self._get_index(source)
		v = self._get_index(destination)
		
		if self.adj[u][v] != 0:
			self.adj[u][v] = 0
			self.nedges -= 1
		else:
			print("Edge does not exist")
			
	def display(self):
		for i in range(self.nvertices):
			for j in range(self.nvertices):
				print(self.adj[i][j], end=" ")
			print()

	def _is_adjacent(self, u, v):
		return self.adj[u][v] != 0
		
	def edge_exists(self, source, destination):
		return self._is_adjacent(self._get_index(source), self._get_index(destination))

	def get_outdegree(self, vertex):
		u = self._get_index(vertex)
		
		outdegree = 0
		for v in range(self.nvertices):
			if self.adj[u][v] != 0:
				outdegree += 1
		
		return outdegree
		
	def get_indegree(self, vertex):
		u = self._get_index(vertex)
		
		indegree = 0
		for v in range(self.nvertices):
			if self.adj[v][u] != 0:
				indegree += 1
		
		return indegree
		
if __name__ == '__main__':
	
	dw_graph = DirectedWeightedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		dw_graph.insert_vertex("0")
		dw_graph.insert_vertex("1")
		dw_graph.insert_vertex("2")
		dw_graph.insert_vertex("3")

		dw_graph.insert_edge("0","3",1)
		dw_graph.insert_edge("1","2",2)
		dw_graph.insert_edge("2","3",3)
		dw_graph.insert_edge("3","1",4)
		dw_graph.insert_edge("0","2",5)
		
		# Display the graph
		dw_graph.display()
		print()
		
		# Deleting an edge
		dw_graph.delete_edge("0","2")
			
		# Display the graph
		dw_graph.display()
		print()

		# Check if there is an edge between two vertices
		print("Edge exist : ", dw_graph.edge_exists("2","3"))
		
		# Display Outdegree and Indegree of a vertex
		print("Outdegree : ", dw_graph.get_outdegree("3"))
		print("Indegree : ", dw_graph.get_indegree("3"))
		
	except Exception as e:
		print(e)
		
