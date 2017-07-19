import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("freq", type=float, help="Desired frequency of signal pulse")
parser.add_argument("-avg", "--average", type=int, help="Number of waveforms to average", default=2048)
parser.add_argument("-amp", "--amplitude", type=float, help="Initial amplitude of waveform", default=5)

args = parser.parse_args()

def signal(freq):
	period = 1/freq
	spl = int((period/1e-9) * 100)
	t = np.linspace(0.0,period, num=spl)	
	y = args.amplitude*np.sin(2*np.pi*freq*t)
	return y, spl

wv, spl = signal(args.freq)

zero = np.zeros(800)
wv = np.concatenate((np.concatenate((zero,wv)), zero))

tot_spl = 1600 + spl
tx = np.linspace(0.0, (tot_spl/100)*1e-9, num=tot_spl)


f = np.zeros(tot_spl)
mu, sigma= 0, 2
err = mu + sigma *np.random.randn(args.average)

for i in range(len(err)):
	y = wv
    	samples = int(float(err[i]) *100)
    
    	if samples > 0: 
        	chunk = y[-1*samples::]
        	w = len(y) - samples
        	shift = y[:w:]
        	y = np.concatenate((chunk, shift))
    	elif samples < 0:
        	chunk = y[-1*samples::]
        	w = len(y) + samples
        	shift = y[:-w:]
        	y = np.concatenate((chunk, shift))
	else:
        	pass

    	f = f + y
    
favg = f/args.average

plt.figure(1)
plt.subplot(311)
plt.plot(tx,f)
plt.subplot(312)
plt.plot(tx,favg)
plt.subplot(313)
plt.plot(tx,wv)
plt.show()
