import uproot as up
import numpy as np
import matplotlib.pyplot as plt
from optparse import OptionParser

#def CrossCorr(s1, s2):
#    f1 = np.fft.fft(s1)
#    f2 = np.conj(np.fft.fft(s2))
#    f1 = f1/f1.std()
#    f2 = f2/f2.std()
#    f = np.fft.ifft(f1*f2) / (norm(f1)*norm(f2))
#    return f;

def CrossCorr(s1,s2):
	f1 = (s1 - np.mean(s1)) / (np.std(s1) * len(s1))
	f2 = (s2 - np.mean(s2)) / (np.std(s2))
     	f = np.correlate(f1, f2, 'same')
	return f;

if __name__ == '__main__':
    	parser = OptionParser()
    	parser.add_option("-f", "--file", default = '/pub/arianna/DATA/Mar2016Prod/FFTshifted/FFTshifted.CalTree.CombinedCommsOffNoHtbt.SnEvtsM0002F7F1F21A.root', help = "File contaning calib tree")
    	parser.add_option("--raw", action="store_true",help="Using raw data instead of calibrated data")
    	parser.add_option("--shift", action="store_true",help="Waveform shifted in tree")
 	parser.add_option("-n", "--nChans", default = 4, help = "Number of DAq channels")
	parser.add_option("-c","--Ch",default = 0, help = "Channel to compare for Cross Correlation")    	
	(options, args) = parser.parse_args()
    	infn = options.file
	raw = options.raw
	shift = options.shift
	nChans = options.nChans
	C = options.Ch

file = up.open(infn)

if shift:
	data = file['CalibTree']['AmpOutDataShifted.']['AmpOutDataShifted.fData'].array()

data = file['CalibTree']['AmpOutData.']['AmpOutData.fData'].array()

data = file['CalibTree']['AmpOutDataFFT.']['AmpOutDataFFT.fFFT'].array()

fFreq
fToPower

ch0, ch1, ch2, ch3 = [], [], [], []
Channels = range(int(nChans))
Channels.remove(int(C))

for i in range(4610):
	for j in Channels:
		m = np.amax(abs(CrossCorr(data[i][int(C)], data[i][j])))
		if j == 0:
			ch0.append(m)
		elif j == 1:
			ch1.append(m)
		elif j == 2:
			ch2.append(m)
		else:
			ch3.append(m)

		#print "Event " + str(i) + " Channel " + str(j) + " Corr " + str(m)
bins = 20
colors = ["#FF9900","#0066FF","#CC00CC","#339933","#fd5249","#00c7c1","#58008f","#5ca7ff"]


if 0 in Channels:
	plt.subplot(221)
	plt.hist(ch0[2380:],bins,color= colors[0])
	plt.xlim(0,1)
	plt.xlabel('Correlation Coefficient')
	plt.ylabel('Number of Events')
	plt.title("Channel 0")

if 1 in Channels:
	plt.subplot(222)
	plt.hist(ch1[2380:],bins,color= colors[1])
	plt.xlim(0,1)
	plt.xlabel('Correlation Coefficient')
	plt.ylabel('Number of Events')
	plt.title("Channel 1")

if 2 in Channels:
	plt.subplot(223)
	plt.hist(ch2[2380:],bins,color= colors[2])
	plt.xlim(0,1)
	plt.xlabel('Correlation Coefficient')
	plt.ylabel('Number of Events')
	plt.title("Channel 2")

if 3 in Channels:
	plt.subplot(224)
	plt.hist(ch3[2380:],bins,color= colors[3])
	plt.xlim(0,1)
	plt.xlabel('Correlation Coefficient')
	plt.ylabel('Number of Events')
	plt.title("Channel 3")

plt.show()

