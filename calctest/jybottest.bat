@echo off

set sikuli_jar=C:\sikulix\sikulixapi.jar

set CLASSPATH=%sikuli_jar%
set JYTHONPATH=%sikuli_jar%/Lib

jybot --pythonpath=CalcLib ^
      --outputdir=results ^
      --loglevel=TRACE ^
      %*