# Copyright (c) 2020 Software AG, Darmstadt, Germany and/or Software AG USA Inc., Reston, VA, USA, and/or its subsidiaries and/or its affiliates and/or their licensors. 
# Use, reproduction, transfer, publication or disclosure is prohibited except as specifically provided for in your License Agreement with Software AG 

import pysys
import apamajdbc.testplugin
from pysys.constants import *

class PySysTest(apamajdbc.testplugin.ApamaJDBCBaseTest):

	def execute(self):
		self.assertPathExists(self.project.appHome+'/connectivity-jdbc.jar', abortOnError=True)

		correlator = self.apamajdbc.startCorrelator('correlator')
		correlator.injectEPL(filenames=['simple.mon'])
		
		self.waitForGrep('correlator.log', expr="Loaded simple test monitor", 
			process=correlator.process, errorExpr=[' (ERROR|FATAL) .*'])
		
	def validate(self):
		# look for log statements in the correlator log file
		self.assertGrep('correlator.log', expr=' (ERROR|FATAL) .*', contains=False)
