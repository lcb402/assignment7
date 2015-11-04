# This function generates a 10 x 3 array of random numbers in range [0,1]
# Then, the number closest to 0.5 in each row is output in a vector
import numpy as np

def my_nearest_half_vec():
	my_array = np.random.rand(10,3)
	best_near_half_sort = np.argsort(np.abs(my_array-0.5))
	best_near_half_idx = best_near_half_sort[:,0]
		
	best_near_half = []	
	for i in range(len(my_array)):
        	i_val = my_array[i][best_near_half_idx[i]]
        	best_near_half.append(i_val)
        print best_near_half
