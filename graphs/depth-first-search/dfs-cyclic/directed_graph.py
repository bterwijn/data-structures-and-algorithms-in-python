# directed_graph.py : Program for traversing a directed graph through DFS using recursion and finding out that graph is 
# cyclic or not

INITIAL = 0
VISITED = 1
FINISHED = 2

class Vertex:
	def __init__(self, name):
		self.name = name
		self.state = None

class DirectedGraph:
	has_cycle = None
	
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

	def _is_adjacent(self, u, v):
		return self.adj[u][v] != 0

	def _dfs(self, vertex):
		self.vertex_list[vertex].state = VISITED

		for i in range(self.nvertices):
			if self._is_adjacent(vertex,i):
				if self.vertex_list[i].state==INITIAL:
					# It's Tree Edge
					self._dfs(i)
				elif self.vertex_list[i].state==VISITED:
					# It's Back Edge
					DirectedGraph.has_cycle = True
		
		self.vertex_list[vertex].state = FINISHED

	def is_cyclic(self):
		# Initially all the vertices will have INITIAL state
		for i in range(self.nvertices):
			self.vertex_list[i].state = INITIAL
		
		DirectedGraph.has_cycle = False
		
		for v in range(self.nvertices):
			if self.vertex_list[v].state == INITIAL:
				self._dfs(v)

		return DirectedGraph.has_cycle

if __name__ == '__main__':
	
	d_graph = DirectedGraph()

	try:
		# Creating the graph, inserting the vertices and edges
		# Graph is acyclic
		# d_graph.insert_vertex("0")
		# d_graph.insert_vertex("1")
		# d_graph.insert_vertex("2")
		# d_graph.insert_vertex("3")

		# d_graph.insert_edge("0","1")
		# d_graph.insert_edge("0","2")
		# d_graph.insert_edge("0","3")
		# d_graph.insert_edge("1","2")
		# d_graph.insert_edge("3","2")

		# Graph is cyclic
		d_graph.insert_vertex("0")
		d_graph.insert_vertex("1")
		d_graph.insert_vertex("2")
		d_graph.insert_vertex("3")

		d_graph.insert_edge("0","1")
		d_graph.insert_edge("0","2")
		d_graph.insert_edge("1","2")
		d_graph.insert_edge("2","3")
		d_graph.insert_edge("3","0")

		# Display the graph
		d_graph.display()
		print()
		
		if d_graph.is_cyclic():
			print("Graph is Cyclic")
		else:
			print("Graph is Acyclic")
		
	except Exception as e:
		print(e)
		
