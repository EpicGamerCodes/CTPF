@echo off
cls
title Text Reader

:reader1
cls
set user=%1
set tiout=%2
set path=%3
set ti=%tiout%
title Text Reader - %user%
cls
if not "%tiout%"=="1" echo ----WARNING: WITH TIMEOUT ENABLED, MESSAGES WILL NOT BE REALTIME!----
type %path%
goto mreader

:mreader
set tiout=%ti%
set content=""
for /F "delims=" %%a in (%path%) do (
   set "content=%%a"
)
echo %content%
goto checkreader

:checkreader
if not "%tiout%"=="0" goto checkreaderwait
for /F "delims=" %%a in (%path%) do (
   set "current=%%a"
)
if not "%current%"=="%content%" goto mreader
set tiout=%ti%
goto checkreader

:checkreaderwait
C:\Windows\System32\timeout.exe /T %tiout% /nobreak >nul
set ti=%tiout%
set tiout=0
goto checkreader

:tiouti
cls
echo Timeout Option not vaild. Needs to be a number.
pause
exit

:clsX
cls
set content=%usern% %content%
goto checkreader
