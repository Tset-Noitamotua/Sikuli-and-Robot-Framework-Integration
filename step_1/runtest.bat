@echo off

java -jar "C:\SikuliX_110\sikulix.jar" -r calc.sikuli

REM START of comment block 1
GOTO EndComment_1
#
# Place multi line
#       comments here
:EndComment_1
REM END of comment block 1

REM Use GOTO:EOF instead of EXIT for Windows NT and later
REM On Windows EXIT closes the console
GOTO:EOF