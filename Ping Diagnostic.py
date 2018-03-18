import subprocess
import re
import tkinter as tk


def get_ping(address):
    output = subprocess.check_output('ping %s -n 1' % (address,), shell=True)
    response = re.search("Average = (.*?)ms", str(output))
    time = int(response.group(1))
    return time


server = "google.co.uk"

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="PING",
                   command=get_ping(server))
slogan.pack(side=tk.LEFT)

root.mainloop()
