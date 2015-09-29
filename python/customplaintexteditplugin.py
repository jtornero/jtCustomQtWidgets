# customplaintexteditplugin.py
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
from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin
from isplugin.customplaintextedit import CustomPlainTextEdit

class CustomPlainTextEditPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent = None):

        QPyDesignerCustomWidgetPlugin.__init__(self)

        self.initialized = False

    def initialize(self, formEditor):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):

        return self.initialized

    def createWidget(self, parent):
      
        return CustomPlainTextEdit(parent)

    def name(self):
        return "CustomPlainTextEdit"

    def group(self):
        return "JT Custom Widgets"
    
    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

    # Returns a short description of the custom widget for use in a tool tip.
    def toolTip(self):
        return "Custom PlainTextEdit with return pressed signals"

    # Returns a short description of the custom widget for use in a "What's
    # This?" help message for the widget.
    def whatsThis(self):
        return ""

    # Returns True if the custom widget acts as a container for other widgets;
    # otherwise returns False. Note that plugins for custom containers also
    # need to provide an implementation of the QDesignerContainerExtension
    # interface if they need to add custom editing support to Qt Designer.
    def isContainer(self):
        return False

    # Returns an XML description of a custom widget instance that describes
    # default values for its properties. Each custom widget created by this
    # plugin will be configured using this description.
    def domXml(self):
        return '<widget class="CustomPlainTextEdit" name="cusPlainTextEdit" />\n'

    # Returns the module containing the custom widget class. It may include
    # a module path.
    def includeFile(self):
        return "isplugin.customplaintextedit"


# Define the image used for the icon.
_logo_32x32_xpm = [
 "32 32 55 1",
"  c None", ". c #000000", "+ c #404040", "@ c #505050","# c #282828",
"$ c #060606", "% c #CCCCCC", "& c #FFFFFF", "* c #838383", "= c #161616",
"- c #111111", "; c #0B0B0B", "> c #888888", ", c #9D9D9D", "' c #9B9B9B",
") c #090909", "! c #2E2E2E", "~ c #292929", "{ c #030303", "] c #010101",
"^ c #D1D1D1", "/ c #7C7C7C", "( c #020202", "_ c #BFBFBF", ": c #DFDFDF",
"< c #FBFBFB", "[ c #323232", "} c #F5F5F5", "| c #626262", "1 c #E4E4E4",
"2 c #696969", "3 c #232323", "4 c #474747", "5 c #BDBDBD", "6 c #E5E5E5",
"7 c #4A4A4A", "8 c #444444", "9 c #B4B4B4", "0 c #FEFEFE", "a c #212121",
"b c #434343", "c c #ABABAB", "d c #858585", "e c #FCFCFC", "f c #C5C5C5",
"g c #0F0F0F", "h c #333333", "i c #898989", "j c #B1B1B1", "k c #BABABA",
"l c #9C9C9C", "m c #4E4E4E", "n c #171717", "o c #808080", "p c #141414",
"                                ",
"           ..........           ",
"         ..............         ",
"       ..................       ",
"      ....................      ",
"     ......................     ",
"    ........................    ",
"   .......+@@#.$@@@@@@@@@@@@@   ",
"   .......%&&*.=&&&&&&&&&&&&&   ",
"  ........%&&*.=&&&&&&&&&&&&&-  ",
"  ........%&&*.;>>>>,&&&'>>>>)  ",
" .........%&&*......!&&&~...... ",
" .........%&&*......!&&&~...... ",
" .........%&&*......!&&&~...... ",
" .........%&&*......!&&&~...... ",
" .........%&&*......!&&&~...... ",
" .........%&&*......!&&&~...... ",
" .........%&&*......!&&&~...... ",
" ....{]...^&&/......!&&&~...... ",
" .(_:<[..(}&&|......!&&&~...... ",
" ..1&&2..3&&&4......!&&&~...... ",
"  .5&&6789&&0a......!&&&~.....  ",
"  .b&&&&&&&&c.......!&&&~.....  ",
"   .de&&&&&fg.......!&&&~....   ",
"   ..hijklm(........nooop....   ",
"    ........................    ",
"     ......................     ",
"      ....................      ",
"       ..................       ",
"         ..............         ",
"           ..........           ",
"                                "]


_logo_pixmap = QtGui.QPixmap(_logo_32x32_xpm)
