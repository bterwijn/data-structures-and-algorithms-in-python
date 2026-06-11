# merge_sort_recursive.py

def merge(lst, temp, low1, up1, low2, up2):
    i = low1
    j = low2
    k = low1

    while i <= up1 and j <= up2:
        if lst[i] < lst[j]:
            temp[k] = lst[i]
            i += 1
        else:
            temp[k] = lst[j]
            j += 1
        k += 1

    while i <= up1:
        temp[k] = lst[i]
        i += 1
        k += 1

    while j <= up2:
        temp[k] = lst[j]
        j += 1
        k += 1


def copy(lst, temp, low, up):
    for i in range(low, up + 1):
        lst[i] = temp[i]


def merge_sort1(lst, temp, low, up):
    if low >= up:
        return

    mid = (low + up) // 2

    merge_sort1(lst, temp, low, mid)
    merge_sort1(lst, temp, mid + 1, up)

    merge(lst, temp, low, mid, mid + 1, up)
    copy(lst, temp, low, up)


def merge_sort(lst):
    temp = [None] * len(lst)
    merge_sort1(lst, temp, 0, len(lst) - 1)


if __name__ == "__main__":
    data_list = [8, 5, 89, 30, 42, 92, 64, 4, 21, 56, 3]

    print("Unsorted list is:")
    print(data_list)

    merge_sort(data_list)

    print("Sorted list is:")
    print(data_list)
