import uproot as up
import matplotlib.pyplot as plt
import numpy as np
from optparse import OptionParser

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
	time = np.arange(np.max(hr)+1)
	time = time +0.5
	return time,freq

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f1", "--file1")
    parser.add_option("-f2", "--file2")
    parser.add_option("-f3", "--file3")
   
(options, args) = parser.parse_args()
file1 = options.file1
file2 = options.file2
file3 = options.file3

root1 = up.open(file1)
DT1 = root1["CalibTree"]["EventHeader."]["EventHeader.fDTms"].array()

root2 = up.open(file2)
DT2 = root2["CalibTree"]["EventHeader."]["EventHeader.fDTms"].array()

root3 = up.open(file3)
DT3 = root3["CalibTree"]["EventHeader."]["EventHeader.fDTms"].array()

time1,freq1 = eventrate(DT1)
time2,freq2 = eventrate(DT2)
time3,freq3 = eventrate(DT3)

plt.figure(1,clear='True')
plt.errorbar(time1,np.log(freq1),0,0.5,'bo')
plt.ylim(-5,0) 
plt.show()
