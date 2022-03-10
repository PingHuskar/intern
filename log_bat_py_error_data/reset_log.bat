for /d %%D in (*) do (
    title %%D
    echo %%~fD
    
    cd %%D
    del log.csv
    del log.txt
    
    cd..

)