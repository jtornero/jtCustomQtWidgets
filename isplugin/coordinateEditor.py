# coordinateEditor.py
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

import math
from PyQt4 import QtCore, QtGui


class customCombo(QtGui.QComboBox):
      
      retPressed = QtCore.pyqtSignal()
      
      def __init__(self,parent):
        QtGui.QComboBox.__init__(self, parent)
        
      def keyPressEvent(self,event):
        #print event.key()
        if (event.key()==QtCore.Qt.Key_Return or event.key()==QtCore.Qt.Key_Enter):
          self.retPressed.emit()
          event.accept()
        else:
          event.ignore()
          QtGui.QComboBox.keyPressEvent(self,event)
      def reset(self):
        self.model().clear()
        self.setCurrentIndex(0)

class coordDialog(QtGui.QDialog):

    def __init__(self,parent, mode = None):
      QtGui.QDialog.__init__(self,parent)
      self.conversion=-1
      self.setModal(True)
      self.layout=QtGui.QVBoxLayout(self)
      self.mode = mode
      self.setupUi()
      
      
    def setupUi(self):
      
      self.labelHemisphere=QtGui.QLabel(self.tr(u"Hemisphere"))
      self.comboHemisphere=customCombo(self)
      
      if self.mode=='LAT':
        self.comboHemisphere.addItem(u'N')
        self.comboHemisphere.addItem(u'S')
        self.setWindowTitle(self.tr(u'LATITUDE'))
        self.validateIntegerG=QtCore.QRegExp('^?([1]?[0-7]?[0-9]|[1-9]?[0-9]|180)?$') #VALIDA 0-180 ENTEROS
        self.validateDoubleG=QtCore.QRegExp('^(([1]?[0-7]?[0-9]|[1-9]?[0-9])?(\.[0-9]{0,8})?|(180))?$') #VALIDA 0-180 8 DECIMALES
      
      elif self.mode=='LON':
        self.comboHemisphere.addItem(u'E')
        self.comboHemisphere.addItem(u'W')
        self.setWindowTitle(self.tr(u'LONGITUDE'))
        self.comboHemisphere.setCurrentIndex(1)#Para ahorrar tiempo ya que todas las coordenadas del GdC son W
        self.validateIntegerG=QtCore.QRegExp('^([1-8]?[0-9]|90)?$') #VALIDA 0-90 ENTEROS
        self.validateDoubleG=QtCore.QRegExp('^(([1-8]?[0-9])(\.[0-9]{0,8})?|(90)?)?$') #VALIDA 0-90 DECIMAL
      else:
        return
      
      self.labelCoordFormat=QtGui.QLabel(self.tr(u"Format"))
      self.comboCoordFormat=customCombo(self)
      self.comboCoordFormat.addItem(self.tr(u"DD.DDDD"))
      self.comboCoordFormat.addItem(self.tr(u"DD MM.MMMM"))
      self.comboCoordFormat.addItem(self.tr(u"DD MM SS.SSSS"))
      
      self.comboCoordFormat.setCurrentIndex(1) # Para facilitar la introduccion de datos
          
      self.validateIntegerMS=QtCore.QRegExp('^([1-5]?[0-9])?$') #VALIDA 0-59 ENTEROS
      self.validateDoubleMS=QtCore.QRegExp('^(([1-5]?[0-9])(\.[0-9]{0,8})?)?$') #VALIDA 0-59 DECIMAL
      
        
      
      self.degreesText=QtGui.QLineEdit(self)
      self.minutesText=QtGui.QLineEdit(self)
      self.secondsText=QtGui.QLineEdit(self)
      
      
      self.layout.addWidget(self.labelHemisphere)
      self.layout.addWidget(self.comboHemisphere)
      self.layout.addWidget(self.labelCoordFormat)
      self.layout.addWidget(self.comboCoordFormat)
      self.layout.addWidget(self.degreesText)
      self.layout.addWidget(self.minutesText)
      self.layout.addWidget(self.secondsText)
      
      
      self.comboHemisphere.retPressed.connect(self.comboCoordFormat.setFocus)
      self.comboCoordFormat.retPressed.connect(self.activateFields)
      self.comboCoordFormat.retPressed.connect(self.degreesText.setFocus)
      self.comboCoordFormat.activated.connect(self.activateFields)
      self.degreesText.returnPressed.connect(self.passDegreesFocus)
      self.minutesText.returnPressed.connect(self.passMinutesFocus)
      self.secondsText.returnPressed.connect(self.passSecondsFocus)
      self.activateFields()
      
    
    def passDegreesFocus(self):
    
      if self.conversion==0:
        self.value=self.degreesText.text().toFloat()[0]
        if self.comboHemisphere.currentIndex()==0:
          pass
        elif self.comboHemisphere.currentIndex()==1:
          self.value=self.value*(-1)
      
        self.done(1)
      else:
        self.minutesText.setFocus()
        
    def passMinutesFocus(self):
      
      if self.conversion==1:
        degrees=self.degreesText.text().toInt()[0]
        minutes=self.minutesText.text().toFloat()[0]
        self.value=degrees+(minutes/60.0)
        if self.comboHemisphere.currentIndex()==0:
          pass
        elif self.comboHemisphere.currentIndex()==1:
          self.value=self.value*(-1)
          
        self.done(1)
      else:
        self.secondsText.setFocus()
      
      
    
    def passSecondsFocus(self):
      if self.conversion==2:
        degrees=self.degreesText.text().toInt()[0]
        minutes=self.minutesText.text().toInt()[0]
        seconds=self.secondsText.text().toFloat()[0]
        self.value=degrees+((minutes/60.0)+seconds/3600.0)
        if self.comboHemisphere.currentIndex()==0:
          pass
        elif self.comboHemisphere.currentIndex()==1:
          self.value=self.value*(-1)
      
        self.done(1)
      
      

    def activateFields(self):
      
      if self.comboCoordFormat.currentIndex()==0:
        self.conversion=0
        self.degreesText.setEnabled(True)
        self.degreesText.setValidator(QtGui.QRegExpValidator(self.validateDoubleG,self))
        self.minutesText.setEnabled(False)
        self.secondsText.setEnabled(False)
        
      elif self.comboCoordFormat.currentIndex()==1:
        self.conversion=1
        self.degreesText.setEnabled(True)
        self.degreesText.setValidator(QtGui.QRegExpValidator(self.validateIntegerG,self))
        self.minutesText.setEnabled(True)
        self.minutesText.setValidator(QtGui.QRegExpValidator(self.validateDoubleMS,self))
        self.secondsText.setEnabled(False)
        
      elif self.comboCoordFormat.currentIndex()==2:
        self.conversion=2
        self.degreesText.setEnabled(True)
        self.degreesText.setValidator(QtGui.QRegExpValidator(self.validateIntegerG,self))
        self.minutesText.setEnabled(True)
        self.minutesText.setValidator(QtGui.QRegExpValidator(self.validateIntegerMS,self))
        self.secondsText.setEnabled(True)
        self.secondsText.setValidator(QtGui.QRegExpValidator(self.validateDoubleMS,self))



class CoordinateEditor(QtGui.QLineEdit):
  
  
  def __init__(self, parent = None, displayMode='DM'):
    
    QtGui.QLineEdit.__init__(self, parent)
    self._mode=None
    self._displayMode=displayMode
    self.coordinate=0
    self.show()
  
  def keyPressEvent(self, event):
    
    if (event.key() == QtCore.Qt.Key_M and event.modifiers() == QtCore.Qt.ControlModifier and self._mode!=None):
      self.getCoords()
    
  def getCoords(self):
    self.coordValue=coordDialog(self,self.getEditorMode())
    a = self.coordValue.exec_()
    if a==1 and self.coordValue.value != 0:
      
        self.setCoordinate(self.coordValue.value,precision=8)
        
    else:
      self.setText('')
  
  def setCoordinate(self, coordinate):
    
    self.coordinate = coordinate
    
    degree_fraction, degrees = math.modf(coordinate)
    degrees=int(degrees)
    
    decimal_minutes=abs(degree_fraction*60)
    
    minute_fraction, minutes = math.modf(decimal_minutes)
    minutes=int(minutes)
    
    decimal_seconds=minute_fraction*60
       
    decString=(u"{0}".format(coordinate))
    dmString=(u"{0}\u00b0 {1}'".format(degrees, decimal_minutes))
    dmsString=(u"{0}\u00b0 {1}' {2}''".format(degrees, minutes, decimal_seconds))
    
    print '***********************',coordinate,decString,dmString,dmsString
    
    if self.displayMode=='DEC':
        print 'DEC'
        self.setText(decString)
        
    elif self.displayMode=='DM':
        print 'DM'
        self.setText(dmString)
    
    elif self.displayMode=='DMS':
        print 'DMS'
        self.setText(dmsString)
    
    self.setToolTip(u"DEC: {0}\nDM: {1}\nDMS: {2}".format(decString,dmString,dmsString))
    
  def getCoordinate(self):
      return self.coordinate
  
  def setEditorMode(self, mode):
    self._mode = mode
    
  def getEditorMode(self):
    return self._mode
  
  def setDisplayMode(self, mode):
    self._displayMode = mode
    
  def getDisplayMode(self):
    return self._displayMode
  
  mode = QtCore.pyqtProperty(str,getEditorMode, setEditorMode)
  displayMode = QtCore.pyqtProperty(str,getDisplayMode, setDisplayMode)