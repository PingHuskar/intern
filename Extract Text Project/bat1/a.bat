echo off

@break > log.txt

@REM goto:txtfiles

@REM :readfile
@REM set f = %~1
@REM echo %~1

@REM @REM for /f "delims=" %%i in ('find "rows copied" %f%') do echo %%i
@REM @REM echo %output%

@REM set "myString=abcdef!%%^^()^!"
@REM call :strlen result myString
@REM if %result% == 14 echo 555
@REM echo %result%
@REM https://stackoverflow.com/questions/5837418/how-do-you-get-the-string-length-in-a-batch-file
@REM goto:eof
setlocal EnableDelayedExpansion
for %%j in (tbl_*.txt) do (
    
    @REM set /a num ='find "rows copied" %%j'
    echo ..........................................................
    @REM echo %%j
    find "rows copied" %%j >> log.txt
    
    find "rows copied" %%j
    echo %f%
    @REM (
        @REM echo %f%
        @REM set tt=%f:-=%
        @REM echo.%tt%
    @REM )
    @REM find "total" %%j >> log.txt

    @REM for /F "delims=\n" %%i in ('find "rows copied" %%j') do (
        @SET VAR=%%i
        @REM SET /A VAR=%%i
        @REM IF %VAR:~0,2% == -- ( echo %VAR%)
        @REM IF %VAR:~0,2% == -- ( echo %%i)


        @REM echo %%i
        @REM @set "myString=!i!"
        @REM call :strlen result myString
        @REM if %result% == 14 echo 555
        @REM echo %result%
        @REM ECHO ...


        @REM ---------- TBL_T1.TXT
        @REM 126245 rows copied.
        
        @REM echo %VAR%
        @REM ---------- TBL_T3.TXT
        @REM IF ECHO %VAR:~0,2% == -- (
            @REM SET /A VAR=%%i
            
            @REM )
        @REM echo %VAR:~0,2%
        @REM echo %VAR:~11,6%
    )
    @REM echo %output%

    @REM FOR /F "delims=\n" %%g IN ('find "rows copied" %%j') do (
    @REM     SET VAR=%%g
    @REM     echo %VAR% %%j
    @REM )

    @REM echo %num%
    @REM find "rows copied" %%j >> log.txt
    @REM find "total" %%j >> log.txt
)

goto:eof

@REM :strlen <resultVar> <stringVar>
@REM (   
@REM     setlocal EnableDelayedExpansion
@REM     (set^ tmp=!%~2!)
@REM     if defined tmp (
@REM         set "len=1"
@REM         for %%P in (4096 2048 1024 512 256 128 64 32 16 8 4 2 1) do (
@REM             if "!tmp:~%%P,1!" NEQ "" ( 
@REM                 set /a "len+=%%P"
@REM                 set "tmp=!tmp:~%%P!"
@REM             )
@REM         )
@REM     ) ELSE (
@REM         set len=0
@REM     )
@REM )
@REM ( 
@REM     endlocal
@REM     set "%~1=%len%"
@REM     exit /b
@REM )