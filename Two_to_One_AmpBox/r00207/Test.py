import ROOT
import matplotlib.pyplot as plt
from optparse import OptionParser
import numpy as np
import sys
from matplotlib.widgets import Button
import datetime as datetime


def cc(s1, s2):
    f1 = np.fft.fft(s1)
    f2 = np.conj(np.fft.fft(s2))
    f1 = f1/f1.std()
    f2 = f2/f2.std()
    f = np.fft.ifft(f1*f2)
    return f;



if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-r", "--run1", default = 143, help = "Run of event to draw",type=int)
    parser.add_option("-e", "--event1", default = 1042, help = "Event ID of event to draw",type=int)
    parser.add_option("-f", "--file1", default = '/pub/arianna/DATA/Mar2016Prod/FFTshifted/FFTshifted.CalTree.CombinedCommsOffNoHtbt.SnEvtsM0002F7F1F21A.root', help = "File contaning calib tree")
    parser.add_option("-g", "--run2", default = 143, help = "Run of event to draw",type=int)
    parser.add_option("-d", "--event2", default = 1042, help = "Event ID of event to draw",type=int)
    parser.add_option("-a", "--file2", default = '/pub/arianna/DATA/Mar2016Prod/FFTshifted/FFTshifted.CalTree.CombinedCommsOffNoHtbt.SnEvtsM0002F7F1F21A.root', help = "File contaning calib tree")
    parser.add_option("-n", "--nChans", default = 4, help = "Number of DAq channels")
    parser.add_option("-s", "--station", default
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-r", "--run1", default = 143, help = "Run of event to dr$
    parser.add_option("-e", "--event1", default = 1042, help = "Event ID of eve$
    parser.add_option("-f", "--file1", default = '/pub/arianna/DATA/Mar2016Prod$
    parser.add_option("-g", "--run2", default = 143, help = "Run of event to dr$
    parser.add_option("-d", "--event2", default = 1042, help = "Event ID of eve$
    parser.add_option("-a", "--file2", default = '/pub/arianna/DATA/Mar2016Prod$
    parser.add_option("-n", "--nChans", default = 4, help = "Number of DAq chan$
    parser.add_option("-s", "--station", default = 31, help = "Station number")
    parser.add_option("--raw", action="store_true",help="Using raw data instead$
    parser.add_option("--fft", action="store_true",help="FFT is in data")
    parser.add_option("--shift", action="store_true",help="Waveform shifted in $

    (options, args) = parser.parse_args()
    infn1 = options.file1
 = 31, help = "Station number")
    parser.add_option("--raw", action="store_true",help="Using raw data instead of calibrated data")
    parser.add_option("--fft", action="store_true",help="FFT is in data")
    parser.add_option("--shift", action="store_true",help="Waveform shifted in tree")
    
    (options, args) = parser.parse_args()
    infn1 = options.file1
    run1 = options.run1
    event1 = options.event1
    infn2 = options.file2
    run2 = options.run2
    event2 = options.event2
    nChans = int(options.nChans)
    station = int(options.station)
    raw = options.raw
    fft = options.fft
    shift = options.shift

nt = ROOT.TChain("CalibTree")
nt.Add(infn1)

if raw:
    calwv1 = ROOT.TSnRawWaveform()
    nt.SetBranchAddress("RawData.", calwv1)

elif shift:
    calwv1= ROOT.TSnCalWvData()
    nt.SetBranchAddress("AmpOutDataShifted.", calwv1)
    print "hi"

else:
    calwv1 = ROOT.TSnCalWvData()
    nt.SetBranchAddress("AmpOutData.", calwv1)

if fft:
    fft1 = ROOT.TSnCalFFTData()
    nt.SetBranchAddress("AmpOutDataFFT.", fft1)
    
evthead1 = ROOT.TSnEventHeader()
nt.SetBranchAddress("EventHeader.", evthead1)

nt.BuildIndex("EventMetadata.fRun", "EventHeader.fNum")
n = nt.GetEntryNumberWithIndex(run1,event1)

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

unixtime = evthead1.GetUnixTime()
unixdatetime = datetime.datetime.utcfromtimestamp(unixtime)
EventIDString = "Stn{}, run: {}, evt: {}, UTC: {}".format(station,run1,event1,unixdatetime)
print EventIDString

"AmpOutDataShifted."fig = plt.figure()
fig.suptitle(EventIDString,fontsize=16)
plots = {}
chan1 = {}

for i in range(0,nChans):
    chan1[i] = calwv1.GetDataOnCh(i)
    #plots[i] = plt.plot(times,chan[i],label="Channel {0}".format(i),linewidth=2,c=colors[i])
#plt xlabel("Time [ns]",fontsize=16)
#plt.ylabel("Amplitude [mV]",fontsize=16)
#plt.show()

bt = ROOT.TChain("CalibTree")
bt.Add(infn2)

if raw:
    calwv2 = ROOT.TSnRawWaveform()
    bt.SetBranchAddress("RawData.", calwv2)

elif shift:
    calwv2= ROOT.TSnCalWvData()
    bt.SetBranchAddress("AmpOutDataShifted.", calwv2)

else:
    calwv2 = ROOT.TSnCalWvData()
    bt.SetBranchAddress("AmpOutData.", calwv2)

if fft:
    fft2 = ROOT.TSnCalFFTData()
    bt.SetBranchAddress("AmpOutDataFFT.", fft2)
    
evthead2 = ROOT.TSnEventHeader()
bt.SetBranchAddress("EventHeader.", evthead2)

bt.BuildIndex("EventMetadata.fRun", "EventHeader.fNum")
b = bt.GetEntryNumberWithIndex(run2,event2)

if (b>-1):
    bt.GetEntry(b)
else:
    print "Event not found in file"
    sys.exit()
    
colors = ["#FF9900","#0066FF","#CC00CC","#339933","#fd5249","#00c7c1","#58008f","#5ca7ff"]

if station in [32,50,52,51]:
    times = np.arange(0,256,1)
else:
    times = np.arange(0,128,0.5)

unixtime = evthead2.GetUnixTime()
unixdatetime = datetime.datetime.utcfromtimestamp(unixtime)
EventIDString = "Stn{}, run: {}, evt: {}, UTC: {}".format(station,run2,event2,unixdatetime)
print EventIDString

fig = plt.figure()
fig.suptitle(EventIDString,fontsize=16)
plots = {}
chan2 = {}

for i in range(0,nChans):
    chan2[i] = calwv2.GetDataOnCh(i)


