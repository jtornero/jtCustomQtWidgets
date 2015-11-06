# itemlistselector.py
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


from PyQt4 import QtCore, QtGui

class ItemListSelector(QtGui.QWidget):
    """This class implements a item selector based in
    two lists of items implemented with QListWidget.
    User can send items from on list to another and finally
    get the list of selected items."""
    __pyqtSignals__ = ("cleared()","selectionChanged()")
    
    
    def __init__(self, parent=None):
    
        QtGui.QWidget.__init__(self,parent)
        
        
        self._mode=None
        
        self.setupUi()
        self.show()

    def setupUi(self):

        self.layout=QtGui.QGridLayout(self)
        
        # These are the two lists
        
        self.originalItemsWidget=QtGui.QListWidget()
        self.selectedItemsWidget=QtGui.QListWidget()
        
        # Labels for the lists
        
        self.originalItemsLabel = QtGui.QLabel()
        self.selectedItemsLabel = QtGui.QLabel()
        # Making possible multiple item selection
        
        self.originalItemsWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.selectedItemsWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        
        # Operation buttons
        self.selectManyButton=QtGui.QPushButton('>')
        self.selectAllButton=QtGui.QPushButton('>>')
        self.unselectManyButton=QtGui.QPushButton('<')
        self.unselectAllButton=QtGui.QPushButton('<<')
        
        # Adding all to layout
        
        self.layout.addWidget(self.originalItemsLabel,0,0,1,1)
        self.layout.addWidget(self.originalItemsWidget,1,0,8,1)
        self.layout.addWidget(self.selectManyButton,2,1,1,1)
        self.layout.addWidget(self.unselectManyButton,3,1,1,1)
        self.layout.addWidget(self.selectAllButton,6,1,1,1)
        self.layout.addWidget(self.unselectAllButton,7,1,1,1)
        self.layout.addWidget(self.selectedItemsLabel,0,2,1,1)
        self.layout.addWidget(self.selectedItemsWidget,1,2,8,1)
        
        # Signal-slot connections, for the buttons
        self.selectManyButton.clicked.connect(self.toSelected)
        self.selectAllButton.clicked.connect(self.toSelectedAll)
        self.unselectManyButton.clicked.connect(self.toOriginal)
        self.unselectAllButton.clicked.connect(self.toOriginalAll)
        
        # Support for mouse double click item moving
        self.originalItemsWidget.doubleClicked.connect(self.toSelected)
        self.selectedItemsWidget.doubleClicked.connect(self.toOriginal)
        
    def setOriginalItems(self,itemList):
        
        self.clearWidgets()
        self.originalItemsWidget.addItems(itemList)  
        
    def setOriginalItemsLabel(self,label=''):
        
        self._originalItemsLabelText=label
        self.originalItemsLabel.setText("<center><b>%s</b></center>" %label)
    
    def getOriginalItemsLabel(self):
        
        return self._originalItemsLabelText
    
    def setSelectedItemsLabel(self,label=''):
        
        self._selectedItemsLabelText=label
        self.selectedItemsLabel.setText("<center><b>%s</b></center>" %label)
    
    def getSelectedItemsLabel(self):
        
        return self._selectedItemsLabelText
    
    
    def clearWidgets(self):
        self.originalItemsWidget.clear()
        self.selectedItemsWidget.clear()
        self.cleared.emit()
        
    def toSelected(self):
                          
        selectedItems=[self.originalItemsWidget.takeItem(self.originalItemsWidget.row(item))\
                       for item in self.originalItemsWidget.selectedItems()]
        
        for item in selectedItems:
            self.selectedItemsWidget.addItem(item)
        
        self.originalItemsWidget.sortItems()
        self.selectedItemsWidget.sortItems()
        self.selectionChanged.emit()
        

    
    def toOriginal(self):
        
        selectedItems=[self.selectedItemsWidget.takeItem(self.selectedItemsWidget.row(item))
                      for item in self.selectedItemsWidget.selectedItems()]
        
        for item in selectedItems:
            self.originalItemsWidget.addItem(item)
    
        self.originalItemsWidget.sortItems()
        self.selectedItemsWidget.sortItems()
        self.selectionChanged.emit()
        
    
    def toSelectedAll(self):
        
        items=[self.originalItemsWidget.takeItem(self.originalItemsWidget.row(item))
              for item in self.originalItemsWidget.findItems('*', QtCore.Qt.MatchWildcard)]
        
        for item in items:
            self.selectedItemsWidget.addItem(item)
    
        
        self.selectedItemsWidget.sortItems()
        self.selectionChanged.emit()
    
    def toOriginalAll(self):
        
        items=[self.selectedItemsWidget.takeItem(self.selectedItemsWidget.row(item))
              for item in self.selectedItemsWidget.findItems('*', QtCore.Qt.MatchWildcard)]
        
        for item in items:
            self.originalItemsWidget.addItem(item)
        
        self.originalItemsWidget.sortItems()
        self.selectionChanged.emit()
    
    def getItemStrings(self):
        
        itemStrings=[str(item.text())
                    for item in self.selectedItemsWidget.findItems('*', QtCore.Qt.MatchWildcard)]
        return itemStrings
        
    def setEditorMode(self, mode):
          
        self._mode = mode
    
    def getEditorMode(self):
    
        return self._mode
  
    mode = QtCore.pyqtProperty(str,getEditorMode, setEditorMode)
    oriItemsLabel = QtCore.pyqtProperty(str,getOriginalItemsLabel, setOriginalItemsLabel)
    selItemsLabel = QtCore.pyqtProperty(str,getSelectedItemsLabel, setSelectedItemsLabel)
    