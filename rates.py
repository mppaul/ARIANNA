import uproot as up
import numpy as np
import matplotlib.pyplot as plt
import sys

file = up.open(sys.argv[1])
print "Root File Opened"

DT = np.array(file["CalibTree"]["EventHeader."]["EventHeader.fDTms"].array())/1000.0
print "Data Loaded"

t = []
add = 0
for i in range(len(DT)):
	add += DT[i]
	t.append(add)

DT = np.array(t)/3600.0

bins = float(sys.argv[2])

rates = []
for j in range(int(DT[-1]/bins)):
	add = 0
	for k in range(len(DT)):
		if DT[k] >= bins*j and DT[k] < bins*(j+1):
			add += 1
	rates.append(add)

rates = np.array(rates)/3600.0
time = np.array(range(int(DT[-1]/bins)))*bins +bins/2.0
print "Rates Computed"

print "Ploting..."
f,ax = plt.subplots()
plt.errorbar(time,rates, 0, bins/2.0, "b+")
ax.set_yscale('log')
plt.ylim(10e-3,10e1)
plt.ylabel("Rate Frequency [Hz]")
plt.xlabel("Time [Hr]")
plt.show()


