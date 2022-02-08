echo off
break > log.txt

for %%j in (tbl_*.txt) do (
    find "rows copied" %%j >> log.txt
    find "total" %%j >> log.txt
@REM     call :readfile %%j
    )

java src/index.java

del log.txt
ren C:\Users\SF114-32\IdeaProjects\project1\final_log.txt log.txt
log.txt
goto:eof
