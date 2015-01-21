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
# 2. cd into ~yourpath_to~\calc_step1
# 3. run runtest.bat
# 4. watch the test run and check the result in the console
#
# NOTE: It ist the same as if your would type "java -jar "~yourpath_to~\sikulix.jar" -r calc.sikuli"
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
# NOTE: This works only if some environment variables are set accordingly and are on the PATH
#
# 1. start console
# 2. cd into ~yourpath_to\calc_step1\calc.sikuli
# 3. run jython calc.py
#
# TODO: need to make this more generic, thus one have not to set environment variables on PATH
# TODO: maybe with something like: jython -J-cp path_to\sikulixapi.jar calc.py ???
#


# optional imports: the script runs correct without them from console
# but if they are missing JntelliJ IDEA shows syntax errors
# TODO: How to avoid syntax issues related to this optional imports?
from org.sikuli.script.Region import wait
from org.sikuli.script.Region import exists
from org.sikuli.script.Region import find
from org.sikuli.script.Region import click
from org.sikuli.script.Match import getLastMatch

# required import
from sikuli import *

# Tell Sikuli where to look for the pictures
# NOTE: getting error msg for run OPTION No. 3 when giving a relativ path here (e.g "calc.sikuli")
setBundlePath("C:\SikuliX_POC\Sikuli-and-Robot-Framework-Integration\step_0\calc.sikuli")

# Show SikuliX version in console
version = JEnv.getSikuliVersion()
print "Running with " + version + "."


class Calculator(object):
	def __init__(self):
		self.appCoordinates = (0, 0, 1024, 768)

	def startApp(self):
		calcApp = App("Rechner")
		if not calcApp.window():
			App.open("calc.exe")
			wait(2)
		calcApp.focus()
		wait(1)

	def verifyApp(self):
		# check application
		if exists("CalcApp.png"):
			print("PASS: Calculator window appeared")
		else:
			print("FAIL: No calculator window")

	def performAction(self, *args):
		# get application region
		find("CalcApp.png")

		match = getLastMatch()
		self.appCoordinates = (match.getX(), match.getY(), match.getW(), match.getH())
		appRegion = Region(*self.appCoordinates)

		# rewrite action
		action = args[1]
		if args[1] == '+':
			action = 'Plus'
		elif args[1] == 'exp':
			action = 'Exp'

		with appRegion:
			click("btnC.png")

			click("btn%s.png" % (args[0],))
			click("btn%s.png" % (action,))
			click("btn%s.png" % (args[2],))

			click("btnEqual.png")

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
