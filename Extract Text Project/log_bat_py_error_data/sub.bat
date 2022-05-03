@echo off
break > log.txt
del log.csv
rem Config
set thisfile=log_db_ams_export

title %thisfile%

for %%i in (*.log) do (
    echo %%i
    call :readfile %%i
)

py ../index.py %thisfile%

ren log.txt log.csv
goto:eof
:readfile
set f=%~1
find "rows copied" %f% >> log.txt
find "total" %f% >> log.txt
find "Server Message" %f% >> log.txt