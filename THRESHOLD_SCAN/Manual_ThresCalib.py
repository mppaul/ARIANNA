######################
# Command to run script: python Manual_ThresCalib.py  thresh_calib_b201_2019.csv #where the first value is the script and the second value is the csv file to be imported.
#######################
import numpy as np
import scipy
import json
import sys
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy.polynomial.polynomial import polyfit
import re


def array_generator():
    if sys.argv[1].endswith('.csv'):
        data = np.genfromtxt(sys.argv[1], dtype=None, delimiter=",")
        d = {}
        dim = data.shape
        CH = ["CH0", "CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7"]
        col = [0, 4, 8, 12, 16, 20, 24, 28]
        for l in range(8):
            ind = []
            for i in range(dim[0]):
                if data[i][col[l]] == CH[l]:
                    d[data[i][col[l]]] = {}
                if data[i][col[l]] == "PG Value":
                    d[CH[l]][data[i][col[l] + 2][5:]] = {}
                    d[CH[l]][data[i][col[l] + 2][5:]][data[i][col[l]]] = []
                    d[CH[l]][data[i][col[l] + 2][5:]][data[i][col[l] + 1]] = []
                    d[CH[l]][data[i][col[l] + 2][5:]]["Frequency"] = []
                    ind.append(i)

            for j in range(len(ind)):
                if ind[j] == ind[-1]:
                    end = dim[0]
                else:
                    end = ind[j + 1]

                for k in range(ind[j] + 1, end):
                    if any(np.core.defchararray.startswith(data[k][col[l]], ["-", '1', '2', '3', '4', '5', '6', '7', '8', '9'])) == False:
                        break
                    d[CH[l]][data[ind[j]][col[l] + 2][5:]][data[ind[j]][col[l]]].append(float(data[k][col[l]]))
                    d[CH[l]][data[ind[j]][col[l] + 2][5:]][data[ind[j]][col[l] + 1]].append(float(data[k][col[l] + 1]))
                    d[CH[l]][data[ind[j]][col[l] + 2][5:]]["Frequency"].append(float(data[k][col[l] + 2]))

        with open("data.json", 'w') as outfile:
            json.dump(d, outfile, sort_keys=True, indent=4)
        data = d

        # if sys.argv[1].endswith('.json'):
        #     with open(sys.argv[1], 'r') as fin:
        #         data = json.load(fin)
        # for chan in data:
        #     for thres in data[chan]:
        #         plt.plot(data[chan][thres]["SCOPE"], data[chan][thres]["Frequency"])

    # print(data)
    return data

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def thresh_calib_calc():
    data = array_generator()

    CH = ["CH0", "CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7"]
    VOL1 = ["30mV", "45mV", "60mV", "80mV", "120mV", "150mV", "200mV", "300mV",
            "-30mV", "-45mV", "-60mV", "-80mV", "-120mV", "-150mV", "-200mV", "-300mV"]

    def fsigmoid(x, a, b):
        y = 1 / (1 + np.exp(-b * (x - a)))  # generates sigmoid for comparison
        return y
    lst = {}
    for ch in CH:
        linear_plotx = []
        linear_ploty = []
        for vol in VOL1:
            scope = data[ch][vol]["SCOPE"]
            frequency = data[ch][vol]["Frequency"]
            # print(ch, vol)

            f_yvals = []
            for i in frequency:
                f_yvals.append(i / 1000.)  # easier for code to understand max values of 1 for y values
            v_xvals = scope

            # first p0 value is last value in scope voltage to get near actual middle value.
            popt, pcov = curve_fit(fsigmoid, v_xvals, f_yvals, p0=[int(scope[len(v_xvals) - 1]), 1])
            xfin = np.linspace(v_xvals[0], v_xvals[len(v_xvals) - 1], 100)  # last value in this function it number of points not intervals!
            yfin = fsigmoid(xfin, *popt)

            # since switched x and y value, this interpolates the voltages(y value) given an x (freuqency) 0.5kHz.
            yinterp = np.interp(0.5, f_yvals, v_xvals)
            match = re.match(r"(-?[0-9]+)([a-zA-Z]+)", vol, re.I)  # separates voltage label from label.
            if match:
                items = match.groups()
            linear_plotx.append(int(items[0]))
            linear_ploty.append(yinterp)

        # positive voltage values
        b, m = polyfit(linear_plotx[:8], linear_ploty[:8], 1)
        print(b, m)
        plt.plot(np.array(linear_plotx[:8]), np.array(linear_ploty[:8]), '.', label="y = %s x + %s " % (float(m), float(b)))
        plt.plot(np.array(linear_plotx[:8]), b + m * np.array(linear_plotx[:8]), '-')
        plt.legend()
        plt.ylim(0, 350)
        plt.xlim(0, 350)
        plt.title("%s: postive voltage" % (ch))
        plt.show()

        # negative voltage values
        b2, m2 = polyfit(linear_plotx[8:], linear_ploty[8:], 1)
        print(b, m)
        plt.plot(np.array(linear_plotx[8:]), np.array(linear_ploty[8:]), '.', label="y = %s x + %s " % (float(m2), float(b2)))
        plt.plot(np.array(linear_plotx[8:]), b2 + m2 * np.array(linear_plotx[8:]), '-')
        plt.legend()
        plt.ylim(0, -350)
        plt.xlim(0, -350)
        plt.title("%s: negative voltage" % (ch))
        plt.show()

        lst[ch] = (b, m), (b2, m2)
    print(lst)


thresh_calib_calc()
