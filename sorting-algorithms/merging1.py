# merging1.py : Program of merging two sorted lists of a list into another list.

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

	while i<=up1:
		temp[k] = lst[i]
		k += 1
		i += 1
	
	while j<=up2:
		temp[k] = lst[j]
		k += 1
		j += 1

if __name__ == '__main__':
	data_list = [5,8,9,28,34, 4,22,25,30,33,40,42]

	temp = [None]*(len(data_list))

	print("List is :")
	print(data_list)

	merge(data_list,temp,0,4, 5,11)

	print("Merged list :")
	print(temp)
