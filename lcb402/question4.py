import numpy as np
import matplotlib.pyplot as plt


# This class assigns the parameters that we want to use in our Mandelbrot iteration
class my_mandelbrot(): 
	def __init__(self):
		self.N_max = 50
		self.some_threshold = 50
		self.x_min = -2
		self.x_max = 1
		self.y_min = -1.5
		self.y_max = 1.5


# This function does the appropriate iteration and plots the Mandelbrok fractal
def my_mandelbrot_fractal():
	fractal = my_mandelbrot()
	fractal.x_line = np.linspace(fractal.x_min,fractal.x_max,1000)
	fractal.y_line = np.linspace(fractal.y_min,fractal.y_max,1000)
	fractal.x_grid,fractal.y_grid = np.meshgrid(fractal.x_line,fractal.y_line)
	fractal.xy_grid = fractal.x_grid + 1j*fractal.y_grid
	fractal.xy_grid
	
	c = fractal.xy_grid
	z = c
	np.seterr(all='ignore')
	for v in range(fractal.N_max):
		z = z**2 + c
	mask = np.abs(z) < fractal.some_threshold

	plt.imshow(mask, extent=[-2, 1, -1.5, 1.5])
	plt.gray()
	plt.savefig('mandelbrot.png')
