@echo off

set sikuli_jar=C:\sikulix\sikulixapi.jar
set robotframework_jar=C:\RobotFramework\robotframework-2.8.6.jar

java -cp "%robotframework_jar%;%sikuli_jar%" ^
     -Dpython.path="%sikuli_jar%/Lib" ^
     org.robotframework.RobotFramework ^
     --pythonpath=CalcLib ^
     --outputdir=results ^
     --loglevel=TRACE ^
     %*