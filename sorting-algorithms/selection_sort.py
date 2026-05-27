# selection_sort.py : Program of sorting using selection sort.

def selection_sort(lst, n):
	for i in range(n-1):
		# Find the index of smallest element
		min = i
		for j in range(i+1,n):
			if lst[min] > lst[j]:
				min = j

		if i != min:
			lst[i],lst[min] = lst[min],lst[i]

if __name__ == '__main__':
	data_list = [82, 42, 49, 8, 25, 52, 36, 93, 59, 15]

	print("Unsorted list is :")
	print(data_list)

	selection_sort(data_list,len(data_list))

	print("Sorted list is :")
	print(data_list)
