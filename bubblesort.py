def bubblesort( bad_list ):

	# List is assumed not to be sorted
	sorted = False 

	# multiple passes
	while not sorted: 

		# assume we are now done
		sorted = True 

		for i in range(0,len(bad_list)-1):
			if bad_list[i] > bad_list[i+1]:

				# Found 2 integers not sorted
				sorted = False

				tmp = bad_list[i]
				bad_list[i] = bad_list[i+1]
				bad_list[i+1] = tmp