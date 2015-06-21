# customcombodb.py
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
from PyQt4 import QtCore, QtGui, QtSql

class CustomComboDB(QtGui.QComboBox):
    
    __pyqtSignals__ = ("returnKeyPressed()",)
    
    def __init__(self, parent = None, db = None, table = None, indexColumn = None, showColumn = None, orderColumn = None, valueByDefault = True, defaultIndex = 1, tableFilter = None, initialized = True, passFocusTo = None):
      
      QtGui.QComboBox.__init__(self, parent)
      self.setDatabase(db)
      self.setTable(table)
      self.setIndexColumn(indexColumn)
      self.setShowColumn(showColumn)
      self.setValueByDefault(valueByDefault)
      self.setDefaultIndex(defaultIndex)
      if orderColumn == None:
            self.setOrderColumn(self.getIndexColumn())
      else:
            self.setOrderColumn(orderColumn)
      if initialized == True:
        self.setTableFilter(tableFilter)
        
      if (parent != None and passFocusTo != None):
        self.setPassFocusTo(passFocusTo)
        
    # WIDGET TO FOCUS AFTER PRESSING ENTER    
    def setPassFocusTo(self, passFocusTo):
      try:
        self.returnKeyPressed.disconnect()
      except:
        pass
      self._passFocusTo = widget
      try:
        self.returnKeyPressed.connect(passFocusTo.setFocus)
      except:
       
        print "Tried to pass a non-Qt widget object for focusing"
        
    def getPassFocusTo(self):
      return self._passFocusTo

    #DATABASE 
    
    def setDatabase(self, db):
      
      self._db = db
    
      
    def getDatabase(self):
    
      return self._db
    
    def setTable(self, table):
      
      self._table = table
      self.setIndexColumn(None)
      self.setShowColumn(None)
      self.setOrderColumn(None)
      self.startCombo()
      
      
    def getTable(self):
    
      return self._table
    
    #INDEX COLUMN
    def setIndexColumn (self, indexColumn):
        self._indexColumn = indexColumn
        
    def getIndexColumn (self):
        return self._indexColumn
    
    #SHOW COLUMN
    def setShowColumn (self, showColumn):
        self._showColumn = showColumn
        
    def getShowColumn (self):
        return self._showColumn
    
    #ORDER COLUMN
    def setOrderColumn (self, orderColumn = None):
        if orderColumn != None:
            self._orderColumn = orderColumn
        
        else:
            self._orderColumn = '1'
        
    def getOrderColumn (self):
        return self._orderColumn
    
    #VALUE BY DEFAULT
    def setValueByDefault (self, valueByDefault):
        self._valueByDefault = valueByDefault
        
    def getValueByDefault (self):
        return self._valueByDefault
      
    #DEFAULT INDEX
    def setDefaultIndex (self, defaultIndex):
        self._defaultIndex = defaultIndex
        
    def getDefaultIndex (self):
        return self._defaultIndex
      
    #TABLE FILTER   
    def setTableFilter(self, tableFilter):
      
      if tableFilter == None:
        #self._tableFilter = ''
        self._tableFilter = None
        
        
      else:
        self._tableFilter = tableFilter
      
    def getTableFilter(self):
        return self._tableFilter
 
    def startCombo(self):
      
      emptyModel = QtSql.QSqlTableModel()
      self.setModel(emptyModel)
      
      
      if None in (self._db, self._table, self._indexColumn, self._showColumn):

        return
      try:
        self.clear()
        hasFilter = self.getTableFilter()
        if hasFilter:
          tableFilter = "where %s" %hasFilter
        else:
          tableFilter = ""
        filterQuery = QtCore.QString("""SELECT DISTINCT %1, %2 FROM %3 %4 order by %5""").arg(self.getIndexColumn()).arg(self.getShowColumn()).arg(self.getTable()).arg(tableFilter).arg(self.getOrderColumn())
        print "FILTER->", filterQuery
        print 'DB->', self.getDatabase()
        self.filterQuery = QtSql.QSqlQuery(filterQuery,self._db)
        self.tblModel = QtSql.QSqlTableModel()
        self.tblModel.setQuery(self.filterQuery)
        self.setModel(self.tblModel)
        self.setModelColumn(1)
        
        if self.count() > 1:
          self.insertItem(0, self.tr(u'Select'))
        self.setCurrentIndex(0)
        
        if self.count() == 0:
          self.insertItem(0, self.tr(u'No Data'))
          self.noData = True
        else:
          self.noData = False
        self.setCurrentIndex(0)
                   
      except:
        QtGui.QMessageBox.information(None, self.tr(u"Cancel"), self.tr(u"Can't execute query"))
        print sys.exc_info()
        return
      
        
    def reset(self):
    
      self.setCurrentIndex(0)
    
    def getValueIndex(self):

      if self.count() == 1:
        selectedIndex = self.model().index(self.currentIndex(), 0)
        return self.model().data(selectedIndex).toString()
     
      elif self.count()>1 and self.currentIndex()!=0:
        selectedIndex=self.model().index(self.currentIndex(), 0)
        return self.model().data(selectedIndex).toString()
      
      else:
        return 'null'

     
    def keyPressEvent(self, event):
      
      self.blockSignals(True)
      if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
        #print self.currentIndex(), self.valueByDefault,self.count()

        if self.valueByDefault:
          if self.currentIndex() == 0:
            self.blockSignals(False)
            #iNSERTS VALUE BY DEFAULT
            self.setCurrentIndex(self._defaultIndex)
            self.returnKeyPressed.emit()
            
          elif self.currentIndex() > 0:
            event.accept()
            self.blockSignals(False)
            self.returnKeyPressed.emit()
        else:
          if self.currentIndex() == 0 and self.count() == 1 and self.noData == False:
            #print 'Dentro 1b-->',self.currentIndex()
            event.ignore()
            self.blockSignals(False)
            self.returnKeyPressed.emit()
            QtGui.QComboBox.keyPressEvent(self, event)
          elif self.currentIndex()>0:
            #print 'Dentro 2b-->',self.currentIndex()
            event.accept()
            self.blockSignals(False)
            self.returnKeyPressed.emit()
          
      else:
        event.ignore()
        QtGui.QComboBox.keyPressEvent(self, event)
        self.blockSignals(False)

    table = QtCore.pyqtProperty(str,getTable, setTable)
    indexColumn = QtCore.pyqtProperty(str,getIndexColumn, setIndexColumn)
    showColumn = QtCore.pyqtProperty(str,getShowColumn, setShowColumn)
    orderColumn = QtCore.pyqtProperty(str,getOrderColumn, setOrderColumn)
    valueByDefault = QtCore.pyqtProperty(bool,getValueByDefault, setValueByDefault)
    defaultIndex = QtCore.pyqtProperty(int,getDefaultIndex, setDefaultIndex)
    tableFilter = QtCore.pyqtProperty(str,getTableFilter, setTableFilter)