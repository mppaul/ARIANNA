import ROOT
import matplotlib.pyplot as plt
from optparse import OptionParser
import numpy as np
import sys
from matplotlib.widgets import Button
import datetime as datetime

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-r", "--run", default = 143, help = "Run of event to draw",type=int)
    parser.add_option("-e", "--event", default = 1042, help = "Event ID of event to draw",type=int)
    parser.add_option("-f", "--file", default = '/pub/arianna/DATA/Mar2016Prod/FFTshifted/FFTshifted.CalTree.CombinedCommsOffNoHtbt.SnEvtsM0002F7F1F21A.root', help = "File contaning calib tree")
    parser.add_option("-n", "--nChans", default = 4, help = "Number of DAq channels")
    parser.add_option("-s", "--station", default = 31, help = "Station number")
    parser.add_option("--raw", action="store_true",help="Using raw data instead of calibrated data")
    parser.add_option("--fft", action="store_true",help="FFT is in data")
    parser.add_option("--shift", action="store_true",help="Waveform shifted in tree")
    
    (options, args) = parser.parse_args()
    infn = options.file
    run = options.run
    event = options.event
    nChans = int(options.nChans)
    station = int(options.station)
    raw = options.raw
    fft = options.fft
    shift = options.shift

nt = ROOT.TChain("CalibTree")
nt.Add(infn)

if raw:
    calwv = ROOT.TSnRawWaveform()
    nt.SetBranchAddress("RawData.", calwv)

elif shift:
    calwv= ROOT.TSnCalWvData()
    nt.SetBranchAddress("AmpOutDataShifted.", calwv)

else:
    calwv = ROOT.TSnCalWvData()
    nt.SetBranchAddress("AmpOutData.", calwv)

if fft:
    fft = ROOT.TSnCalFFTData()
    nt.SetBranchAddress("AmpOutDataFFT.", fft)
    
evthead = ROOT.TSnEventHeader()
nt.SetBranchAddress("EventHeader.", evthead)

nt.BuildIndex("EventMetadata.fRun", "EventHeader.fNum")
n = nt.GetEntryNumberWithIndex(run,event)

if (n>-1):
    nt.GetEntry(n)
else:
    print "Event not found in file"
    sys.exit()
    
colors = ["#FF9900","#0066FF","#CC00CC","#339933","#fd5249","#00c7c1","#58008f","#5ca7ff"]

if station in [32,50,52,51]:
    times = np.arange(0,256,1)
else:
    times = np.arange(0,128,0.5)

unixtime = evthead.GetUnixTime()
unixdatetime = datetime.datetime.utcfromtimestamp(unixtime)
EventIDString = "Stn{}, run: {}, evt: {}, UTC: {}".format(station,run,event,unixdatetime)
print EventIDString

fig = plt.figure()
fig.suptitle(EventIDString,fontsize=16)
plots = {}
chan = {}

for i in range(0,nChans):
    chan[i] = calwv.GetDataOnCh(i)
    #plots[i] = plt.plot(times,chan[i],label="Channel {0}".format(i),linewidth=2,c=colors[i])
#plt xlabel("Time [ns]",fontsize=16)
#plt.ylabel("Amplitude [mV]",fontsize=16)
#plt.show()



