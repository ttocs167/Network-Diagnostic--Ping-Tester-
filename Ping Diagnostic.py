import subprocess
import re
import time
import tkinter as tk
import matplotlib.pyplot as plt


def get_periodic_ping():
    global address
    global log
    output = subprocess.check_output('ping %s -n 3' % (address,), shell=True)
    response = int(re.search("Average = (.*?)ms", str(output)).group(1))
    log.append(response)


def stop():
    global running
    running = False
    root.destroy()


def testing():
    global running
    running = True
    if running:
        get_periodic_ping()
        root.after(10000, testing)


address = "google.co.uk"
log = []
running = True

root = tk.Tk()
root.title("PING TESTER")
root.geometry("200x100")

startButton = tk.Button(root, text='START', command=testing).pack()
stopButton = tk.Button(root, text='STOP', command=stop).pack()

root.mainloop()

plt.plot(log)
plt.show()
