# customlineedit.py
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

class CustomLineEdit(QtGui.QLineEdit):
  
    __pyqtSignals__ = ("returnKeyPressed()","ctrlReturnKeyPressed()",)
    
    def __init__(self, parent=None , dataType=None, passFocusTo = None):
        
        QtGui.QLineEdit.__init__(self,parent)
        self.parent=parent
        self.setDecimals(3)
        self.setDataType(dataType)
    
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

    def setDataType(self,dataType):
        
        if dataType==None:
            
            self._dataType=None
            return
        
        self._dataType = dataType
        if self._dataType==1:
            #VALIDATE 0-9999, 3 decimals
            self.validator=QtCore.QRegExp(('^(([0-9]{0,4})?(\.[0-9]{0,%i})?)$' %(self.getDecimals()))) 
        elif self._dataType==2:
            #VALIDATES 0-999999
            self.validator=QtCore.QRegExp('^(([0-9]{0,6})?)$') 
        elif self._dataType==3:
            #VALIDATES 0-9999, 3 DECIMALS PLUS SIGN
            self.validator=QtCore.QRegExp(('^(([-]?[0-9]{0,4})?(\.[0-9]{0,%i})?)$' %(self.getDecimals())))
            
        elif self._dataType==4:
            self.validator=QtCore.QRegExp('^(([-]?[0-9]{0,6})?)$') #VALIDATES 0-999999 PLUS SIGN
        
        self.setValidator(QtGui.QRegExpValidator(self.validator,self))
    
    def getDataType(self):
        
        return self._dataType
    
    def setDecimals(self,decimals):
        
        self._decimals=decimals
        self.setDataType(1)
        
    def getDecimals(self):
        
        return self._decimals

    def keyPressEvent(self,event):
        
        if ((event.key()==QtCore.Qt.Key_Return and event.modifiers()==QtCore.Qt.ControlModifier)\
        or (event.key()==QtCore.Qt.Key_Enter and event.modifiers()==(QtCore.Qt.ControlModifier|QtCore.Qt.KeypadModifier))):
            event.accept()
            self.ctrlReturnKeyPressed.emit()
        elif (event.key()==QtCore.Qt.Key_Return or (event.key()==QtCore.Qt.Key_Enter)):
            print 'RETORNO'
            event.accept()
            self.returnKeyPressed.emit()
        else:
            event.ignore()
            QtGui.QLineEdit.keyPressEvent(self,event)
    
    dataType = QtCore.pyqtProperty(int, getDataType, setDataType)
    decimals = QtCore.pyqtProperty(int, getDecimals, setDecimals)
    
            