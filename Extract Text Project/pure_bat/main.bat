echo off
break > log.txt
break > log2.txt
@REM syntax-FOR-Files
for %%j in (tbl_*.txt) do (
    @REM set A=%find "rows copied" %%j%
    @REM echo %%j
    set /A ifile=%%j
    @REM echo %%j %ifile%
    call :findrow %%j

    )

log.txt
@REM log2.txt

goto:eof

:findrow

for /F %%a in ('findstr /E /R "rows copied." %~1') do (
        echo %~1, %%a >> log.txt
    )
@REM for /F %%a in ('findstr "total" %~1') do (
for /F "delims=: " %%a in ('findstr /B /R "Clock Time " %~1') do (
    echo a %%a
    for %%b in (%%a) do (
        @REM echo %%b >> log.txt
        echo b %%b
    )
        @REM echo %%a >> log2.txt
    )
@REM echo ...