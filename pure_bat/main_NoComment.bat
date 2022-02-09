echo off
break > log.txt
break > log2.txt

for %%j in (tbl_*.txt) do (

    set /A ifile=%%j
    call :findrow %%j

    )
log.txt
goto:eof

:findrow

for /F %%a in ('findstr /E /R "rows copied." %~1') do (
        echo %~1, %%a >> log.txt
    )

for /F "delims=: " %%a in ('findstr /B /R "Clock Time " %~1') do (
    echo a %%a
    for %%b in (%%a) do (
        echo b %%b
    )
)
