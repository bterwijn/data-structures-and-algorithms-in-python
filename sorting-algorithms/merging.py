# merging.py : Program of merging two sorted lists into a third sorted list.

def merge(list1, list2, temp, n1, n2):
	i = 0	# Index for first list
	j = 0	# Index for second list
	k = 0	# Index for merged list

	while i<=n1-1  and j<=n2-1:
		if list1[i] < list2[j]:
			temp[k] = list1[i]
			i += 1
		else:
			temp[k] = list2[j]
			j += 1
		
		k += 1

	# Put remaining elements of list1 into temp
	while i <= n1-1:
		temp[k] = list1[i]
		k += 1
		i += 1
	
	# Put remaining elements of arr2 into temp
	while j <= n2-1:
		temp[k] = list2[j]
		k += 1
		j += 1

if __name__ == '__main__':
	data_list1 = [5, 8, 9, 28, 34]
	data_list2 = [4, 22, 25, 30, 33, 40, 42]

	temp = [None] * (len(data_list1) + len(data_list2))

	print("List 1 in sorted order :")
	print(data_list1)
	print("List 2 in sorted order :")
	print(data_list2)

	merge(data_list1,data_list2,temp,len(data_list1),len(data_list2))

	print("Merged list :")
	print(temp)
