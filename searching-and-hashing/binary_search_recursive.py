# binary_search_recursive.py : Program of recursive binary search in a list.

def rbinary_search1(lst, low, up, item):
	if low > up:
		return -1

	mid = (low+up)//2

	if item > lst[mid]:		# Search in right half
		return rbinary_search1(lst, mid+1, up, item)
	elif item < lst[mid]:	# Search in left half
		return rbinary_search1(lst, low, mid-1, item)
	else:
		return mid

def rbinary_search(lst, n, item):
	return rbinary_search1(lst, 0, n-1, item)

if __name__ == '__main__':
	data_list = [2, 9, 16, 19, 29, 36, 41, 67, 85, 96]
	item = 29

	index = rbinary_search(data_list, len(data_list), item)

	if index == -1:
		print(f"{item} not found in the list")
	else:
		print(f"{item} found at position {index}")
