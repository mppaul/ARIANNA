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
701     10		16214		---
702     17		27364		---
703     23		36940		---
704     17		27364		---
705     17		27364		---
706     23		36940		300		479054

==============================================================================
                              FIRST REPORT
                           February 20, 2019
==============================================================================

Since the 4CH tests above did not show any issues with SBD we are left
to conclude that maybe it's not a 4CH issue but an 8CH. As we know the stations
that are showing this behavior are the 8CH boards that are in SP. I have
requested that Geoff take some force trigger data with Stn 14 (sister station to
Stn 13) and see if it shows any issues of transfering data or if it acts just
like Stn 13. All  data on the 4CH board was tranfered successfully given the 
commuication window. After increasing the communication window to 9hours the
largest file (300 events) was successfully transferred in its entirity. So far
no issues have been able to be recreated. We now move to doing the same tests
but for a 8CH board. Here are some questions to consider as we move forward:

1) Could this be just an 8CH issue solely?

2) Since I have not seen any issues with the data transfer could we rule out 
that there is no issue on our side in Snowflake?
  
3) Could the enviorment of Antarctica be the main issue?

4) Could the station be saving data incorrectly? Therefore transferring bad 
data and we cant tell the difference

------------------------------------------------------------------------------
Test #3 - Data Transfer w/ 8CH Station
------------------------------------------------------------------------------

Notes: There was a small issue with the SD card not being read and writing data
to it but was fixed(?). Station was set up with three force trigger files each
with a different number of events(10, 50, 100). The same coomuincation config
used in the 4CH station was used in the 8CH but obviously an 8CH config. A 
computer was placed near the station to record the debug output. This output
is named screenlog.mbed. The station was sent a config and closed its
communication window. 

Data on SD:
r00801 -- 10 FTpS
r00802 -- 50 FTpS
r00803 -- 100 FTpS

FTpS = Force Triggers per Sequence

Communication Settings:
r00804 -- Initial Comm Setting Config

Debug Output: screenlog.mbed

Original data is stored in data directory and the SBD transfered data is stored
in Trans_data.


DATA FROM SD CARD:

FILE    # OF EVENTS     DAT BYTES       ROOT BYTES
801     10              31910           49824
802     50              113576          158470
803     100             193961		316670


DATA TRANSFER:

        FIRST TRANSFER                  SECOND TRANSFER
        ---------------------------     ---------------------------
FILE    # OF EVENTS     DAT BYTES       # OF EVENTS     DAT BYTES
801     10              31910           --
802     12              38216		--		          
803*	9				6

Screenlog.sbd Notes:

Signed Off			00:11:39

Queued 30min Conf: 804		00:26:00

Start Comm Win			00:32:53
Send RawStatus	
Checking Queue
Sent New Conf: 804
Send Status Data Packs		00:35:52
Checking File Queue
Old Conf Still Running
No File Request in Queue
Send Last File Made: 804*-53	00:37:52
Confirmed Received 0E 10PR
Checking File Queue
No File Request in Queue
Signed Off			00:39:18

Queued 803 File Request		00:50:00

Start Comm Win                  01:00:41
New Conf is Running
Send RawStatus   
Checking Queue
No Conf in Queue
Send Status Data Packs          01:03:00
Checking File Queue
Request of Run 803 Sent
Request of Seq 0 0 Sent		01:04:39
Sending Requested 803-0 File	01:06:42
Last pullFromBuffToBinFile Sent	01:30:04

Queued New Conf - 806		01:40:00

Start Comm Win                  01:53:30
Send RawStatus
Checking Queue
Sent New Conf: 806
Send Status Data Packs          01:54:58
Checking File Queue
Old Conf Still Running
No File Request in Queue
Send Last File Made: 804*-55    01:57:00
Confirmed Received 0E 10PR
Checking File Queue
No File Request in Queue
Signed Off                      01:59:21

Start Comm Win                  02:20:38
Send RawStatus
New Conf is Running: 806
Checking Queue
No Conf in Queue
Send Status Data Packs          02:23:17
Checking File Queue
Request of Run 803 Sent
Request of Seq 0 0 Sent         02:25:38
Sending Requested 803-0 File    02:08:08
Last pullFromBuffToBinFile Sent 03:19:35 

Queued New Conf - 805           03:30:00

Start Comm Win                  03:44:14
Send RawStatus
Checking Queue
Sent New Conf: 805
Send Status Data Packs          03:47:02
Checking File Queue
Old Conf Still Running
No File Request in Queue
Send Last File Made: 806-0	03:50:26
Confirmed Received 0E 10PR
Checking File Queue
No File Request in Queue
Signed Off                      03:51:58

Start Comm Win                  04:12:36
Send RawStatus
New Conf is Running: 805
Checking Queue
No Conf in Queue
Send Status Data Packs          04:14:19
Checking File Queue
Request of Run 803 Sent
Request of Seq 0 0 Sent         04:19:43
Sending Requested 803-0 File    04:23:14
Last pullFromBuffToBinFile Sent 07:51:51
Checking File Queue
Sending Last File Made: 805-1	07:53:49
Checking File Queue		07:54:49
Signed Off			07:56:35


        File r00803 Transfer
        --------------------------- 
TIME	EVENTS		DAT BYTES
30MIN	12
60MIN	24
300MIN	100


Station had a issue where it reset. After a succesfful comm with one 
config 805 it then during the next config data taking for 7min. 
It then possibly restarted and sent its config on the chip. It then
sent a 805 config since the hardware config was different from the 
last config it had. Some extra hickups include sending the signed off
during the checking queue for configs.

 
==============================================================================
                    CONSULTATION w/ Geoff and Chris
                           February 28, 2019
==============================================================================

After recoridng all this data from Test 3 I consulted with Geoff and Chris. My
guess is that SBD is working just fine. I was able to succussfully transfer
large data files. There was two times there was a hiccup and it could have 
occur because the successful files were sent before the comm window. So the
first time the comm window checks the file request it is  there. I will try and 
catch it during the second time it checks the file request. To attempt to 
recreate the issue. 

My guess is that the reason that we are getting data that has no events and
look corrupted may be because the station for some reason is reseting its self.
causing files to not be written correctly. Or during its comm window and its 
sending data the station could be reseting and then corrupting the data.
That would explain why every time we request the file it doesn't send more 
events.

Chris explain that the watchdog is a process that after 20min of doing nothing
the station will reboot. We noticed that the station was rebooting on the 
screenlog.sbd file. After a successful comm it then reboots  during the data 
taking. Cause the original config on the mbed to appear again. Then SBD
will send the most rpevious config which is the saftey procedure when the 
station resets and forgets the configs that are sent to it via comm.

We notice that during purely data taking configs watchdog does not reset. But 
during file request the watchdog resets  more often. However during the 
comm win we dont see it reseting but definity after we do. 

Next steps include: Watching the screenlog.sbd to record when the file request
is sent to the comm win and look for watchdog resets. In addition, to look at 
taking data while during data taking.

------------------------------------------------------------------------------
Test #4 - Study of Communication Sequence
------------------------------------------------------------------------------

First Comm -- 2019-03-05 00:12:12 
Station Commuincates, Sends Current File, Signs Off

Second Comm -- 2019-03-05 00:43:09
Station Commuincates, Checks Station Actors, Loses Communication

Third Comm -- 2019-03-05 01:05:40 (10 events)
Station Communicates, Watchdog Reset TRUE, Sends Previous Conf, Sends Requested
File, Conf Running 804, Signs Off

Fourth Comm -- 2019-03-05 01:54:04
Station Communicates, Conf Running 808, Sends Current File, Signs Off

Communications After were fine but this occured.
2019-03-05 03:55:16+0000 [-] Station [0002F7F2E82D] signed off.
2019-03-05 03:58:27+0000 [-] Station [0002F7F2E82D] signed off.
2019-03-05 04:01:50+0000 [-] Station [0002F7F2E82D] signed off.
2019-03-05 04:06:10+0000 [-] Station [0002F7F2E82D] signed off.
2019-03-05 04:10:47+0000 [-] Station [0002F7F2E82D] signed off.
2019-03-05 04:14:15+0000 [-] Station [0002F7F2E82D] signed off.
2019-03-05 04:18:47+0000 [-] Station [0002F7F2E82D] signed off.
2019-03-05 04:21:27+0000 [-] Station [0002F7F2E82D] signed off.
Comms before and after this were fine.

Next Comm -- 2019-03-05 06:06:46 (6 events)
Station Communicates, File Request Sent First Check, File Sent, Timesout

Comm -- 2019-03-05 07:00:06
Station Commuincates, Sends Current File, Signs Off

Next Comm -- 2019-03-05 07:30:45 (9 Events)
Station Communicates, File Request Sent First Check, File Sent, Timesout

Comm -- 2019-03-05 08:23:14 (9 events)
Station Communicates, File Request Sent Second Check, File Sent, Timesout

Next Comm -- 2019-03-05 09:17:18
Station Commuincates, Gets New Conf, Sends Current File, Signs Off

Comm -- 2019-03-05 09:46:44 (10 events)
Station Commuincates, File Reqeust Sent First Check, File Sent, No Timeout
Checks File Actor, Signs Off (Data 807 Seq 2,3,4, 5)

------------------------------------------------------------------------------
Test #5 - Patterns in Watchdog Reset
------------------------------------------------------------------------------


