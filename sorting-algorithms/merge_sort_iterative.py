# merge_sort_iterative.py : Program of sorting using merge sort without recursion.

# lst[low1]...lst[up1] and lst[low2]...lst[up2] merged to temp[low1]..temp[up2]
def merge(lst, temp, low1, up1, low2, up2):
	i = low1
	j = low2
	k = low1

	while i<=up1 and j<=up2:
		if lst[i] < lst[j]:
			temp[k] = lst[i]
			i += 1
		else:
			temp[k] = lst[j]
			j += 1
		k += 1

	while i <= up1:
		temp[k] = lst[i]
		k += 1
		i += 1
	
	while j <= up2:
		temp[k] = lst[j]
		k += 1
		j += 1

# copies temp[low]....temp[up] to lst[low]...lst[up]
def copy(lst, temp, n):
	for i in range(n):
		lst[i] = temp[i]
	
def merge_pass(lst, temp, size, n):
	low1 = 0
	
	while low1+size <= n-1:
		up1 = low1 + size - 1
		low2 = low1 + size
		up2 = low2 + size - 1
		if up2 >= n:	# if length of last sublist is less than size
			up2 = n-1
		merge(lst,temp,low1,up1,low2,up2)
		low1 = up2 + 1	# Take next two sublists for merging

	for i in range(low1,n):
		temp[i] = lst[i]	# If any sublist is left alone

	copy(lst,temp,n)

def merge_sort(lst, n):
	temp = [None]*(len(lst))
	size = 1

	while size < n:
		merge_pass(lst,temp,size,n)
		size = size*2

if __name__ == '__main__':
	data_list = [8, 5, 89, 30, 42, 92, 64, 4, 21, 56, 3]

	print("Unsorted list is :")
	print(data_list)

	merge_sort(data_list,len(data_list))

	print("Sorted list is :")
	print(data_list)
