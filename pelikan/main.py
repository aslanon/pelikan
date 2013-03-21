#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under GPL v3
# Copyright 2013, Onur ASLAN <slnnronur@gmail.com>
#
# Please read the COPYING file.

import sys, signal
from PyQt4 import QtCore
from PyQt4 import QtGui
from scrPelikan import MainWindow
import icons_rc

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtGui.QApplication(sys.argv)

    app.setApplicationName("pelikan")
    app.setOrganizationName("pelikan")
    mainWindow = MainWindow()
    mainWindow.show()
    return app.exec_()

if __name__ == "__main__":
    main()