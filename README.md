**HELP PLEASE:**
Still searching for a way to get code assistance for Jython
in Vim / gVim e.g. code completion, syntax highlighting and
analysis etc. If you have an idea - please share!!!

You may contact me here: wagner.wladislaw@gmail.com
or leave a comment or an answer on [stackoverflow](http://stackoverflow.com/questions/27924485/is-there-any-way-to-get-jython-support-in-vim-gvim)

==============================================
Sikuli and Robot Framework Integration Project
==============================================

**RECENT UPDATE:**

Works nice and smoothly on Windows 7 AND 8.1 (German version)

**NEXT STEPS:**

- Adjust to English Windows version
- create detailed / beginner friendly documentation in the wiki
- upload all necessary files in step_0 folder

**NOTE:**

On English Windows version you will have to make a new screenshot of your calculator and replace CalcApp.png in all three step_x folders AND in all three folders in calc.py you will have to replace the string "Rechner" with "Calculator". To do that in each calc.py search the line ```calcApp = App("Rechner")``` and change it to ```calcApp = App("Calculator")```.

###Description

Originally this were the source files for Mykhailo´s great tutorial  about integration of [Sikuli](http://www.sikuli.org) with the [Robot Framework](http://www.robotframework.org) on his [block](blog.mykhailo.com). (see readme backup below)

The files were updated in this repo to make them work with SikuliX 1.1.0 (nightly build 2015-01-16) on Windows 8.1. It turned out that after the update da shit is working even with Window 7 without any extra changes needed! That´s because Sikuli is so cool!!!

The hardest thing was to set up everything right. So until the [wiki](https://github.com/Tset-Noitamotua/Sikuli-and-Robot-Framework-Integration/wiki) is ready try to stick to this notes: Install all tools (s. System Config. Setup below) in 32 bit version (even on 64 bit Windows). Put Java, Python, Jython and Sikuli after installation on the PATH - means set your system environment variable PATH accordingly! Here is an
example of [how to put things on the PATH](https://github.com/Tset-Noitamotua/Sikuli-and-Robot-Framework-Integration/wiki/How-To:-Change-Add-System-Environment-Variables). Adjust paths to files and folders in the code if necessary.

####System Configuration Setup:
- Windows 8.1 (German - but I plan to change that to English soon)
- Java version 1.8.0_05 (build 1.8.0_05-b13) can be JDK or JRE
- SikuliX 1.1.0 (nightly build 2015-01-16)
- Robot Framework 2.8.7
- Python 2.7.3
- Jython 2.7 beta3 (Jython 2.7b3)

Optional (for code assistance purpose):
IntelliJ IDEA 14.0.2 with Python plugin and
Jython as project SDK + sikulixapi.jar and
Lib folder from Sikulix installation (~your_path_to_sikulix~\Lib
or ~your_path_to_sikulix~\sikulixapi.jar\Lib) as external libraries
for the project to have syntax highlighting and
code completion for both SikuliX and Python.

Cheers
Tset Noitamotua




######----- BACKUP OF ORIGINAL README -----

================================================
Sikuli and Robot Framework Integration Project
================================================

This is source files for my blogpost on blog.mykhailo.com.
Each directory is a result of same name step described in the blogpost.

To use "robottest.bat" files - robotframework.jar file is requited.
It can be downloaded from Robot Framework official site.

Best regards,
Mykhailo Moroz
