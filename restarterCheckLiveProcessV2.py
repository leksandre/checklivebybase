import subprocess
import time
import random
import psutil
import os
p = psutil.Process(os.getpid())
p.nice(18)


while True:
    subprocess.run(["python3.6", "./checkLiveToProcessV2.py"]) 
    time.sleep(1)
    subprocess.run(["python3.6", "./checkLiveToProcessV2.py"]) 
    time.sleep(1)
    subprocess.run(["python3.6", "./checkLiveToProcessV2.py"]) 
    time.sleep(1)
    subprocess.run(["python3.6", "./checkLiveToProcessV2.py"]) 
    time.sleep(1)
    subprocess.run(["python3.6", "./checkLiveToProcessV2.py"]) 
    time.sleep(1)
    subprocess.run(["python3.6", "./checkLiveToProcessV2.py"]) 
    
    time.sleep(random.randint(1,10))
