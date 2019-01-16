import sys
import numpy as np
import matplotlib.pyplot as plt

file1 = np.genfromtxt(sys.argv[1], delimiter=',')

data = []
time = []

for i in range(len(file1)-2):
	data.append(file1[i+2][1])
	time.append(file1[i+2][0])

data = np.array(data)
time = np.array(time)

print time[1]-time[0]

freq = np.fft.rfftfreq(len(data), d=time[1]-time[0])
freq_data = np.abs(np.fft.rfft(data, norm="ortho"))



plt.subplot(211)
plt.plot(time*1e6, data*1000)
plt.xlabel("Time [us]")
plt.ylabel("Voltage [mV]")


plt.subplot(212)
plt.plot(freq[20:]/1e9,freq_data[20:])
plt.xlabel("Frequency [GHz]")

plt.show()

