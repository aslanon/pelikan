# -*- coding: utf-8 -*-
#Onur ASLAN <aslanon> <slnnronur@gmail.com>
 
import descriptionsDesktop 
from PyQt4 import QtCore, QtGui

def check(self):
	self.index = self.stackedWidget.currentIndex()  
	self.labelReady.show()
	if self.index == 0:
	    self.buttonNext.show()
	    self.statusLabel.setText("Choose your desktop")
	    self.screenLabel.setText("Welcome to Pelikan")
	    print "index 0: "+self.screenLabel.text()
	    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/icons/pelikan.png"))
	    self.buttonBack.hide()
	    
	if self.index == 1:
	    self.buttonNext.show()
	    self.statusLabel.setText("Download packages")
	    self.screenLabel.setText("Choose your desktop")            
	    print "index 1: "+self.screenLabel.text()
	    self.buttonBack.show()
	    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/icons/applications-other.png"))
	    desktopValue = self.comboBox.currentIndex()
	    if desktopValue == 0:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(""))
		    self.xdesktopLabel.setText("none")
		    self.buttonNext.setEnabled(False)
		    self.getinfoButton.setEnabled(False)
	    if desktopValue == 1:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Gnome.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/gnome.png"))
		    self.xdesktopLabel.setText("gnome")
		    self.buttonNext.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/gnome.png" /></p>"""+descriptionsDesktop.gnomeDescrip)               
	    if desktopValue == 2:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Xfce.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/xfce.png"))
		    self.xdesktopLabel.setText("xfce")
		    self.buttonNext.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/xfce.png" /></p>"""+descriptionsDesktop.xfceDescrip)
	    if desktopValue == 3:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/E17.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/enlightenment.png"))
		    self.xdesktopLabel.setText("enlightenment")
		    self.buttonNext.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/e17.png" /></p>"""+descriptionsDesktop.e17Descrip)
	    if desktopValue == 4:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Lxde.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/lxde.png"))
		    self.xdesktopLabel.setText("lxde")
		    self.buttonNext.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/lxde.png" /></p>"""+descriptionsDesktop.lxdeDescrip)
	    if desktopValue == 5:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Mate.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/mate.png"))
		    self.xdesktopLabel.setText("mate")
		    self.buttonNext.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/mate.png" /></p>"""+descriptionsDesktop.mateDescrip)
	    if desktopValue == 6:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Razor-qt.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/razor-qt.png"))
		    self.xdesktopLabel.setText("razor-qt")
		    self.buttonNext.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/razor-qt.png" /></p>"""+descriptionsDesktop.razor_qtDescrip)
	    if desktopValue == 7:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Cinnamon.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/cinnamon.png"))
		    self.xdesktopLabel.setText("cinnamon")
		    self.buttonNext.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/cinnamon.png" /></p>"""+descriptionsDesktop.cinnamonDescrip)
	    if desktopValue == 8:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Fluxbox.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/fluxbox.png"))
		    self.xdesktopLabel.setText("fluxbox")
		    self.buttonNext.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/fluxbox.png" /></p>"""+descriptionsDesktop.fluxboxDescrip)	
	self.labelReady.setText("'"+self.comboBox.currentText()+"' Selected")
			    
	if self.index == 2:
	    self.buttonBack.show()
	    self.buttonNext.hide()
	    self.statusLabel.setText("Completed!")
	    self.screenLabel.setText("Download packages")
	    print "index 3: "+self.screenLabel.text()
	    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/icons/applications-internet.png"))
	    self.addPackLabel.hide()
	    self.addPackButtonYes.hide()
	    self.addPackButtonNo.hide()
	    self.desktopLogoLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/"+self.xdesktopLabel.text()+".png"))
