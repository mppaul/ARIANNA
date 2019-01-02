from __future__ import print_function
import json
from scripts.offline import dacs2014 as dacs
from scripts.online import AriUtils
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import json
import sys

plot = False

channelstr_to_channelid = {0: 3,
                           1: 2,
                           2: 1,
                           3: 0,
                           4: 7,
                           5: 6,
                           6: 5,
                           7: 4}


if __name__ == "__main__":

    with open(sys.argv[1], 'r') as fin:
        data = json.load(fin)
        for board in data.keys():
            n_channels = len(data[board]['onesided_600Hz'].keys())
            print('single sided thresholds')
            for iCh in range(n_channels):
                for lh in ['high', 'low']:
                    high = data[board]['onesided_600Hz'][str(iCh)][lh]
                    V = np.array([x[0] for x in high])
                    rates = np.array([x[1] for x in high])
                    rates[rates == None] = np.nan
                    dac_thresholds = np.array([dacs.getDac(203, channelstr_to_channelid[iCh], x) for x in V])
                    
                    print("channel {} {}: {:d} (was {:.1f} Hz)".format(iCh, lh, dac_thresholds[-1], rates[-1]))
#                     ss = get_sigma(rates)
                    if plot:
                        fig, ax = plt.subplots(1, 1)
                        ax.plot(dac_thresholds, rates, 'o')
                        ax.plot(dac_thresholds[-1], rates[-1], 'd')
                        ax.set_title('channel {} {}'.format(iCh, lh))
                        ax.set_xlabel("dac count")
                        ax.set_ylabel("frequency [Hz]")
                        fig.tight_layout()
                        plt.show()
                        
                        
            # loop through dual sided thresholds
            print('dual thresholds')
            for iCh in range(n_channels):
                if(str(iCh) in data[board]['dual_60Hz']):
                    high = data[board]['dual_60Hz'][str(iCh)]
                    Vlow = np.array([x[0] for x in high])
                    Vhigh = np.array([x[1] for x in high])
                    rates = np.array([x[2] for x in high])
                    rates[rates == None] = np.nan
                    dac_thresholds_low = np.array([dacs.getDac(203, channelstr_to_channelid[iCh], x) for x in Vlow])
                    dac_thresholds_high = np.array([dacs.getDac(203, channelstr_to_channelid[iCh], x) for x in Vhigh])
                    
                    if(np.isnan(rates[-1])):
                        print("channel {}: low = {:d} high =  {:d} (was {:.1f}, {:.1f} Hz)".format(iCh, dac_thresholds_low[-1], dac_thresholds_high[-1], rates[-1], rates[-2]))
                    else:
                        print("channel {}: low = {:d} high =  {:d} (was {:.1f} Hz)".format(iCh, dac_thresholds_low[-1], dac_thresholds_high[-1], rates[-1]))
    #                     ss = get_sigma(rates)
