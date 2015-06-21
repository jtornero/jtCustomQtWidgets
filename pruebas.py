#!/usr/bin/env python

# Just an example to see itemListSelector working

import sys
from PyQt4 import QtCore, QtGui
import isplugin.itemlistselector as il


app=QtGui.QApplication(sys.argv)

listOfItems=['Apples','Carrots','Pears','Lemons','Strawberries']


b=il.ItemListSelector()
b.setOriginalItems(listOfItems)


b.show()

sys.exit(app.exec_())