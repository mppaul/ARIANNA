This folder contains the files and data from BMU Noise tests. According to 
the Antarctica team the wind gen does not supply constant charging and 
discharging to the BMU. The idea is that the BMU has to make more desicions 
when it loses charging voltage and when it gains it. Causing more noise to 
be created. 

Test #1
______________________

This test will look at the baseline noise while the station is charging and 
discharging. Force triggers and thermal triggers are taken to measure the 
noise level (Force Triggers) and the fluctuations in the noise that can 
trigger the station. In addition, we will look at the noise generated when
the power supply that is charging the station is cut off and turned on 
multiple times and when it is, decently, slowly ramped up and declined. 

Run 4001 Force Triggers - Discharging
Run 4002 Force Triggers - Charging
Run 4003 Thermal Triggers - Charging
Run 4004 Thermal Triggers - Discharging
Run 4005 Thermal Triggers - Rapid Charging/ Discharging
Run 4006 Thermal Triggers - Slow Charging/ Discharging

NOTES:

4001 -- Will let config run for 15min. Station is closed and has top lid on
with book to supply weight. USB cord is hanging over the edge with the weight
of the book keeping it in place. Checked power to amps. Checked lights for 
indication that force triggers where being taken. Confirmed SD card was 
inserted. Config started at 4:47PM on Jan 10. Config ended at 5:07PM.

4002 -- Similiar to 4001. Config started at 5:07PM on Jan 10. Config ened 
at 5:23PM. 

4003 -- All channels were set to ~80mV threshold. The non- calibrated thresholds
nevertheless the signals we are looking for are quite large to the point the
signals are being clipped in the data. Config started at 4:18PM on Jan 11. 
Config ended at 4:34PM.

4004 -- Similar to 4003. After checking power to board everytime I probed the
power terminal the station would trigger. The first few triggers are of the
probing. Will consult Chris. Config started at 4:38PM on Jan 11. Config ended
at 4:54PM. Chris found result interesting. After Thermal Trigger Tests probe 
this effect with the oscilloscope.

4005 -- Turning power supply off and on to simulate rapid voltage changes. For
the first 4 min the on and off switch was random. The next 5 min the switch 
was turn off and on in intervals of ~30s. The last 6 min will be in intervals
of ~1min. Config started at 4:56PM. Config ended at 5:11PM.

4006 -- The power is sweeped from the maximum power (17.5V) to  minimum (0V).
During the first 5 min the sweeping will bounce to varous voltages  to be as 
random as possible. The next 3 min will sweep very low voltages (0V-5V), 
next 3min will sweep (5V-10V), the next 4min will sweep (10V-15V). At 13.77V 
the current begings to jump around alot. The current becomes stable again at 
14.3V. Would like to proble this with the oscilloscope. Config started at 
5:15PM on Jan 11. Config ended at 5:30PM.

Test #2
_______________________

DMM - Noise caused by probing Vout with DMM
VOUT - Noise from Vout
VIN -  Noise from Vin
4P - Noise from 4P

NOTES:

All measurements only showed unique waveforms when power to the Vin is abrutly
stopped. While slowly decreasing the voltage nothing creates large events.


Test #3
_______________________

12345 - Run took only thremal triggers for 2 hours. Small issue with ground 
of BMU that may cause some data to be use less in the beginning. Station was
closed and terminators are placed on the inputs of the station and on the 
inputs of the SST board. 




20004 - FPN measurement
20005 - Thermal Trigg Test
20006 - Trig In Trig Out
60000 - Threshold Calibration
05679 - ???

Make better measurements of the pulses and use scope to measure stuff.


Vin Probing
scope_7_2 (ignore)

scope_9 largest pulse

Notes: Image looks like ramping up and down voltages. Difference in time 
between peaks is about 500ms with some pulses being able to disrupt this.

4p Probing

scope_10 image

vout probing 

scope11 image


Notes: replaced the power supply and the same effect happens

Test #4
________________________

I am going to attenpt to  sync the pulse on the Vin line with the pulse
measured on the power supply outside the box.

I will also see if there are dramatic differences when the battery is at very
low charge (dead).

Observation: The voltage range at which the station begins to power cycle 
moves! Power cycling occurs when the input voltage matches the voltage of the
battery. Since the battery was "dead" around 11-12V it began to power cycle
early. Also once the voltage on the battery increased past the input power 
the current decreases which makes sense since the BMU no longer take thinks 
the input voltage is useful for charging. 

Results: The power line outside the box experiences many little pulses with 
the largest pulses being paired with a pulse from the Vin of the BMU. The 
pulse seen on the outer line is indeed the beginning of the Vin pulse so 
the low frequncy stuff is taken away and only high frequency stuff is what 
goes back and forth along the power lines. It is my judgement that the smaller
pulses seen on the outside power line are reflections as their amplitudes get 
smaller and smaller. I would imagine there is not much attentuation since
these reflected pulses are in abundance. I say they are reflected pulses 
because the largest pulse are allways accompanied with a pulse from the Vin.
Also they are all the same waveform shape but they do get more dispersed. 

It is clear that the BMU Vin pulse is first as it and the pulse measured on
the power line have a 19ns separation with the power line trailing. Also I am 
not sure if power cycling is the best term anymore because at these voltages 
the current is not cycling but we are still getting noise on the power lines.
 
          
