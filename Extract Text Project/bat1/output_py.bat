echo off
break > log.txt

:txtfiles
for %%i in (TBL_T*.txt) do (
    call :readfile %%i
)
py index.py
goto:eof

:readfile
set f=%~1
set /a line = 1
find "rows copied" %f% >> log.txt

find "total" %f% >> log.txt
