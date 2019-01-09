import uproot as up
import matplotlib.pyplot as plt
import numpy as np

def eventrate(DT):
	total = 0
	sec = [] 
	for i in range(len(DT)):
		total += DT[i]/3600000.0
		sec.append(total)

	hr = []
	for i in range(len(sec)):
		hr.append(int(sec[i]))
	plt.figure(1)
	bins = range(np.max(hr)+2)
	histo = plt.hist(hr,bins)
	freq = histo[0]/3600.0
	print histo[0]
	time = np.arange(np.max(hr)+1)
	time = time +0.5
	return time,freq

file = up.open("CalTree.raw.root")
DT = file["CalibTree"]["EventHeader."]["EventHeader.fDTms"].array()

time1,freq1 = eventrate(DT)

plt.figure(1,clear='True')
plt.errorbar(time1,freq1,0,0.5,'bo')
#plt.ylim(0,1) 
plt.show()
