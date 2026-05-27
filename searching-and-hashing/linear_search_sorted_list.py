# linear_search_sorted_list.py : Program of sequential search (linear search) in sorted list

def linear_search(lst, n, item):
	i=0
	while i<n and lst[i]<item:
		i += 1

	if i==n or lst[i] is not item:
		return -1
	else:
		return i

if __name__ == '__main__':
	data_list = [2, 9, 16, 19, 29, 36, 41, 67, 85, 96]
	item = 29
	
	index = linear_search(data_list, len(data_list), item)

	if index == -1:
		print(f"{item} not found in the list")
	else:
		print(f"{item} found at position {index}")
