@echo off
cd /d %~dp0

REM Số vòng lặp PageRank
set iterations= 8

REM Thư mục đầu vào ban đầu
set input=input

for /L %%i in (1,1,%iterations%) do (
    echo ==== Iteration %%i ====
    
    REM Xoá output cũ nếu có
    if exist output rmdir /s /q output

    REM Chạy Hadoop Streaming
    call hadoop jar D:\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar ^
     -input %input% ^
     -output output ^
     -mapper "python mapper.py" ^
     -reducer "python reducer.py" 

    REM Kiểm tra kết quả của Hadoop
    if %errorlevel% neq 0 (
        echo Hadoop job failed with error level %errorlevel%
        pause
        exit /b %errorlevel%
    )

    REM Ghi kết quả làm đầu vào cho vòng sau
    rmdir /s /q %input%
    mkdir %input%
    copy output\part-00000 %input%\graph.txt > nul

    echo =========================
)

REM Tạo độ trễ sau khi chạy xong
timeout /t 5

REM Hoặc dừng lại với pause
pause
