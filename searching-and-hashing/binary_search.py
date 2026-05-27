# binary_search.py : Program of binary search in a list.

def binary_search(lst, n, item):
	low = 0
	up = n-1

	while low <= up:
		mid = (low+up)//2
		if item > lst[mid]:
			low = mid+1		# Search in right half
		elif item < lst[mid]:
			up = mid-1		# Search in left half
		else:
			return mid

	return -1

if __name__ == '__main__':
	data_list = [2, 9, 16, 19, 29, 36, 41, 67, 85, 96]
	item = 29

	index = binary_search(data_list, len(data_list), item)

	if index == -1:
		print(f"{item} not found in the list")
	else:
		print(f"{item} found at position {index}")
