==============================================================================
                               BMU Noise Study
==============================================================================
Problem

This folder contains the files and data from BMU Noise tests. According to 
the Antarctica team the wind gen does not supply constant charging and 
discharging to the BMU. The idea is that the BMU has to make more desicions 
when it loses charging voltage and when it gains it. Causing more noise to 
be created. 

==============================================================================
Test #1
------------------------------------------------------------------------------

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

------------------------------------------------------------------------------
Test #2
------------------------------------------------------------------------------

DMM - Noise caused by probing Vout with DMM
VOUT - Noise from Vout
VIN -  Noise from Vin
4P - Noise from 4P

NOTES:

All measurements only showed unique waveforms when power to the Vin is abrutly
stopped. While slowly decreasing the voltage nothing creates large events.

------------------------------------------------------------------------------
Test #3
------------------------------------------------------------------------------

12345 - Run took only thremal triggers for 2 hours. Small issue with ground 
of BMU that may cause some data to be use less in the beginning. Station was
closed and terminators are placed on the inputs of the station and on the 
inputs of the SST board. 

Note: Need to rerun test#3.

Better measurements of noise with scope.
scope_9 - largest pulse

Notes: Image looks like ramping up and down voltages. Difference in time 
between peaks is about 500ms with some pulses being able to disrupt this.

4p Probing - scope_10 image

vout probing - scope11 image


Notes: replaced the power supply and the same effect happens

------------------------------------------------------------------------------
Test #4
------------------------------------------------------------------------------


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
the high frequncy stuff is taken away and only low frequency stuff is what 
goes back and forth along the power lines. It is my judgement that the smaller
pulses seen on the outside power line are reflections as their amplitudes get 
smaller and smaller. I would imagine there is not much attentuation since
these reflected pulses are in abundance. I say they are reflected pulses 
because the largest pulse are allways accompanied with a pulse from the Vin.
Also they are all the same waveform shape but they do get more dispersed.

Note: After some conversations with Steve and Stewart the little pulses on the
power line outside the box are associated with the noise of the power source.
It seems that the little pulses get added to the large pulse that makes it out
the station from giving the appearence that the pulses are synced really what
is happening is the large pulse being emitted from the BMU is making it out
the filter pin and is being found on the powerline. However this pulse is 
attenuated and lost some of its higher frequency components.

It is clear that the BMU Vin pulse is first as it and the pulse measured on
the power line have a 19ns separation with the power line trailing. Also I am 
not sure if power cycling is the best term anymore because at these voltages 
the current is not cycling but we are still getting noise on the power lines.
 
==============================================================================
                    CONSULTATION w/ Steve & Stewart
			   January 24, 2019
==============================================================================

Stewart believes that the sawtooth or exponential waveforms are due to the BMU
trying to decide whether or not to charge the battery. This usually occurs 
when the power source voltage significanty close to the voltage measured 
on the battery. Stewart brough up the point that we should be using constant
current instead of voltage since that is a more accurate way of representing
the wind gen and solar panels. When using constant current the same waveform 
appear. The frequency of the exponential waveform is about 4.2 Hz or 240ms. 
When the power source is about +1V above the battery voltage the exponential 
waveform goes away. This is because we are at a voltage that is high enough
that the battery is safely be always charging.

Stewart also believes that the more narrow pulses that appear at a frequency
of 500Hz that are overlaid on top of the exponential waveform may be due to 
the current limiter. These pulse continue till the power supply is 3V higher 
than the battery voltage. In addition the higher in voltage we go the frequncy
increases as well to about 33 kHz. Stewart beleive this is the current 
limiter because the voltage and corresponding current is to much to charge 
the battery so the limiter could be making descisions to lower the current to 
a safe charging current. If the power source is raised higher then stewart 
belives the current limiter could be no longer charging the battery or has 
lowered the current as far down as possible.

Steve and Astrid have observed lines that appear on the time difference 
between event vs event number. The lines appear at multiples of 240ms. This 
is likely due to the exponential waveform. The extra multiples come from the 
station missing the trigger. The wind gen data shows these lines more 
frequnently because of the intermident wind fluctions. 

Steve, according to last meeting, asked Astrid to look closer at the solar
panel stations to see if they also show these lines in the delta t's vs event
number especially at times when the sun is setting. A preliminiary look at stn
14 showed some of these lines during times when the sun is going down. A more 
detailed look is to  come soon.

A problem we faced is not being able to view the high frequency stuff that is
coming out the power line that could trigger the station. Stewart beleives that
the power supply we are using has a lot of capcitance that doesn't allow any 
fast moving/ high frequency fluctuations to happen on the line. Stewart 
suggested we use a solar panel and try and mimic this behavior especially if
Astrid shows that the solar panel also causes this nosie to occur when the 
power source voltage matches the battery voltage from old data. 

Steve says the solar panel is difficult to use when it come to trying to lower
the power going to the battery. I suggested using a 12V Max solar panel and 
using the battery when it is 'dead" (11V) so that the solar panel will charge
it into the range where the noise starts to occur. At this point we should be 
able to see if any high frequency stuff is leaking out.

Steve also suggested a redo of Test#3. To double check that the station does 
not trigger it's self on the inside this is because Stewart's suggestion to 
fix this over all issue with the BMU is creating a better filter to filter 
out the high noise. The question then becomes where to put it. If the noise does
not trigger the station on the inside then the current filter pins on the BMU
box do not need to be changed. The filter can then go on the Power in to the 
station. But if they do in fact trigger the station on the inside then it 
should go on the BMU box.

Steve believes we may be able to just buy better filer pins instead of creating
a filter all together. Stewart would also like to see the wind gen circuit
diagram to see if the pulse being sent to the wind gen could cause a reaction
by the wind gen which could then be creating high frequency noise.

Next Steps:
-- Find a 12V solar panel for Steve to buy
-- Rerun Test #3 with details
-- Place 12V solar panel on top of the High Bay and try to recreate noise with
dead battery.

------------------------------------------------------------------------------
Test #5 - Redo of Test #3
------------------------------------------------------------------------------

r06789 - Config takes only thermal triggers. Set threshold low to make sure
we only trigger on amps noise and extra noise from BMU. The thresholds are set
to around +/- 45V. Channels 2 and 7 are connected to amps while all others 
are terminated on the SST board. Station is set to High or low and 1 of 2
majority.

Notes: The station was dead. The battery voltage was 11.5V. I waited until 
it reach around 12V before beginning test. The station would turn off when the
power cycling began around 11.5V. Makes sense since the only reason the station
is on is because of the power source. If it cycles in power then it will 
naturally turn it off. 

The station is taking thermal triggers I will check the rates once I get the 
data. I will take two sets. One while pwoer cycling and the other when it is not
to compare the rates at these thresholds. T

Test began at 8:20PM. The station was put into power cycling. Will change the 
power source voltage at 9:06PM. Station was put into charging mode with large 
voltage ~17V. Data taking ended at 10:05PM.


------------------------------------------------------------------------------
Test #6 - Solar Panel + BMU Noise Tests
------------------------------------------------------------------------------


