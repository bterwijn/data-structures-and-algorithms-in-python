# build_heap.py : Program to build the heap.

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
	while i >= 1:
		restore_down(i, lst, n)
		i -= 1

def restore_up(i, lst):
	k = lst[i]
	i_parent = i//2

	while lst[i_parent] < k:
		lst[i] = lst[i_parent]
		i = i_parent
		i_parent = i//2

	lst[i] = k

def build_heap_top_down(lst, n):
	i = 2
	while i <= n:
		restore_up(i, lst)
		i += 1
	
if __name__ == '__main__':
	list1 = [9999, 25, 35, 18, 9, 46, 70, 48, 23, 78, 12, 95]
	n1 = len(list1)-1

	print("Building Heap Botton Up :")
	build_heap_bottom_up(list1, n1)

	i = 1
	while i <= n1:
		print(f"{list1[i]} ", end='')
		i += 1
	print()

	list2 = [9999, 25, 35, 18, 9, 46, 70, 48, 23, 78, 12, 95]
	n2 = len(list2)-1

	print("Building Heap Top Down :")
	build_heap_top_down(list2, n2)

	i = 1
	while i <= n2:
		print(f"{list2[i]} ", end='')
		i += 1
	print()
