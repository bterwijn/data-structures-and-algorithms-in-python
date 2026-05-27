# insertion_sort.py : Program of sorting using insertion sort.

def insertion_sort(lst, n):
	for i in range(1,n):
		k = lst[i]
		j = i-1
		while j>=0 and lst[j]>k:
			lst[j+1] = lst[j]
			j -= 1
		lst[j+1] = k

if __name__ == '__main__':
	data_list = [82, 42, 49, 8, 25, 52, 36, 93, 59, 15]

	print("Unsorted list is :")
	print(data_list)

	insertion_sort(data_list,len(data_list))

	print("Sorted list is :")
	print(data_list)
