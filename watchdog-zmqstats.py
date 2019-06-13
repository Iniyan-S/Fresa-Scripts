#!/usr/bin/python2.7 -tt
"""
******************************************************************************************
 * Copyright (C) 2017 Fresa Technologies - All Rights Reserved
 * 
 * Unauthorized copying of this file, via any medium is strictly  prohibited
 * Proprietary and confidential
 * Written by S. Iniyan <iniyan@fresatechnologies.com>, October - 2017
 
 The purpose of this  program is to monitor the Postfix queue status of the Zimbra progam 
 notify the mail server admin via MAIL when the set threshold value is reached.

 ******************************************************************************************
"""
import os
import threading
import smtplib
import base64

def watchdog_qstats():
	# Set this value to set the poll interval time in SECONDS of this script.
	# timer_value = SECONDS
	
	timer_value = 1800.0 
	
	# Adjust this value to set the threshold value of the queue.
	# threshold = QUEUE VALUE
	
	threshold = 30 	
	
	threading.Timer(timer_value, watchdog_qstats).start()
	output = os.popen("/opt/zimbra/libexec/zmqstat | grep -i active").read()
	data = output.split("=")
	value = int(data[1])
	
	if (value >= threshold):
		print("The value is %d" % value)
		print("The the o/p is high")
		p = base64.b64decode("MW4xeTRuMjYwOA==")
		subject = "The Queue has reached the threshold"
		content = "Subject:{}\n\n The Active Queue has reached {}".format(subject, value)
		#content = ("The  Deferred Queue has reached %d" % value)
		server = smtplib.SMTP('smtp.gmail.com', '587')
		server.ehlo()
		server.starttls()
		server.login('iniyansargunam@gmail.com', p)
		server.sendmail('iniyansargunam@gmail.com', 'iniyan@fresatechnologies.com', content)
		server.close()
		#timer_value = 600.0
	else:
		timer_value = 1800.0
		print("The value is %d" % value)
		print("The o/p is not high")
	
# Start the WATCHDOG_QSTATS function	
watchdog_qstats()