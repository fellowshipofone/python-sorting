import random
import time
from bubblesort import bubblesort
from quicksort import quicksort
from mergesort import mergesort

def checkSorted(a):
    for i in xrange(1, len(a) - 1):
        if a[i] < a[i-1]:
            print "%d >= %d" % (a[i], a[i-1])
            return False
    return True

def main():

    algos = {"QuickSort": quicksort, "BubbleSort": bubblesort, "MergeSort": mergesort}




    for name,method in algos.iteritems():

        # Test algorithm
        num_values = 1000
        bad_list = [int(num_values*random.random()) for i in xrange(num_values)]
        method( bad_list )
        if not checkSorted(bad_list):
            print bad_list
            exit(name + " algorithm does not work")



    num_values = 5000

    bad_list_random = [int(num_values*random.random()) for i in xrange(num_values)]
    bad_list_sorted = [i for i in xrange(num_values)]
    bad_list_sorted.sort()
    bad_list_reverse = [i for i in xrange(num_values)]
    bad_list_reverse.sort(reverse=True)

    print "List of %d items" % len(bad_list_random)

    for name,method in algos.iteritems():


        # Random
        bad_list = list(bad_list_random)
        start_time = time.time()
        method( bad_list )
        duration = time.time() - start_time
        print name + " Random (" + str(num_values) + ") in " + str(duration) + " seconds"

        # Sorted
        bad_list = list(bad_list_sorted)
        start_time = time.time()
        method( bad_list )
        duration = time.time() - start_time
        print name + " Sorted (" + str(num_values) + ") in " + str(duration) + " seconds"

        # Reverse
        bad_list = list(bad_list_reverse)
        start_time = time.time()
        method( bad_list )
        duration = time.time() - start_time
        print name + " Reverse (" + str(num_values) + ") in " + str(duration) + " seconds"

        print

if __name__ == "__main__":
    main()

