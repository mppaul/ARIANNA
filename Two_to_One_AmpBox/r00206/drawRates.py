import os,sys
import ROOT

if (len(sys.argv)<2):
    print "Usage: python -i drawRates.py [eventRates filename]"
    sys.exit()

erfn = sys.argv[1]

erf = ROOT.TFile(erfn)

gERvsT = erf.Get("gERvsT")
gERvsEnum = erf.Get("gERvsEnum")
gEnumVsT = erf.Get("gEnumVsT")
hRawDT = erf.Get("hRawDT")
hConsDT = erf.Get("hConsDT")
hCombDT = erf.Get("hCombDT")
hConsDTvsT = erf.Get("hConsDTvsT")
gConsDTvsT = erf.Get("gConsDTvsT")
hCombDTvsT = erf.Get("hCombDTvsT")

cwid = 500
chit = 400
plots={}
store=[]

ROOT.gStyle.SetOptStat(0)
#ROOT.gStyle.SetOptTitle(0)
#ROOT.gStyle.SetTitleYOffset(1.2);
#ROOT.gStyle.SetPadLeftMargin(0.12);
#ROOT.gStyle.SetPadRightMargin(0.04);
#ROOT.gStyle.SetPadTopMargin(0.03);
#ROOT.gStyle.SetPadBottomMargin(0.12);
ROOT.gSystem.Setenv("TZ","UTC");
ROOT.gStyle.SetTimeOffset(0);
'''
c1 = ROOT.TCanvas("c1","c1 - rate vs evt num",cwid,chit)
c1.cd()
gERvsEnum.Draw("ap")
c1.cd()
c1.Update()
'''
c2 = ROOT.TCanvas("c2","c2 - rate vs t",cwid,int(chit*1.5))
c2.Divide(1,2)
c2.cd(1)
gERvsT.Draw("ap")
c2.Update()
gERvsT.GetHistogram().GetXaxis().SetTimeDisplay(1)
gERvsT.GetHistogram().GetXaxis().SetNdivisions(505)
gERvsT.Draw("ap")
'''
c2.cd(2)
gEnumVsT.Draw("ap")
c2.Update()
gEnumVsT.GetHistogram().GetXaxis().SetTimeDisplay(1)
gEnumVsT.GetHistogram().GetXaxis().SetNdivisions(505)
gEnumVsT.Draw("ap")
c2.cd()
c2.Update()

c3 = ROOT.TCanvas("c3","c3 - dt",int(cwid*1.5),int(chit*1.5))
c3.Divide(2,2)
c3.cd(1)
hRawDT.Draw()
c3.GetPad(1).SetLogy()
c3.cd(3)
hConsDT.Draw()
c3.GetPad(3).SetLogy()
c3.cd(4)
hCombDT.Draw()
c3.GetPad(4).SetLogy()
c3.cd()
c3.Update()

c4 = ROOT.TCanvas("c4","c4 - dt vs t",int(cwid*1.5),int(chit*1.5))
c4.Divide(2,2)
c4.cd(3)
hConsDTvsT.GetXaxis().SetTimeDisplay(1)
hConsDTvsT.GetXaxis().SetNdivisions(505)
hConsDTvsT.Draw("colz")
c4.cd(2)
gConsDTvsT.Draw("ap")
c4.Update()
gConsDTvsT.GetHistogram().GetXaxis().SetTimeDisplay(1)
gConsDTvsT.GetHistogram().GetXaxis().SetNdivisions(505)
gConsDTvsT.Draw("ap")
c4.cd(4)
hCombDTvsT.GetXaxis().SetTimeDisplay(1)
hCombDTvsT.GetXaxis().SetNdivisions(505)
hCombDTvsT.Draw("colz")
c4.cd()
c4.Update()'''
