# heap_sort.py : Program of sorting using heap sort.

def restore_down(i, lst, n):
	k = lst[i]
	lchild = 2*i
	rchild = lchild+1

	while rchild <= n:
		if k>=lst[lchild] and k>=lst[rchild]:
			lst[i] = k
			return
		elif lst[lchild] > lst[rchild]:
			lst[i] = lst[lchild]
			i = lchild
		else:
			lst[i] = lst[rchild]
			i = rchild

		lchild = i*2
		rchild = lchild+1

	# If number of nodes is even
	if lchild==n and k<lst[lchild]:
		lst[i] = lst[lchild]
		i = lchild

	lst[i] = k

def build_heap_bottom_up(lst, n):
	i = n//2
	while i>=1:
		restore_down(i,lst,n);
		i -= 1

def heap_sort(lst, n):
	build_heap_bottom_up(lst,n)

	print("Heap is :")
	for i in range(1,len(lst)):
		print(f"{lst[i]} ",end='')
	print()

	# deleting the root and moving it(max_value) to lst[n]
	while n > 1:
		max_value = lst[1]
		lst[1] = lst[n]
		lst[n] = max_value
		n -= 1
		restore_down(1,lst,n)

		print("Heap is :")
		for i in range(1,len(lst)):
			print(f"{lst[i]} ",end='')
		print()

if __name__ == '__main__':
	data_list = [9999, 25, 35, 18, 9, 46, 70, 48, 23, 78, 12, 95] # data is from data_list[1]
	n = 11 # data is from data_list[1]...data_list[11]

	print("Unsorted list is :")
	for i in range(1,len(data_list)):
		print(f"{data_list[i]} ",end='')
	print()

	heap_sort(data_list,n)

	print("Sorted list is :")
	for i in range(1,len(data_list)):
		print(f"{data_list[i]} ",end='')
	print()
