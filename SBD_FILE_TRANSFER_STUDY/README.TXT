==============================================================================
			   SBD File Transfer Study
==============================================================================
Problem

This folder contains all the files related to the tests done to figure out the
reason so many data files are lost or imcomplete during data transfer with 
Iridium (SBD).

==============================================================================
Test #1 - Preliminary Data Transfer Test
------------------------------------------------------------------------------

Notes:
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
The board was set with pretaken force trigger data with varying yet known 
number of events. From snowflake, a request was sent to the board via SBD
to send its stored data. All data that was on the SD card was requested.

Observations: It looks like all the data that was transfered over only hold 
8kbytes of data in each file when we can see that shouldn't be. Geoff and Chris
think there may be an issue with how the a program takes the incoming data and 
processes it. The processing may occur before the file has fully been sent over.
Geoff has editied the program and I will run the test again. So far I have no
comments on the debug read out as I must speak with Chris on how to interept it.

Comment: This test needs to be redone. The reason why the transferred files had
only 8k bytes of data is becuase the actual config file that the station was 
using had a communication window of 10min. The config file r00707 was on the 
MBED flash memory but the MBED has a safety procedure of remembering the last
config it was given before it turnned off. If the Config file on its flash
memory and its last config differ then the MBED will return to its old config 
after one comm window. Essentially it used the flash memory config to start up
and communicate first then got the most previous config it had last ran which
was from when it was in Antarctica. 

------------------------------------------------------------------------------
Test #2 - Redo of Preliminary Data Transfer Test
------------------------------------------------------------------------------

Notes:
Using the same set up and process as described in test 1, except now the station
is activitly using the right config file to regularly communicate, we conduct
a redo test.

The config file (r00707) has been queued and will determine the station's comm
windows. Note a file will be sent with r00707 on it as the station's will send 
their most recent file creation every comm window. If a file is requested then
the station first sends the requested file. 

The debug output will be collected when there is a loss of data noticed. 


DATA FROM SD CARD:

FILE	# OF EVENTS	DAT BYTES	ROOT BYTES 
701	10		16214		41823		
702	50		80054		74635
703	100		115481		159854
704	150		239654		157940
705	200		319454		198643
706	300		479054		281918

Note: r00703 has 4 sequences in it but we only care about the first one since 
that is the only one we request.

DATA TRANSFER:

	FIRST TRANSFER			SECOND TRANSFER 
	---------------------------	---------------------------
FILE	# OF EVENTS     DAT BYTES	# OF EVENTS     DAT BYTES 
701	10		16214		10		16214
702	29		46516		23		36940
703	17		27364		23		36940
704	17		27364		17		27364
705	23		36940		17		27364
706	17		27364		17		27364


        THIRD TRANSFER                  FOURTH TRANSFER
        ---------------------------     ---------------------------   
FILE    # OF EVENTS     DAT BYTES       # OF EVENTS     DAT BYTES
701        
702     
703     
704     
705     
706     

