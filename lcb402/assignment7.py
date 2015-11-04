# Author: Laura Buchanan
# NetID: lcb402

import numpy as np
import matplotlib.pyplot as plt
import question2
import question3
import question4

# 1. Create array
print "Question 1:"
try:
	my_array = np.arange(1,16).reshape(5,3)
	print my_array
except: 
	print "Oops, something wrong with Question 1!"

# 1.a.
print "Question 1a:"
try:
	array_row_2_n_4 = np.vstack([my_array[1],my_array[3]])
	print array_row_2_n_4
except:
	print "Oops, something wrong with Question 1a!"

# 1.b.
print "Question 1b:"
try:
	array_col_2 = my_array[:,1]
	print array_col_2
except:
	print "Oops, something wrong with Question 1b!"

# 1.c.
print "Question 1c:"
try:
	array_rec = my_array[[[3],[1]],[1,0]]
	print array_rec
except: 
	print "Oops, something wrong with Question 1c!"

# 1.d.
print "Question 1d:"
try:
	array_3_to_11 = my_array[(3 < my_array) & (my_array < 11)]
	print array_3_to_11
except:
	print "Oops, something wrong with Question 1d!"

# 2.
print "Question 2:" 
try: 
	a = np.arange(25).reshape(5,5)
	b = np.array([1.,5,10,15,20]) 
	question2.my_divide(a,b)
except:
	print "Oops, something wrong with Question 2!"

# 3. 
print "Question 3:" 
try:
	question3.my_nearest_half_vec()
except:
	print "Oops, something wrong with Question 3!"

# 4.
print "Question 4:"
try:
	question4.my_mandelbrot_fractal()
	print "Check out mandelbrot.png!"
except: 
	print "Oops, something wrong with Question 4!"
