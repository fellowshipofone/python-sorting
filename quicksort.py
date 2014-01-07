from math import ceil

def quicksort( bad_list, left=0, right=None ):
    """ Quick sort bad_list, in-place
    """

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

    # Quicksort recursively
    if pivot > left:
        quicksort(bad_list, left, pivot-1)
    if pivot < right:
        quicksort(bad_list, pivot+1, right)


def partition( bad_list, left, right, pivot ):
    """ Partition a list in 2 with item smaller than pivot and the others
    """

    # Initialize the writing index
    store_i = left

    # Keep the pivot to the right
    swap(bad_list, pivot, right)
    pivot = right

    # Check all items against the pivot...
    for i in range(left,right):
        if bad_list[i] <= bad_list[pivot]:
            # ... and move them to the storing index if smaller
            swap(bad_list, store_i, i)
            store_i += 1

    # Restore the pivot between smaller and bigger itmes
    if store_i < right:
        swap(bad_list, pivot, store_i)

    # Return new pivot (index)
    return store_i


def swap( l, i1, i2 ):
    """ Swap 2 items in a list
    """

    tmp = l[i2]
    l[i2] = l[i1]
    l[i1] = tmp
