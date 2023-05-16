from threading import *

print("Name of Current Thead ",current_thread()) #  <_MainThread(MainThread, started 4301866368)>

current_thread().setName("Simplilearn-CISCO Thread")

print("Name of Current Thead ",current_thread()) #<_MainThread(Simplilearn-CISCO Thread, started 4373988736)>