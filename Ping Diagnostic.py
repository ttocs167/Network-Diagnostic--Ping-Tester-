import subprocess
import re
import tkinter as tk


def get_ping():
    global address
    global pingTime
    output = subprocess.check_output('ping %s -n 1' % (address,), shell=True)
    response = re.search("Average = (.*?)ms", str(output))
    time = int(response.group(1))
    pingTime.set(str(time))


address = "google.co.uk"

root = tk.Tk()
root.geometry("300x200+350+350")

pingTime = tk.StringVar()

pingButton = tk.Button(root,
                       text='PING',
                       command=get_ping)
pingButton.pack()

pingLabel = tk.Label(root,
                     textvariable=pingTime)
pingLabel.pack()

root.mainloop()
