from subprocess import Popen, PIPE
from sys import stdout 


with Popen(['python', 'Producer.py'], stdout=PIPE, text=True) as proc:
    for line in proc.stdout:
        print("DATA",line.rstrip())



