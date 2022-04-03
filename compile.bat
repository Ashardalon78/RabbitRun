python setup.py build
rmdir build\exe.win-amd64-3.7\lib\scipy /Q /S
rmdir build\exe.win-amd64-3.7\lib\numpy /Q /S
rmdir build\exe.win-amd64-3.7\lib\tkinter /Q /S
rmdir build\exe.win-amd64-3.7\lib\distutlis /Q /S
rmdir build\exe.win-amd64-3.7\lib\pytz /Q /S
rmdir build\exe.win-amd64-3.7\lib\setuptools /Q /S
rmdir build\exe.win-amd64-3.7\lib\test /Q /S
rmdir build\exe.win-amd64-3.7\lib\unittest /Q /S
rmdir build\exe.win-amd64-3.7\lib\urllib /Q /S
rmdir build\exe.win-amd64-3.7\lib\win32com /Q /S
rmdir build\exe.win-amd64-3.7\lib\xmlrpc /Q /S
cd build
ren exe.win-amd64-3.7 Rabbit_Run_Win10