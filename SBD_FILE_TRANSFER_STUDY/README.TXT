==============================================================================
			   SBD File Transfer Study
==============================================================================
Problem

This folder contains all the files related to the tests done to figure out the
reason so many data files are lost during data transfer with Iridium (SBD) or 
transfering the wrong data.

==============================================================================
Test #1 - Preliminary Data Transfer Test
--------

Each run file will contain only one sequence. This data will be taken in 
advance of the data transfer test. During the test the station will be asked
to send this data that is on the SD card. All data transfered in this test will
have the same communication settings.   

Data on SD:
r00701 -- 10 FTpS
r00702 -- 50 FTpS
r00703 -- 100 FTpS
r00704 -- 150 FTpS
r00705 -- 200 FTpS
r00706 -- 300 FTpS

FTpS = Force Triggers per Sequence

Communication Settings:
r00707 -- Initial Comm Setting Config

Debug Output: screenlog.test1

Original data is stored in data directory and the SBD transfered data is stored
in Trans_data. 

Process: Board 102 (4ch originally stn 13) was set up with just a iridum mod.
The Mbed was connected to a computer and the Mbed code was set to the standard
4ch settings as well as debug mode which would output a log onto the computer.
The board was set with pretaken force trigger data with varying yet known and number of events. From snowflake, a request was sent to the board via SBD
to send its stored data. All data that was on the SD card was requested.

Observations: It looks like all the data that was transfered over only hold 
8kbytes of data in each file when we can see that shouldn't be. Geoff and Chris
think there may be an issue with how the a program takes the incoming data and 
processes it. The processing may occur before the file has fully been sent over.
Geoff has editied the program and I will run the test again. So far I have no
comments on the debug read out as I must speak with Chris on how to interept it.

