# shell_sort.py : Program of sorting using shell sort.

def shell_sort(lst, n):
	incr = 5 # maximum increment (odd value)
	
	while incr >= 1:
		for i in range(incr,n):
			k=lst[i]
			
			j = i-incr
			while j>=0 and k<lst[j]:
				lst[j+incr] = lst[j]
				j = j-incr
			lst[j+incr] = k

		incr=incr-2;	# Decrease the increment

if __name__ == '__main__':
	data_list = [19, 63, 2, 6, 7, 10, 1, 18, 9, 4, 45, 3, 5, 17, 16, 12, 56]

	print("Unsorted list is :")
	print(data_list)

	shell_sort(data_list,len(data_list))

	print("Sorted list is :")
	print(data_list)
