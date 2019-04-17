
# To run: python Thermal_Noise.py -f Calibrated Root file path -n Number of Channels

import uproot as up
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab
from optparse import OptionParser

if __name__ == '__main__':
        parser = OptionParser()
        parser.add_option("-f", "--file", help = "File contaning calib tree")
        parser.add_option("-n", "--nChans", default = 8, help = "Number of DAq channels")
        (options, args) = parser.parse_args()
	infn = options.file
        nChans = int(options.nChans)

print "Initializing..."

Printvals = True 	# Print each channel's average sigma, VRMS and offset for the entire data set
makePlots = False	# Make histogram plots of the noise voltage
log = False 		# Plot histogram in log
TempPlots = False	# Make Temperature Plots: 1) VRMS vs Temp 2) Temp vs Time**
FreqPlots = True	# Make Frequency Plots: 1) AVG Frequency 2) Frequency vs Event
Freq_Temp = False	# Make Frequency as a function of Temperature Plot** *MUST Have TempPlots and FreqPlots = True*

colors = ["#FF9900","#0066FF","#CC00CC","#339933","#fd5249","#00c7c1","#58008f","#5ca7ff"]

# Opening Root file using Uproot and extracting Force Trigger Data and putting into a Numpy array

file = up.open(infn)
print "File Opened..."
data = np.array(file['CalibTree']['AmpOutData.']['AmpOutData.fData'].array())
Temp = np.array(file['TemperatureTree']['Temperature.']['Temperature.fTemp'].array())
print "Data Loaded..."

# Removal of Stops from Data

stops = file['CalibTree']['RawData.']['RawData.fStop'].array()
data_ns = np.zeros((len(data),nChans,245))
for i in range(len(data)):
	for k in range(len(stops[i])):
		if stops[i][k] > 0:
			for j in range(nChans):
				sam = (k+1)*8
				stp = np.linspace(sam-9,sam+1,11, dtype="int")
				for l in range(11):
					if stp[l] < 0:
						stp[l] = stp[l]+256
					if stp[l] > 255:
						stp[l] = stp[l]-256
				data_ns[i][j] = np.delete(data[i][j], stp)	
			break

data = np.zeros((len(data), nChans,245))
data = data_ns
#################################################################################################################

# Does a real Fast Fourier Transform of the data 

if FreqPlots == True:
	print "Making Frequency Plots"
	freq_data = {}
	freq = np.fft.rfftfreq(245,d=1e-9)/1e9
	avg_freq = {}
	plt.figure(1)
	for i in range(nChans):
		freq_data[i] = np.zeros((len(data), 123))
		for j in range(len(data)):
			freq_data[i][j] = np.abs(np.fft.rfft(data[j][i], norm="ortho"))
		plt.subplot(421+i)		
		plt.pcolormesh(np.arange(0,len(data)),freq, np.transpose(freq_data[i]), vmin=0, vmax=120)
		plt.xlabel("Event Number")
		plt.ylabel("Frequncy [GHz]")
		plt.title("Channel " + str(i) +": Frequency Dependence")
		plt.ylim(0,0.5)
		plt.colorbar()
	plt.subplots_adjust(top=0.95, bottom=0.05, left=0.075, right=1.0, hspace=0.5, wspace=0.05)	
	
	plt.figure(2)	
	for i in range(nChans):	
		avg_freq[i] = np.sum(freq_data[i], axis=0)/len(freq_data[i])
		plt.plot(freq[10:],avg_freq[i][10:], color=colors[i], label="Channel " +str(i))
		plt.title("Average Frequency Dependence")
		plt.xlabel("Frequency [GHz]")
		plt.legend()
	plt.show()
#################################################################################################################

# Calculation of each channel's average sigma, VRMS, and offset for whole data set

if Printvals == True:
	print "Channel \#: sigma, offset, Vrms"
	for i in range(nChans):
		sigma = np.std(data[:,i,:].flatten())
		avg = np.average(data[:,i,:].flatten())
		vrms = np.sqrt(np.mean(data[:,i,:].flatten()**2))
		print "Channel " + str(i) + ": " + str(round(sigma,1)) + ", " + str(round(avg,1)) + ", " + str(round(vrms,1))
#################################################################################################################

# Make the histogram plots of the thermal noise can save to file or show in terminal

if makePlots == True:
	print "Making Histograms..."
	for i in range(nChans):
        	f,ax = plt.subplots()
	 	(mu, sig) = norm.fit(data[:,i,:].flatten())
        	n, bins, patches = plt.hist(data[:,i,:].flatten(),np.arange(min(data[:,i,:].flatten()), max(data[:,i,:].flatten()), 1),normed =1,color=colors[i],label="Channel " +str(i))
        	y = mlab.normpdf(bins, mu, sig)
		l = plt.plot(bins,y,"b--", label="Fit to " + str(sig))
		plt.legend()
		plt.xlabel("Voltage (mV)")
		plt.title("Channel " + str(i) + ": Sigma " + str(round(sig,1)) + ", Mu " + str(round(mu,1)))
		if log == True:
			ax.set_yscale('log')
			plt.ylim(10e-7,10e-1)
		#plt.savefig("Channel_" + str(i) + "COLD_FPN_COLD_DATA" + ".png")
	plt.show()
#################################################################################################################

# Plot the sig, vrms, and offset as a function of temperature and temperature as a function of time [NOT AUTOMATED]

if TempPlots == True:
	print "Making Temperature Plots..."
	temperature  = []
	sig, avg, vrms = {}, {}, {}
	for k in range(nChans):
		sig[k], avg[k], vrms[k] = [], [], []
	for j in range(len(data)/10):
		temperature.append(np.average(Temp[j*3:(j+1)*3].flatten()))
		for i in range(nChans):
			sig[i].append(np.std(data[j*10:(j+1)*10,i,:].flatten()))
                	avg[i].append(np.average(data[j*10:(j+1)*10,i,:].flatten()))
                	vrms[i].append(np.sqrt(np.mean(data[j*10:(j+1)*10,i,:].flatten()**2)))
	for i in range(nChans):
		plt.figure(1)
		plt.plot(temperature, avg[i], color=colors[i], label="Channel " +str(i))
		plt.title("Offset as a function of Temperature")
		plt.legend()
		plt.xlabel("Temperature [Celsius]")
		plt.ylabel("Voltage [mV]")
		plt.figure(2)
                plt.plot(temperature, sig[i], color=colors[i], label="Channel " +str(i))
		plt.title("Sigma as a function of Temperature")
                plt.legend()
                plt.xlabel("Temperature [Celsius]")
                plt.ylabel("Voltage [mV]")
		plt.figure(3)
                plt.plot(temperature, vrms[i], color=colors[i], label="Channel " +str(i))
		plt.title("Vrms as a function of Temperature")
                plt.legend()
                plt.xlabel("Temperature [Celsius]")
                plt.ylabel("Voltage [mV]")
	dt = np.delete(np.arange(0,820,1), np.arange(0,820,10))/60.0
	plt.figure(4)
	plt.plot(dt,Temp)
	plt.title("Temperature vs Time")
        plt.ylabel("Temperature [Celsius]")
        plt.xlabel("Time [Hours]")
	
	if Freq_Temp == True:
		plt.figure(5)
		temp_freq = {}
		for i in range(nChans):
			temp_freq[i] = np.zeros((len(data)/10,123))
			for j in range(len(data)/10):
				temp_freq[i][j] = np.sum(freq_data[i][j*10:(j+1)*10], axis=0)/10	
		for i in range(nChans):
			plt.subplot(421+i)
			plt.pcolormesh(temperature, freq, np.transpose(temp_freq[i]), vmin=0, vmax=120)
			plt.colorbar()
			plt.ylim(0,0.5)
			plt.ylabel("Frequency [GHz]")
			plt.title("Channel " + str(i))
			plt.xlabel("Temperature [Celsius]")
		plt.subplots_adjust(top=0.95, bottom=0.05, left=0.075, right=1.0, hspace=0.5, wspace=0.05)

		step_temps, avg_step_freq, q = {}, {}, ["-20to-15", "-10to-5", "5to10", "15to20"]
		for i in q:
			step_temps[i]= []
		for i in range(len(Temp)):
		        if Temp[i] > -20 and Temp[i] < -15:
		                step_temps[q[0]].append(i)
			if Temp[i] > -10 and Temp[i] < -5:
		                step_temps[q[1]].append(i)
			if Temp[i] > 5 and Temp[i] < 10:
		                step_temps[q[2]].append(i)
			if Temp[i] > 15 and Temp[i] < 20:
		                step_temps[q[3]].append(i)
		for j in range(nChans):
			avg_step_freq[j] = {}
			plt.figure(j+6)
			plt.title("Channel " + str(j))
			for i in range(4):
				maxind = np.max(step_temps[q[i]])
				minind = np.min(step_temps[q[i]])	
				avg_step_freq[j][q[i]] = np.sum(freq_data[j][minind-1:maxind+1], axis=0)/(len(step_temps[q[i]])+2)		
				plt.plot(freq[1:],avg_step_freq[j][q[i]][1:],label=q[i])
			plt.plot(freq[1:],avg_freq[j][1:], label="Average")
			plt.xlabel("Frequency [GHz]")
			plt.legend()
	plt.show()
#################################################################################################################

'''
bins = np.linspace(-80,80,81)

File = np.genfromtxt(infn, delimiter=',')
list = []
for i in range(len(File)-2):
	list.append(File[i+2][1])
Ghz = []
for i in range((len(File) -2)/4):
	Ghz.append(File[i*4][1])

data = np.array(list)*1000
data_downsam = np.array(Ghz)*1000

plt.figure(1)
plt.hist(data, np.arange(min(data), max(data), 0.6), normed =1)
plt.legend()
plt.xlabel("Voltage (mV)")

plt.figure(2)
plt.hist(data_downsam, np.arange(min(data_downsam), max(data_downsam), 0.6), normed =1)
plt.legend()
plt.xlabel("Voltage (mV)")

sigma = np.std(data)
sigma_down = np.std(data_downsam)

avg = np.average(data)
avg_down = np.average(data_downsam)


print "4Ghz " + str(sigma) + ", " + str(avg)
print "1Ghz (time domain) " + str(sigma_down) + ", " + str(avg_down)
plt.show()

'''
