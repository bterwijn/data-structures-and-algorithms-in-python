# directed_graph.py : Program to find out the path matrix using warshall's algorithm.

class Vertex:
	def __init__(self, name):
		self.name = name

class DirectedGraph:
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

	def insert_edge(self, source, destination):
		u = self._get_index(source)
		v = self._get_index(destination)

		if u == v:
			print("Not a valid edge")
		elif self.adj[u][v] != 0:
			print("Edge already present")
		else:
			self.adj[u][v] = 1
			self.nedges += 1
			
	def display(self):
		for i in range(self.nvertices):
			for j in range(self.nvertices):
				print(self.adj[i][j], end=" ")
			print()

	def warshalls_algorithm(self):
		P = [ [0 for column in range(self.nvertices)] for row in range(self.nvertices) ]

		# Initializing P(-1)
		for i in range(self.nvertices):
			for j in range(self.nvertices):
				P[i][j] = self.adj[i][j]
				
		# P0,P1......Pn-1
		for k in range(self.nvertices):
			for i in range(self.nvertices):
				for j in range(self.nvertices):
					P[i][j] = 1 if ((P[i][j]!=0) or (P[i][k]!=0 and P[k][j]!=0 )) else 0
			
			# Display P
			print("P" + str(k) + ":")
			for i in range(self.nvertices):
				for j in range(self.nvertices):
					print(P[i][j], end=" ")
				print()

if __name__ == '__main__':
	
	d_graph = DirectedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		d_graph.insert_vertex("0")
		d_graph.insert_vertex("1")
		d_graph.insert_vertex("2")
		d_graph.insert_vertex("3")

		d_graph.insert_edge("0","1")
		d_graph.insert_edge("0","3")
		d_graph.insert_edge("1","0")
		d_graph.insert_edge("1","2")
		d_graph.insert_edge("1","3")
		d_graph.insert_edge("2","3")
		d_graph.insert_edge("3","0")
		d_graph.insert_edge("3","2")

		# Display the graph
		d_graph.display()
		print()
		
		print("Find the path matrix :");
		d_graph.warshalls_algorithm();
		
	except Exception as e:
		print(e)
		
