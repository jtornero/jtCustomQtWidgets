# customdoubledpinbox.py
#
# This file is part of jtCustomQtWidgets
#
# Copyright (C) 2015 Jorge Tornero, http://imasdemase.com @imasdemase
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
from PyQt4 import QtCore, QtGui

class CustomDoubleSpinBox(QtGui.QDoubleSpinBox):
  
    __pyqtSignals__ = ("returnKeyPressed()","ctrlReturnKeyPressed()",)
    
    def __init__(self, parent=None, passFocusTo = None):
        
        QtGui.QDoubleSpinBox.__init__(self,parent)
        self.parent=parent
        
        if (parent != None and passFocusTo != None):
            self.setPassFocusTo(passFocusTo)
            
    def setPassFocusTo(self, passFocusToWidget):
        try:
            self.returnKeyPressed.disconnect()
        except:
            pass
        self._passFocusToWidget = passFocusToWidget
        try:
            self.returnKeyPressed.connect(self._passFocusToWidget.setFocus)
        except:
                
            print "Tried to pass a non-Qt widget object for focusing"
                
    def getPassFocusTo(self):
        return self._passFocusTo

    def keyPressEvent(self,event):
        
        if ((event.key()==QtCore.Qt.Key_Return and event.modifiers()==QtCore.Qt.ControlModifier)\
        or (event.key()==QtCore.Qt.Key_Enter and event.modifiers()==(QtCore.Qt.ControlModifier|QtCore.Qt.KeypadModifier))):
            event.accept()
            self.ctrlReturnKeyPressed.emit()
        elif (event.key()==QtCore.Qt.Key_Return or (event.key()==QtCore.Qt.Key_Enter)):
            event.accept()
            self.returnKeyPressed.emit()
        else:
            event.ignore()
            QtGui.QDoubleSpinBox.keyPressEvent(self,event)
    
    def focusInEvent(self,event):
        
        self.selectAll()
        QtGui.QDoubleSpinBox.focusInEvent(event)  
            