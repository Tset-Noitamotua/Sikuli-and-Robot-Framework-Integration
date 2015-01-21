@echo off

java -jar "C:\SikuliX_110\sikulix.jar" -r calc.sikuli

REM Start of comment block 1

GOTO EndComment_1
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

:EndComment_1

REM Use GOTO:EOF instead of EXIT for Windows NT and later
REM On Windows EXIT closes the cosole
GOTO:EOF