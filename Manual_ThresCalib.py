import numpy as np 
import json
import sys

#Open CSV file with raw manual threshold data

data = np.genfromtxt(sys.argv[1], dtype=None,  delimiter=",")
d = {}
dim = data.shape
CH = ["CH0", "CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7"]
col = [0, 4, 8, 12, 16, 20, 24, 28]

#for k in range(len(CH))
ind = []
for i in range(dim[0]):
	if data[i][col[0]] == CH[0]:
		d[data[i][col[0]]] = {}
	if data[i][0] == "PG Value":
		d[CH[col[0]]][data[i][col[0]+2][5:]] = {}
		d[CH[col[0]]][data[i][col[0]+2][5:]][data[i][col[0]]] = []
		d[CH[col[0]]][data[i][col[0]+2][5:]][data[i][col[0]+1]] = []
		d[CH[col[0]]][data[i][col[0]+2][5:]]["Frequency"] = []
		ind.append(i)
	
for j in range(len(ind)):
	if ind[j] == ind[-1]:
		end = dim[0]
			
	else:
		end = ind[j+1]
	
	for k in range(ind[j]+1,end):			 
		d[CH[col[0]]][data[ind[j]][col[0]+2][5:]][data[ind[j]][col[0]]].append(float(data[k][col[0]]))
		d[CH[col[0]]][data[ind[j]][col[0]+2][5:]][data[ind[j]][col[0]+1]].append(float(data[k][col[0]+1]))
		d[CH[col[0]]][data[ind[j]][col[0]+2][5:]]["Frequency"].append(float(data[k][col[0]+2]))

with open("data.json", 'w') as outfile:
	json.dump(d, outfile, sort_keys=True, indent=4)
