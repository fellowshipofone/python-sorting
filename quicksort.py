from math import ceil

def quicksort( bad_list, left=0, right=None ):

    # Set right index if not set
    if right is None:
        right = len(bad_list) -1

    # Handle the case where subset are empty
    if left == right:
        return

    # Set pivot index
    pivot = left + int(ceil((right-left) / 2 ))

    # Partition
    pivot = partition( bad_list, left, right, pivot )

    # Quicksort
    if pivot > left:
        quicksort(bad_list, left, pivot-1)
    if pivot < right:
        quicksort(bad_list, pivot+1, right)


def partition( bad_list, left, right, pivot ):

    store_i = left
    swap(bad_list, pivot, right)
    pivot = right
    for i in range(left,right):
        if bad_list[i] <= bad_list[pivot]:
            swap(bad_list, store_i, i)
            store_i += 1

    if store_i < right:
        swap(bad_list, pivot, store_i)
    return store_i


def swap( l, i1, i2 ):

    tmp = l[i2]
    l[i2] = l[i1]
    l[i1] = tmp
