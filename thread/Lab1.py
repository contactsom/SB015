import threading

print("Name of Current Thead ", threading.current_thread().getName()) # MainThread OLD

print("Name of Current Thead ", threading.current_thread()) #  <_MainThread(MainThread, started 4301866368)>