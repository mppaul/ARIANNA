import sys
import numpy as np

file = np.genfromtxt(sys.argv(1), delimiter=',')
data, time = [], []


for i in range(len(file)-2):
	data.append(file[i+2][1])


