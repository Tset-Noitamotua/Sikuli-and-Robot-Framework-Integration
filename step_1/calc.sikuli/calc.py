# -*- coding: utf-8 -*-
from __future__ import with_statement

# You have three options to run this script from cmd (console / terminal or whatever u like to call it):
# [ON WINDOWS]To start your console press Win + R then type cmd and press ENTER.
#
# /// OPTION No. I (Using runtest.bat)
#
# NOTE: Make sure to adjust the path to your sikulixapi.jar in runtest.bat!
#
# 1. start console
# 2. cd into ~yourpath_to~\step_1
# 3. run runtest.bat
# 4. watch the test run and check the result in the console
#
# NOTE: It is the same as if your would type "java -jar "~yourpath_to~\sikulix.jar" -r calc.sikuli"
# in your console. Thus runtest.bat is just for convinience.
# TODO: clarify - sikulix.jar contains an own Jython interpreter? Thus the installed one isn´t used in this case???
#
#
# /// OPTION No. II (Using runsikulix.cmd of Sikuli)
#
# 1. start console
# 2. run ~yourpath_to\runsikulix.cmd -r ~yourpath_to\calc.sikuli
# 3. watch the test run and check the result in the console
#
# NOTE: -r makes the Sikuli-IDE (sikulix.jar) execute our calc.sikuli folder
# without showing the Sikuli-IDE
#
# TODO: clarify - the build in Jython Interpreter of Sikuli is used in this case, too???
#
# /// OPTION No. III (Using jython command)
#
# NOTE: This works only if environment variables CLASSPATH and JYTHONPATH are set accordingly
# (e.g. CLASSPATH=~your_path_to~\sikulixapi.jar and JYTHONPATH=~your_path_to~\sikulixapi.jar\Lib)
#
# 1. start console
# 2. cd into ~yourpath_to\step_1\calc.sikuli
# 3. run jython calc.py
#
# TODO: need to make this more generic, thus one have not to set environment variables
# TODO: maybe with something like: jython -J-cp path_to\sikulixapi.jar calc.py ???



# IMPORTANT: Python level import (sikuli comes from sikulixapi.jar\Lib
# NEVER EVER mix Python level imports of Sikuli like this with Java level
# imports like "from org.sikuli.script.Region import wait"
# For more details go here: https://answers.launchpad.net/sikuli/+question/261129
from sikuli import *
# from sikuli import JEnv
# from sikuli import Env
# from sikuli import setBundlePath
# from sikuli.Sikuli import App
# from sikuli import Region
# from sikuli import Screen
# from sikuli import KEY_CTRL



# Tell Sikuli where to look for pictures
setBundlePath("calc.sikuli")

# Show SikuliX version in console
version = JEnv.getSikuliVersion()
print "Running with " + version + "."

# Need to create a Screen Object to avoid usage of undotted methods
# e.g. wait(), find(image), click(image), exists(image) etc. will
# be marked as unresolved references by ana IDE
# thus one should use s.wait(), s.find(image) etc
# or use the constant SCREEN.wait(), SCREEN.find(image ... NOTE: it´s case sensitive!!!
s = Screen()

class Calculator(object):
	def __init__(self):
		self.appCoordinates = (0, 0, 1024, 768)

	def startApp(self):
		calcApp = App("Rechner")
		if not calcApp.window():
			App.open("calc.exe")
			s.wait(2)
		calcApp.focus()
		s.wait(1)

	def verifyApp(self):
		# check application
		if s.exists("CalcApp.png"):
			print("PASS: Calculator window appeared")
		else:
			print("FAIL: No calculator window")

	def performAction(self, *args):
		# get application region
		s.find("CalcApp.png")

		match = s.getLastMatch()
		self.appCoordinates = (match.getX(), match.getY(), match.getW(), match.getH())
		appRegion = Region(*self.appCoordinates)

		# rewrite action
		action = args[1]
		if args[1] == '+':
			action = 'Plus'
		elif args[1] == 'exp':
			action = 'Exp'

		# Use of "with" leads to undotted method call click() which causes a unresolved reference!!!
		# with appRegion:
		appRegion.click("btnC.png")

		appRegion.click("btn%s.png" % (args[0],))
		appRegion.click("btn%s.png" % (action,))
		appRegion.click("btn%s.png" % (args[2],))

		appRegion.click("btnEqual.png")

	def verifyResult(self, *args):
		expected_result = str(eval(''.join(args)))
		actual_result = self.getResultFromClipboard()

		#verification
		if actual_result == expected_result:
			print("PASS: Action performed correctly and result equals %s" % expected_result)
		else:
			print("FAIL: Actual result '%s' is not equal to expected result '%s'" % (actual_result, expected_result))

	def getResultFromClipboard(self):
		type('c', KEY_CTRL)
		return str(Env.getClipboard())

	def runTest(self):
		self.startApp()
		self.verifyApp()

		actions = '2+2'
		self.performAction(*actions)
		self.verifyResult(*actions)


if __name__ == "__main__":
	calc = Calculator()
	calc.runTest()
