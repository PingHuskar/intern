@ECHO off
setlocal EnableDelayedExpansion
@REM findstr /R /c:".* rows copied." log.txt
set r =('findstr /R /c:".* rows copied." log.txt')
echo %r%
@REM for /f "delims=" %%a in ("%result%") do (
    @REM echo %%a
    @REM echo asdf
@REM )
@REM echo %result%

@REM FOR %G IN (tbl_*.txt) do (find /n /i "rows copied" "%G")