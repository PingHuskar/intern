@echo off

for /d %%D in (*) do (
    title %%D
    echo %%~fD

    echo start %%D\main.bat
    echo.
    cd %%D
    main.bat
    echo.
    echo stop %%D\main.bat
    
    cd..

)

set /p pattern=Enter to continue:
goto:eof