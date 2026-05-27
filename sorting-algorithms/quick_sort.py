# quick_sort.py : Program of sorting using quick sort.

def partition(lst, low, up):
	pivot = lst[low]

	i = low+1		# moves from left to right
	j = up			# moves from right to left

	while i <= j:
		while lst[i]<pivot and i<up:
			i += 1
		
		while lst[j] > pivot:
			j -= 1
		
		if i < j:	# swap lst[i] and lst[j]
			lst[i],lst[j] = lst[j],lst[i]
			i += 1
			j -= 1
		else:	# found proper place for pivot
			i += 1

	# Proper place for pivot is j
	lst[low] = lst[j]
	lst[j] = pivot
	
	return j

# Recursive function quick_sort1()
def quick_sort1(lst, low, up):
	if low >= up:
		return

	pivotloc = partition(lst,low,up)
	quick_sort1(lst,low,pivotloc-1)	# process left sublist
	quick_sort1(lst,pivotloc+1,up)	# process right sublist

def quick_sort(lst, n):
	quick_sort1(lst, 0, n-1)

if __name__ == '__main__':
	data_list = [48, 44, 19, 59, 72, 80, 42, 65, 82, 8, 95, 68]

	print("Unsorted list is :")
	print(data_list)

	quick_sort(data_list,len(data_list))

	print("Sorted list is :")
	print(data_list)
