# directed_weighted_graph.py : Program to find shortest path matrix by Modified Warshall's (Floyd) algorithm.

INFINITY = 9999

class Vertex:
	def __init__(self, name):
		self.name = name

class DirectedWeightedGraph:
	def __init__(self, max_size=30):
		self.nvertices = 0
		self.nedges = 0
		self.adj = [ [0 for column in range(max_size)] for row in range(max_size) ]
		self.vertex_list = []
		self.D = [ [0 for column in range(max_size)] for row in range(max_size) ]		# Shortest Path Matrix
		self.Pred = [ [0 for column in range(max_size)] for row in range(max_size) ]	# Predecessor Matrix

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

	def _display(self, mat):
		for i in range(self.nvertices):
			for j in range(self.nvertices):
				print(mat[i][j], end=" ")
			print()	
	
	def display(self):
		for i in range(self.nvertices):
			for j in range(self.nvertices):
				print(self.adj[i][j], end=" ")
			print()

	def _is_adjacent(self, u, v):
		return self.adj[u][v] != 0

	def _floyd_warshalls_algorithm(self, s):
		# Getting D(-1), Pred(-1)
		for i in range(self.nvertices):
			for j in range(self.nvertices):
				if self.adj[i][j] == 0:
					self.D[i][j] = INFINITY
					self.Pred[i][j] = -1
				else:
					self.D[i][j] = self.adj[i][j]
					self.Pred[i][j] = i
					
		# Getting D(k), Pred(k)
		for k in range(self.nvertices):
			for i in range(self.nvertices):
				for j in range(self.nvertices):
					if (self.D[i][k]+self.D[k][j]) < self.D[i][j]:
						self.D[i][j] = self.D[i][k]+self.D[k][j]
						self.Pred[i][j] = self.Pred[k][j]

		# Finding negative cycle
		for i in range(self.nvertices):
			if self.D[i][i] < 0:
				raise Exception("There is a negative cycle in graph.")
		
		print("Shortest Path Matrix :")
		self._display(self.D)
		print("Predecessor Matrix :")
		self._display(self.Pred)

	def _find_path(self, s, v):
		path = []
		
		if self.D[s][v] == INFINITY:
			print("No path")
		else:
			while True:
				path.append(v)
				v = self.Pred[s][v]
				if v == s:
					break
		
			path.append(s)
			print("Shortest Path : ", end="")
			for u in reversed(path):
				print(self.vertex_list[u].name, end=" ")
			print()

	def find_paths(self, source):
		s = self._get_index(source)
		
		self._floyd_warshalls_algorithm(s)
		
		print("Source :", source)
		
		for v in range(self.nvertices):
			print("Destination : " + self.vertex_list[v].name)
			self._find_path(s, v)
			print("Shortest Distance :", self.D[s][v])

if __name__ == '__main__':
	
	dw_graph = DirectedWeightedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		dw_graph.insert_vertex("0")
		dw_graph.insert_vertex("1")
		dw_graph.insert_vertex("2")
		dw_graph.insert_vertex("3")

		dw_graph.insert_edge("0","1",2)
		dw_graph.insert_edge("0","3",9)
		dw_graph.insert_edge("1","0",3)
		dw_graph.insert_edge("1","2",4)
		dw_graph.insert_edge("1","3",7)
		dw_graph.insert_edge("2","1",6)
		dw_graph.insert_edge("2","3",2)
		dw_graph.insert_edge("3","0",14)
		dw_graph.insert_edge("3","2",4)

		# Graph with negative cycle
		# dw_graph.insert_vertex("0")
		# dw_graph.insert_vertex("1")
		# dw_graph.insert_vertex("2")
		# dw_graph.insert_vertex("3")
		# dw_graph.insert_vertex("4")

		# dw_graph.insert_edge("0","1",2)
		# dw_graph.insert_edge("0","2",7)
		# dw_graph.insert_edge("1","3",-9)
		# dw_graph.insert_edge("2","4",6)
		# dw_graph.insert_edge("3","0",4)
		# dw_graph.insert_edge("3","4",5)
		
		# Display the graph
		dw_graph.display()
		print()
		
		# Finding path from source vertex to other vertices
		dw_graph.find_paths("0")

	except Exception as e:
		print(e)
		
