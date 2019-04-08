
import numpy as np
import scipy
import json
import sys
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy.polynomial.polynomial import polyfit
import re


def array_generator():
	if sys.argv[1].endswith('.csv'):
		data = np.genfromtxt(sys.argv[1], dtype=None, delimiter=",")
		d = {}
		dim = data.shape
		CH = ["CH0", "CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7"]
		col = [0, 4, 8, 12, 16, 20, 24, 28]
		for l in range(8):
			ind = []
			for i in range(dim[0]):
				if data[i][col[l]] == CH[l]:
                    			d[data[i][col[l]]] = {}
                		if data[i][col[l]] == "PG Value":
                    			d[CH[l]][data[i][col[l] + 2][5:]] = {}
                    			d[CH[l]][data[i][col[l] + 2][5:]][data[i][col[l]]] = []
                    			d[CH[l]][data[i][col[l] + 2][5:]][data[i][col[l] + 1]] = []
                    			d[CH[l]][data[i][col[l] + 2][5:]]["Frequency"] = []
                    			ind.append(i)

            		for j in range(len(ind)):
                		if ind[j] == ind[-1]:
                			end = dim[0]
                		else:
                    			end = ind[j + 1]

                		for k in range(ind[j] + 1, end):
                    			if any(np.core.defchararray.startswith(data[k][col[l]], ["-", '1', '2', '3', '4', '5', '6', '7', '8', '9'])) == False:
                        			break
                    			d[CH[l]][data[ind[j]][col[l] + 2][5:]][data[ind[j]][col[l]]].append(float(data[k][col[l]]))
                    			d[CH[l]][data[ind[j]][col[l] + 2][5:]][data[ind[j]][col[l] + 1]].append(float(data[k][col[l] + 1]))
                    			d[CH[l]][data[ind[j]][col[l] + 2][5:]]["Frequency"].append(float(data[k][col[l] + 2]))

        	with open("data.json", 'w') as outfile:
            		json.dump(d, outfile, sort_keys=True, indent=4)
        	data = d

	if sys.argv[1].endswith('.json'):
        	with open(sys.argv[1], 'r') as fin:
        		data = json.load(fin)
        #for chan in data:
        #     for thres in data[chan]:
        #         plt.plot(data[chan][thres]["SCOPE"], data[chan][thres]["Frequency"])

	return data

def thresh_calib_calc():
	data = array_generator()

    	CH = ["CH0", "CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7"]
    	VOL1 = ["30mV", "45mV", "60mV", "80mV", "120mV", "150mV", "200mV", "300mV","-30mV", "-45mV", "-60mV", "-80mV", "-120mV", "-150mV", "-200mV", "-300mV"]

    	def fsigmoid(x, a, b):
        	y = 1000.0 / (1 + np.exp(-b * (x - a)))  # generates sigmoid for comparison
        	return y

    	def ifsigmoid(y, a, b):
		x = (-1/b) * np.log((1000.0/y) - 1) + a
		return x

    	def linear(x, y):
		m, b = np.polyfit(x, y, 1)
		return m, b

    	lst = {}
    	for ch in CH:
		lst[ch] = {}
        	linear_plotx = []
        	linear_ploty = []
        	for vol in VOL1:
            		scope = data[ch][vol]["SCOPE"]
            		frequency = data[ch][vol]["Frequency"]
	
            		popt, pcov = curve_fit(fsigmoid, scope, frequency, p0=[int(scope[len(scope)/2 - 1]), 1])
	    		thres_val = ifsigmoid(500.0, *popt)

	    		'''
            		xfin = np.linspace(scope[0], scope[len(scope) - 1], 100)  
            		yfin = fsigmoid(xfin, *popt)
	    		plt.plot(xfin, yfin)
	   		plt.plot(scope, frequency)
	    		plt.plot(thres_val, 500, 'bo')	
	    		plt.show()
	    		'''

	    		linear_ploty.append(thres_val)
	    		linear_plotx.append(int(vol[0:-2]))

		linear_plotx = (np.array(linear_plotx) + 900)/0.03816
	
		# Positive Threshold Calculation
		m,b = linear(linear_plotx[:8], np.array(linear_ploty)[:8])
		lst[ch]["High"] = [m, b]
	
		'''
		dacs = np.linspace(linear_plotx[0], linear_plotx[7], 100)
		plt.plot(linear_plotx[:8], np.array(linear_ploty)[:8], 'bo')
		plt.plot(dacs, m*dacs + b)
		plt.show()
		'''
	
		# Negative Threshold Calculation
		m,b = linear(linear_plotx[8:], np.array(linear_ploty)[8:])
		lst[ch]["Low"] = [m, b]	

		'''
		dacs = np.linspace(linear_plotx[15], linear_plotx[8], 100)
		plt.plot(linear_plotx[8:], np.array(linear_ploty)[8:], 'bo')
		plt.plot(dacs, m*dacs + b)
		plt.show()
		'''

	return lst

thres_calib = thresh_calib_calc()

print "    0: {'high': {'b': %g, 'm': %f}," % (thres_calib["CH0"]["High"][1], thres_calib["CH0"]["High"][0])
print "        'low': {'b': %g, 'm': %f}}," % (thres_calib["CH0"]["Low"][1], thres_calib["CH0"]["Low"][0])
print "    1: {'high': {'b': %g, 'm': %f}," % (thres_calib["CH1"]["High"][1], thres_calib["CH1"]["High"][0])
print "        'low': {'b': %g, 'm': %f}}," % (thres_calib["CH1"]["Low"][1], thres_calib["CH1"]["Low"][0])
print "    2: {'high': {'b': %g, 'm': %f}," % (thres_calib["CH2"]["High"][1], thres_calib["CH2"]["High"][0])
print "        'low': {'b': %g, 'm': %f}}," % (thres_calib["CH2"]["Low"][1], thres_calib["CH2"]["Low"][0])
print "    3: {'high': {'b': %g, 'm': %f}," % (thres_calib["CH3"]["High"][1], thres_calib["CH3"]["High"][0])
print "        'low': {'b': %g, 'm': %f}}," % (thres_calib["CH3"]["Low"][1], thres_calib["CH3"]["Low"][0])
print "    4: {'high': {'b': %g, 'm': %f}," % (thres_calib["CH4"]["High"][1], thres_calib["CH4"]["High"][0])
print "        'low': {'b': %g, 'm': %f}}," % (thres_calib["CH4"]["Low"][1], thres_calib["CH4"]["Low"][0])
print "    5: {'high': {'b': %g, 'm': %f}," % (thres_calib["CH5"]["High"][1], thres_calib["CH5"]["High"][0])
print "        'low': {'b': %g, 'm': %f}}," % (thres_calib["CH5"]["Low"][1], thres_calib["CH5"]["Low"][0])
print "    6: {'high': {'b': %g, 'm': %f}," % (thres_calib["CH6"]["High"][1], thres_calib["CH6"]["High"][0])
print "        'low': {'b': %g, 'm': %f}}," % (thres_calib["CH6"]["Low"][1], thres_calib["CH6"]["Low"][0])
print "    7: {'high': {'b': %g, 'm': %f}," % (thres_calib["CH7"]["High"][1], thres_calib["CH7"]["High"][0])
print "        'low': {'b': %g, 'm': %f}}," % (thres_calib["CH7"]["Low"][1], thres_calib["CH7"]["Low"][0])



