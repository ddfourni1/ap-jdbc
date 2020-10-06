# Copyright (c) 2015-2016, 2018-2020 Software AG, Darmstadt, Germany and/or Software AG USA Inc., Reston, VA, USA, and/or its subsidiaries and/or its affiliates and/or their licensors. 
# Use, reproduction, transfer, publication or disclosure is prohibited except as specifically provided for in your License Agreement with Software AG 

from pysys.constants import *
from apama.basetest import ApamaBaseTest
from apama.correlator import CorrelatorHelper

class PySysTest(ApamaBaseTest):

	def execute(self):
		self.assertPathExists(self.project.appHome+'/connectivity-jdbc.jar', abortOnError=True)

		correlator = CorrelatorHelper(self, name='correlator')
		correlator.start(logfile='correlator.log')
		
		correlator.injectEPL(filenames=['simple.mon'])
		
		self.waitForGrep('correlator.log', expr="Loaded simple test monitor", 
			process=correlator.process, errorExpr=[' (ERROR|FATAL) .*'])
		
	def validate(self):
		# look for log statements in the correlator log file
		self.assertGrep('correlator.log', expr=' (ERROR|FATAL) .*', contains=False)
