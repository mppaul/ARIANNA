import uproot as up 
import numpy as np 
import matplotlib.pyplot as plt

file = up.open("FFTshifted.CalTree.raw.root") # One Box
file1 = up.open("../r00206/FFTshifted.CalTree.raw.root") # Two Box

data = file["CalibTree"]["AmpOutDataShifted."]["AmpOutDataShifted.fData"].array()
data1 = file1["CalibTree"]["AmpOutDataShifted."]["AmpOutDataShifted.fData"].array()
times = np.arange(0,128,0.5)
dt = 0.5e-9
freq = np.fft.rfftfreq(len(times),dt)
colors = ["#58008f","#0066FF","#CC00CC","#339933","#fd5249","#000000" ,"#00c7c1","#5ca7ff"]

force1 = [169,211,241,265,284,300,325,353,370,385,408,417,432,448,461,467,485,502,519,535,545,559,574,581,590,610,620,632,640,652,662,675,684,697]
force2 = [45,55,65,80,84,91,101,106,111,118,123,133,137,141,145,146,152,160,171,175,179,184,190,193,198,205,211,215,218,226,232,234,238,242]

chan0 = abs(np.fft.rfft(data[128][0],norm='ortho'))
chan1 = abs(np.fft.rfft(data[128][1],norm='ortho'))
chan2 = abs(np.fft.rfft(data[128][2],norm='ortho'))
chan3 = abs(np.fft.rfft(data[128][3],norm='ortho'))

chan0_ = abs(np.fft.rfft(data1[29][0],norm='ortho'))
chan1_ = abs(np.fft.rfft(data1[29][1],norm='ortho'))
chan2_ = abs(np.fft.rfft(data1[29][2],norm='ortho'))
chan3_ = abs(np.fft.rfft(data1[29][3],norm='ortho'))

for i in force1:
	chan0 += abs(np.fft.rfft(data[i][0],norm='ortho'))
	chan1 += abs(np.fft.rfft(data[i][1],norm='ortho'))
	chan2 += abs(np.fft.rfft(data[i][2],norm='ortho'))
	chan3 += abs(np.fft.rfft(data[i][3],norm='ortho'))

for j in force2:
	chan0_ += abs(np.fft.rfft(data1[j][0],norm='ortho'))
	chan1_ += abs(np.fft.rfft(data1[j][1],norm='ortho'))
	chan2_ += abs(np.fft.rfft(data1[j][2],norm='ortho'))
	chan3_ += abs(np.fft.rfft(data1[j][3],norm='ortho'))

plt.figure(1)
plt.plot(freq[1:], (chan0/35)[1:], color=colors[0], label="One Box")
plt.plot(freq[1:], (chan0_/35)[1:], color=colors[4], label="Two Box")
plt.xlabel("Frequency (Hz)")
plt.title("Average Force Trigger Noise FFT Chan0")
plt.legend(loc="center right")

plt.figure(2)
plt.plot(freq[1:], (chan1/35)[1:], color=colors[1], label="One Box")
plt.plot(freq[1:], (chan1_/35)[1:], color=colors[5], label="Two Box")
plt.xlabel("Frequency (Hz)")
plt.title("Average Force Trigger Noise FFT Chan1")
plt.legend(loc="center right")

plt.figure(3)
plt.plot(freq[1:], (chan2/35)[1:], color=colors[2], label="One Box")
plt.plot(freq[1:], (chan2_/35)[1:], color=colors[6], label="Two Box")
plt.xlabel("Frequency (Hz)")
plt.title("Average Force Trigger Noise FFT Chan2")
plt.legend(loc="center right")

plt.figure(4)
plt.plot(freq[1:], (chan3/35)[1:], color=colors[3], label="One Box")
plt.plot(freq[1:], (chan3_/35)[1:], color=colors[7], label="Two Box")
plt.xlabel("Frequency (Hz)")
plt.title("Average Force Trigger Noise FFT Chan3")
plt.legend(loc="center right")

'''
plt.figure(1)
plt.plot(freq[1:], (chan0/1000)[1:], color=colors[0], label="One Box")
plt.plot(freq[1:], (chan0_/1000)[1:], color=colors[4], label="Two Box")
plt.xlabel("Frequency (Hz)")
plt.title("Average Thermal Noise FFT Chan0")
plt.legend(loc="center right")

plt.figure(2)
plt.plot(freq[1:], (chan1/1000)[1:], color=colors[1], label="One Box")
plt.plot(freq[1:], (chan1_/1000)[1:], color=colors[5], label="Two Box")
plt.xlabel("Frequency (Hz)")
plt.title("Average Thermal Noise FFT Chan1")
plt.legend(loc="center right")

plt.figure(3)
plt.plot(freq[1:], (chan2/1000)[1:], color=colors[2], label="One Box")
plt.plot(freq[1:], (chan2_/1000)[1:], color=colors[6], label="Two Box")
plt.xlabel("Frequency (Hz)")
plt.title("Average Thermal Noise FFT Chan2")
plt.legend(loc="center right")

plt.figure(4)
plt.plot(freq[1:], (chan3/1000)[1:], color=colors[3], label="One Box")
plt.plot(freq[1:], (chan3_/1000)[1:], color=colors[7],  label="Two Box")
plt.xlabel("Frequency (Hz)")
plt.title("Average Thermal Noise FFT Chan3")
plt.legend(loc="center right")
'''

#plt.figure(1)
#plt.plot(times, data[0][0], color=colors[0])

#plt.figure(2)
#plt.plot(times, data1[0][0], color=colors[4])

#for i in range(4):
#    plt.plot(freq[1:],abs(np.fft.rfft(data[0][i], norm='ortho'))[1:], color=colors[i])



