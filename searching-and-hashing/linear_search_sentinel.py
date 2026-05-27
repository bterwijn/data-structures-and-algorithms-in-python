# linear_search_sentinel.py : Program of sequential search (linear search) using sentinel in a list.

def linear_search(lst, n, item):
	lst.append(item) # item at nth location

	i = 0
	while lst[i] is not item:
		i += 1

	if i < n:
		return i
	else:
		return -1

if __name__ == '__main__':
	data_list = [96, 19, 85, 9, 16, 29, 2, 36, 41, 67]

	item = 29
	
	index = linear_search(data_list, len(data_list), item)	

	if index == -1:
		print(f"{item} not found in the list")
	else:
		print(f"{item} found at position {index}")
