import time
from threading import Thread, Lock
import random

N = int(input()) # Number of threads
list_of_all_threads = []
on = [] # List of threads which  will be turn on after initialization
if ML_in == True: # wait until ML module initialised
    a = randint((0,N - 1)) # get random number. Thread on this number will 
                           # be proexecutedceed, others will be switch off.
    on = list_of_all_threads[a]
