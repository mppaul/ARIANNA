import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

file1 = np.genfromtxt(sys.argv[1], delimiter=',')

data, time = [], []

for i in range(len(file1)-2):
	data.append(file1[i+2][1])
	time.append(file1[i+2][0])

data = np.array(data)
time = np.array(time)
t_0 = time[0]
time = time - t_0

freq = np.fft.rfftfreq(len(data), d=time[1]-time[0])
freq_data = np.abs(np.fft.rfft(data, norm="ortho"))

plt.subplot(311)
plt.plot(time*1e6, data*1000)
plt.xlabel("Time [us]")
plt.ylabel("Voltage [mV]")

plt.subplot(312)
for i in range(len(freq)):
	if int(freq[i]/1e6) == 1:
		ind = i 
	else:
		ind = 20
plt.plot(freq[ind:]/1e6,freq_data[ind:])
plt.xlabel("Frequency [MHz]")
plt.ylim(0,1)
plt.xlim(0,500)

plt.subplot(313)
f,t,sxx = sp.spectrogram(data, 1.0/(time[1]-time[0]))
plt.pcolormesh(t,f,sxx)
plt.ylabel("Frequency [MHz]")
plt.xlabel("Time [us]")
plt.ylim(0,500e6)

plt.show()

