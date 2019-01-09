import uproot as up
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab
from optparse import OptionParser

if __name__ == '__main__':
        parser = OptionParser()
        parser.add_option("-f", "--file", help = "File contaning calib tree")
        (options, args) = parser.parse_args()

        infn = options.file

File = np.genfromtxt(infn, delimiter=',')

