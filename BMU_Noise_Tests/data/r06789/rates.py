#python ./rates.py infn intv 

import uproot as up 
import numpy as np
import matplotlib.pyplot as plt
import sys

infn = up.open(sys.argv[1])
data = np.array(infn["CalibTree"]["AmpOutData."]['AmpOutData.fData'].array())
dt = np.array(infn["CalibTree"]['EventHeader.']['EventHeader.fDTms'].array())/1000.0

clk = 0
time = []
for i in range(len(dt)):
	clk += dt[i]
	time.append(clk)

time = np.array(time)/3600

intv = float(sys.argv[2])
s = int(time[len(time)-1]/intv)+1
rate = []

for j in range(s):
	cnt = 0
	for i in range(len(time)):
		if time[i] > (intv*j) and time[i] <= intv*(j+1):	
			cnt += 1
	rate.append(cnt/(intv*3600))

t = np.arange(intv,intv*(s+1),intv)



