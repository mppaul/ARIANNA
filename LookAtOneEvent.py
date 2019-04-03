import uproot as up
import numpy as np
import matplotlib.pyplot as plt
from optparse import OptionParser

if __name__ == '__main__':
        parser = OptionParser()
        parser.add_option("-f", "--file", help = "File contaning calib tree")
       # parser.add_option("--raw", action="store_true",help="Using raw data instead of calibrated data")
       # parser.add_option("--shift", action="store_true",help="Waveform shifted in tree")
        parser.add_option("-e", "--event", default = 4, help = "Number of DAq channels")
        (options, args) = parser.parse_args()

        infn = options.file
        #raw = options.raw
        #shift = options.shift
        e = int(options.event)
        #C = options.Ch

makePlots = False

file = up.open(infn)
data = np.array(file['CalibTree']['AmpOutData.']['AmpOutData.fData'].array())
#data = np.array(file['CalibTree']['FPNSubData.']['FPNSubData.fData'].array())

colors = ["#FF9900","#0066FF","#CC00CC","#339933","#fd5249","#00c7c1","#58008f","#5ca7ff"]
time = np.arange(0,256,1)

for i in range(4):
	plt.figure(i)
	plt.plot(time,data[e][i], color=colors[i], label="Channel " +str(i))
	plt.legend()
	plt.ylabel("Voltage [mV]")
	plt.xlabel("Time [ns]")

plt.show()
