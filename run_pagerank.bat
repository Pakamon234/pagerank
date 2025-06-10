@echo off
cd /d %~dp0

REM Số vòng lặp PageRank
set iterations=10

REM Thư mục đầu vào ban đầu
set input=input

for /L %%i in (1,1,%iterations%) do (
    echo ==== Iteration %%i ====
    
    REM Xoá output cũ nếu có
    if exist output rmdir /s /q output

    REM Chạy Hadoop Streaming
    hadoop jar D:\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar ^
     -input %input% ^
     -output output ^
     -mapper "python mapper.py" ^
     -reducer "python reducer.py" 

    REM Ghi kết quả làm đầu vào cho vòng sau
    rmdir /s /q %input%
    mkdir %input%
    copy output\part-00000 %input%\graph.txt > nul

    echo =========================
)

pause
