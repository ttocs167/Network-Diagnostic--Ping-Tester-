# Network-Diagnostic--Ping-Tester-
Tool for periodically pinging an address and returning graph.


This tool was made by me to diagnose some network problems.
It periodically pings a specified server using windows commands and then grabs the ping through a string search on the returned string.
This response time is then graphed over time using matplotlib.
The whole thing is wrapped in a Tkinter UI so it can be started and stopped.

It is still a work in progress in the sense that there are still some features I would like to add, 
but it is functional and has been useful to me.
