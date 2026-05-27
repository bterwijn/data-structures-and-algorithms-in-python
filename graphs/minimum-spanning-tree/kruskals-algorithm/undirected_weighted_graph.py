# undirected_weighted_graph.py : Program to create minimum spanning tree using Kruskal's algorithm.

NIL = -1

class Vertex:
	def __init__(self, name):
		self.name = name
		self.father = None

class Edge:
	def __init__(self, u, v, wt):
		self.u = u
		self.v = v
		self.wt = wt

class UndirectedWeightedGraph:
	def __init__(self, max_size=30):
		self.nvertices = 0
		self.nedges = 0
		self.adj = [ [0 for column in range(max_size)] for row in range(max_size) ]		
		self.vertex_list = []
		self.tree_edges = []

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
			self.adj[v][u] = weight
			self.nedges += 1
			
	def display(self):
		for i in range(self.nvertices):
			for j in range(self.nvertices):
				print(self.adj[i][j], end=" ")
			print()

	def _is_adjacent(self, u, v):
		return self.adj[u][v] != 0

	def _kruskals_algorithm(self):
		count = 0	# Number of edges in the tree
		edge_list = []
		
		# Inserting all the edges in edge_list
		for u in range(self.nvertices):
			for v in range(u,self.nvertices):
				if self._is_adjacent(u,v):
					edge_list.append( (u,v,self.adj[u][v]) )
		
		# Sorting the edge_list on weight
		edge_list = sorted(edge_list, key = lambda item: item[2], reverse = True)
	
		# Initialize the father of vertices to NIL
		for i in range(self.nvertices):
			self.vertex_list[i].father = NIL

		v1_root=NIL
		v2_root=NIL
		
		while len(edge_list)!=0 and count<self.nvertices-1:
			edge = edge_list.pop()
			v1 = edge[0]
			v2 = edge[1]

			while v1 != NIL:
				v1_root = v1
				v1 = self.vertex_list[v1].father
			
			while v2 != NIL:
				v2_root = v2
				v2 = self.vertex_list[v2].father
				
			if v1_root != v2_root:	# Include the edge in tree
				count += 1
				self.tree_edges.append(Edge(edge[0],edge[1],edge[2]))
				self.vertex_list[v2_root].father = v1_root
		
		if count < self.nvertices-1:
			raise Exception("Graph is not connected, spanning tree is not possible.")
		
	def minimum_spanning_tree(self):
		tree_weight = 0

		self._kruskals_algorithm()

		print("Minimum Spanning Tree Edges :")
		for e in self.tree_edges:
			print("Edge - (" + self.vertex_list[e.u].name + "-" + self.vertex_list[e.v].name + ")")
			tree_weight += self.adj[e.u][e.v]

		print("Minimum Spanning Tree Weight :", tree_weight)		

if __name__ == '__main__':

	uw_graph = UndirectedWeightedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		# Connected graph
		uw_graph.insert_vertex("0")
		uw_graph.insert_vertex("1")
		uw_graph.insert_vertex("2")
		uw_graph.insert_vertex("3")
		uw_graph.insert_vertex("4")
		uw_graph.insert_vertex("5")
		uw_graph.insert_vertex("6")
		uw_graph.insert_vertex("7")
		uw_graph.insert_vertex("8")

		uw_graph.insert_edge("0","1",9)
		uw_graph.insert_edge("0","3",4)
		uw_graph.insert_edge("0","4",2)
		uw_graph.insert_edge("1","2",10)
		uw_graph.insert_edge("1","4",8)
		uw_graph.insert_edge("2","4",7)
		uw_graph.insert_edge("2","5",5)
		uw_graph.insert_edge("3","4",3)
		uw_graph.insert_edge("3","6",18)
		uw_graph.insert_edge("4","5",6)
		uw_graph.insert_edge("4","6",11)
		uw_graph.insert_edge("4","7",12)
		uw_graph.insert_edge("4","8",15)
		uw_graph.insert_edge("5","8",16)
		uw_graph.insert_edge("6","7",14)
		uw_graph.insert_edge("7","8",20)

		# Not connected graph
		# uw_graph.insert_vertex("0")
		# uw_graph.insert_vertex("1")
		# uw_graph.insert_vertex("2")
		# uw_graph.insert_vertex("3")
		# uw_graph.insert_vertex("4")
		# uw_graph.insert_vertex("5")
		# uw_graph.insert_vertex("6")
		# uw_graph.insert_vertex("7")

		# uw_graph.insert_edge("0","1",6)
		# uw_graph.insert_edge("0","2",3)
		# uw_graph.insert_edge("0","3",8)
		# uw_graph.insert_edge("1","4",9)
		# uw_graph.insert_edge("2","3",7)
		# uw_graph.insert_edge("2","4",5)
		# uw_graph.insert_edge("3","4",4)

		# uw_graph.insert_edge("5","6",2)
		# uw_graph.insert_edge("5","7",8)
		# uw_graph.insert_edge("6","7",5)

		# Display the graph
		uw_graph.display()
		print()
		
		uw_graph.minimum_spanning_tree()
		
	except Exception as e:
		print(e)
		
