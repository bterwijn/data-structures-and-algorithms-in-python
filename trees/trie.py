# trie.py : Program to implement trie.

class Node:
	def __init__(self):
		self._MAX_SIZE = 26
		self.links = [None] * self._MAX_SIZE # links to the child node
		self.eok = False # end of key
	
		for i in range(0, self._MAX_SIZE):
			self.links[i] = None

class Trie:
	def __init__(self):
		self._MAX_SIZE = 26
		self._root = Node()

	def insert(self, key):
		p = self._root

		for i in range(len(key)):
			# If letter of key is not there
			if p.links[ord(key[i])-ord('a')] is None:
				p.links[ord(key[i])-ord('a')] = Node()

			p = p.links[ord(key[i])-ord('a')] # Move to the next child node
		p.eok = True	# end of key
	
	def search(self, key):
		p = self._root

		for i in range(0, len(key)):
			if p.links[ord(key[i])-ord('a')] is None:
				# key is not in the Trie
				return False

			p = p.links[ord(key[i])-ord('a')] # Move to the next child node

		return p.eok
	
	def starts_with(self, prefix):
		p = self._root

		for i in range(0, len(prefix)):
			if p.links[ord(prefix[i])-ord('a')] is None:
				# No prefix
				return False

			p = p.links[ord(prefix[i])-ord('a')] # Move to the next child node

		# prefix found
		return True
	
	def _display(self, p, prefix):
		if p.eok:
			print(prefix)

		for i in range(0, self._MAX_SIZE):
			if p.links[i] is not None:
				self._display(p.links[i], prefix+chr(ord('a')+i))

	def display(self):
		key_str = ""
		self._display(self._root, key_str)
	
	def del_key(self, key):
		p = self._root

		for i in range(0,len(key)):
			if p.links[ord(key[i])-ord('a')] is None:
				print("key is not in the Trie")
				return
			p = p.links[ord(key[i])-ord('a')] # Move to the next child node

		if p.eok == False:
			print("key is not in the Trie")
		else:
			p.eok = False

if __name__ == '__main__':
	trie = Trie()

	trie.insert("lucknow")
	trie.insert("lucknowcity")
	trie.insert("luxembourg")
	trie.insert("lux")
	
	# Search in trie
	print("search(\"lucknowp\") : " + str(trie.search("lucknowp")))

	print("search(\"luxembourg\") : " + str(trie.search("luxembourg")))

	# Prefix in trie
	print("starts_with(\"luxe\") : " + str(trie.starts_with("luxe")))

	print("Trie keys are :")
	trie.display()

	# Deletion of key in trie
	trie.del_key("luxembourg")

	print("After deleting luxembourg, trie keys are :")
	trie.display()
