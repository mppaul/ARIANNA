import numpy as np 
import scipy
import json
import sys
import matplotlib.pyplot as plt

if sys.argv[1].endswith('.csv'):
	data = np.genfromtxt(sys.argv[1], dtype=None,  delimiter=",")
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
				d[CH[l]][data[i][col[l]+2][5:]] = {}
				d[CH[l]][data[i][col[l]+2][5:]][data[i][col[l]]] = []
				d[CH[l]][data[i][col[l]+2][5:]][data[i][col[l]+1]] = []
				d[CH[l]][data[i][col[l]+2][5:]]["Frequency"] = []
				ind.append(i)
		
		for j in range(len(ind)):
			if ind[j] == ind[-1]:
				end = dim[0]		
			else:
				end = ind[j+1]
			
			for k in range(ind[j]+1,end):
				if any(np.core.defchararray.startswith(data[k][col[l]],["-",'1','2','3','4','5','6','7','8','9'])) == False:
					break
				d[CH[l]][data[ind[j]][col[l]+2][5:]][data[ind[j]][col[l]]].append(float(data[k][col[l]]))
				d[CH[l]][data[ind[j]][col[l]+2][5:]][data[ind[j]][col[l]+1]].append(float(data[k][col[l]+1]))
				d[CH[l]][data[ind[j]][col[l]+2][5:]]["Frequency"].append(float(data[k][col[l]+2]))
	
	with open("data.json", 'w') as outfile:
		json.dump(d, outfile, sort_keys=True, indent=4)
	data = d

if sys.argv[1].endswith('.json'):
	with open(sys.argv[1], 'r') as fin:
		data = json.load(fin)


for chan in data:
	for thres in data[chan]:
		plt.plot(data[chan][thres]["SCOPE"], data[chan][thres]["Frequency"])
		
	
