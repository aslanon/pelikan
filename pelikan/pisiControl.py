#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under GPL v3
# Copyright 2013,Onur ASLAN <aslanon> <slnnronur@gmail.com>
# Please read the COPYING file.
#
#pisi/api.py

import pisi.errors
import pisi
import fcntl
import pisi.context as ctx

def pisi():
    global Clicked, PisiRun

    try:
        lock = file("/run/lock/subsys/pisi", 'w')
        Clicked = True
    except:
        Clicked = False
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        ctx.locked = True
        PisiRun = False
    except:
        if not ctx.locked:
            PisiRun = True
pisi()          
print "Pisi Status: %s" % PisiRun
print "Root Status: %s\n" % Clicked