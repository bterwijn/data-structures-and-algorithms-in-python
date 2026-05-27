# bubble_sort.py : Program of sorting using bubble sort.

def bubble_sort(lst, n):
	for i in range(n-1):
		xchanges = 0;
		for j in range(n-1-i):
			if lst[j] > lst[j+1]:
				lst[j],lst[j+1] = lst[j+1],lst[j]
				xchanges += 1

		if xchanges == 0: # If list is sorted
			break

if __name__ == '__main__':
	data_list = [40, 20, 50, 60, 30, 10, 90, 97, 70, 80]

	print("Unsorted list is :")
	print(data_list)

	bubble_sort(data_list,len(data_list))

	print("Sorted list is :")
	print(data_list)
