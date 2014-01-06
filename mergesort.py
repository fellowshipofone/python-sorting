from math import floor

def mergesort( bad_list ):

    if len(bad_list) <= 1:
        return bad_list

    pivot = int(floor(len(bad_list) / 2))

    left_list = mergesort(bad_list[:pivot])
    right_list = mergesort(bad_list[pivot:])

    for i in range(0, len(bad_list)):

        if len(right_list) <= 0 or (len(left_list) > 0 and left_list[0] <= right_list[0]):
            bad_list[i] = left_list.pop(0)
        else:
            bad_list[i] = right_list.pop(0)

    return bad_list