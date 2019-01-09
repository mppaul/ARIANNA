import uproot as up
import matplotlib.pyplot as plt
from optparse import OptionParser
import numpy as np

if __name__ == '__main__':
	parser = OptionParser()
    	parser.add_option("-f", "--root_file", help = "Path to Root File")
    	parser.add_option("-e", "--event_number", help = "Event to View")
   
    	(options, args) = parser.parse_args()
     	file = options.root_file
	event =int( options.event_number)

data = up.open(file)["RawEventTree"]["RawData."]["RawData.fData"].array()
colors = ["#FF9900","#0066FF","#CC00CC","#339933","#fd5249","#00c7c1","#58008f","#5ca7ff"]
time = np.linspace(0,256,256)

for i in range(4):
	plt.plot(time, data[event][i], color= colors[i])


plt.show()
