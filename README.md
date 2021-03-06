JT PyQt4 Custom Widgets
=======================

This is a small and (I hope) growing collection of PyQt4 custom widgets for use in your projects. 
The good point is that they are also QtDesigner plugins, so you can use them in QtDesigner as any other widget, just drag and drop.

One of the advantages of this implementation is that eases focus-chainage of widgets. Some of them has the method passFocusTo which
makes possible to define which widget is going to recive the applicaton focus using its method setPassFocusTo().

So far, the widgets are:

-    coordinateeditor: Derived from QLineEdit, it makes possible to type a geographic coordinate (Latitude or longitude) in several formats.
-    customcombodb: Derived from QComboBox, it makes possible to resolve foreign keys to choose values for a field in a database table. and also has pass-focus-to capability
-    itemlistselector: Two QListWidgets with buttons which make possible move elements from one list to the other.
-    customlineedit: Derived from QLineEdit, provides such a widget with pass-focus-to capabilites as well as multi-validation (real,integer)
-    customcheckbox: Derived from QCheckBox, provides such a widget with pass-focus-to capabilites
-    customplaintextedit:Derived from QPlainTextEdit, provides such a widget with pass-focus-to capabilites
-    customdateedit:Derived from QDateEdit, provides such a widget with pass-focus-to capabilites
-    customspinbox: Derived from QSpinBox, provides such a widget with pass-focus-to capabilites
-    customsdoublepinbox: Derived from QDoubleSpinBox, provides such a widget with pass-focus-to capabilites


Copyright/License
=================

JTCustomQTWidgets has been developed by Jorge Tornero.

(C) 2015 Jorge Tornero, http://imasdemase.com @imasdemase

JTCustomQTWidgets is released under the terms of the

**GNU GENERAL PUBLIC LICENSE**

Version 3, 29 June 2007

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see:

**http://www.gnu.org/licenses**


Notice: As of 2015/06/22, I have some concerns regarding setup script license. They will be fixed as soon as possible.

Documentation
=============

The code is not as well documented as it would be desirable to be, but efforts are being made to improve it.


Installation/Dependencies
=========================

You must have PyQt4 installed in your system

To install, run as root:

    python setup.py install