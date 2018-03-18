import subprocess
import re
import time
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


def get_periodic_ping():  # Main function, logs response delay and time of day into list
    global address
    global log
    global clock
    output = subprocess.check_output('ping %s -n 3' % (address,), shell=True)
    response = int(re.search("Average = (.*?)ms", str(output)).group(1))
    log.append(response)
    clock.append(time.strftime("%H:%M:%S", time.gmtime(time.time())))


def stop():  # Stop function closes tkinter window and ends previous function
    global running
    running = False
    root.destroy()


def testing():  # start function, continuously calls get_periodic_ping() after delay
    global running
    if running:
        get_periodic_ping()
        root.after(10000, testing)


# Initialising variables
address = "google.co.uk"
log = []
clock = []
running = True

root = tk.Tk()  # create tkinter UI
root.title("PING TESTER")
root.geometry("200x100")

startButton = tk.Button(root, text='START', command=testing).pack()  # stop and start buttons
stopButton = tk.Button(root, text='STOP', command=stop).pack()

root.mainloop()

# Plot data when done
plt.figure('Response time to %s' % address)
plt.grid('on')
plt.ylabel('Response time (ms)')

# Only take every 3rd timestamp for clarity
x = range(len(clock))
x = x[0::3]
clock = clock[0::3]
plt.xticks(x, clock, rotation='60')

plt.plot(log)
plt.show()
