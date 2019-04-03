import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab
import sys


File = np.genfromtxt(sys.argv[1], delimiter=',')
list = []
for i in range(len(File)-2):
	list.append(File[i+2][1])
data = np.array(list)*1000

log = True

sigma = np.std(data)
avg = np.average(data)
vrms = np.sqrt(np.mean(data**2))
print str(round(sigma,1)) + ", " + str(round(avg,1)) + ", " + str(round(vrms,1))

f,ax = plt.subplots()
(mu, sig) = norm.fit(data)
n, bins, patches = plt.hist(data,np.arange(min(data), max(data), 0.75),normed =1)
y = mlab.normpdf(bins, mu, sig)
l = plt.plot(bins,y,"b--", label="Fit to " + str(sig))
plt.legend()
plt.xlabel("Voltage (mV)")
plt.title("Sigma " + str(round(sig,1)) + ", Mu " + str(round(mu,1)))
if log == True:
	ax.set_yscale('log')
	plt.ylim(10e-7,10e-1)
'''
freq_data = np.abs(np.fft.rfft(data, norm="ortho"))
freq = np.fft.rfftfreq(len(data),d=0.25e-9)/1e9
plt.plot(freq[100:], freq_data[100:])
'''
plt.show()



