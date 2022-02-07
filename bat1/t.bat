@ECHO off
setlocal EnableDelayedExpansion
set /p pattern=Enter id:
findstr %pattern% tbl_T1.txt > result
if %errorlevel%==0 (
  set var2= <result
  echo(!var2!
  set var1=!var2:~5,3!
  echo(!var1! > test.txt
  echo(!var1!
) else (
  echo error
)
del result