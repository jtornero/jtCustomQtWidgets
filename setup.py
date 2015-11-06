#!/usr/bin/env python

"""
setup.py

Packaging script for the example provided with the Qt Quarterly 26 article,
"Designing Custom Controls with PyQt".

Copyright (C) 2008 Nokia Corporation and/or its subsidiary(-ies).
Contact: Qt Software Information (qt-info@nokia.com)

This file is part of the documentation of Qt. It was originally
published as part of Qt Quarterly.

Commercial Usage
Licensees holding valid Qt Commercial licenses may use this file in
accordance with the Qt Commercial License Agreement provided with the
Software or, alternatively, in accordance with the terms contained in
a written agreement between you and Nokia.


GNU General Public License Usage
Alternatively, this file may be used under the terms of the GNU
General Public License versions 2.0 or 3.0 as published by the Free
Software Foundation and appearing in the file LICENSE.GPL included in
the packaging of this file.  Please review the following information
to ensure GNU General Public Licensing requirements will be met:
http://www.fsf.org/licensing/licenses/info/GPLv2.html and
http://www.gnu.org/copyleft/gpl.html.  In addition, as a special
exception, Nokia gives you certain additional rights. These rights
are described in the Nokia Qt GPL Exception version 1.3, included in
the file GPL_EXCEPTION.txt in this package.

Qt for Windows(R) Licensees
As a special exception, Nokia, as the sole copyright holder for Qt
Designer, grants users of the Qt/Eclipse Integration plug-in the
right for the Qt/Eclipse Integration to link to functionality
provided by Qt Designer and its related libraries.

If you are unsure which license is appropriate for your use, please
contact the sales department at qt-sales@nokia.com.
"""

import os, sys
from distutils.core import setup
import distutils.dist

try:
    import PyQt4.QtCore

except ImportError:
    print "PyQt4 not found in your system. Please check if PyQt4 is installed"
    print
    sys.exit(1)


class Distribution(distutils.dist.Distribution):

    def __init__(self, attrs = None):
    
        attrs = self.preprocess_attrs(attrs)
        distutils.dist.Distribution.__init__(self, attrs)
    
    def preprocess_attrs(self, attrs):
    
        attrs = self.process_ui_files(attrs)
        attrs = self.process_designer_plugins(attrs)
        
        return attrs
    
    def process_ui_files(self, attrs):
    
        if "ui_files" not in attrs:
            return attrs
        
        if "ui_package" not in attrs:
            return attrs
        
        ui_files = attrs["ui_files"]
        del attrs["ui_files"]
        
        ui_package = attrs["ui_package"].replace("/", os.sep)
        del attrs["ui_package"]
        
        if "build" not in attrs["script_args"]:
            return attrs
        
        import PyQt4.uic
        
        for path in ui_files:
        
            path = path.replace("/", os.sep)
            directory, file_name = os.path.split(path)
            file_name = "ui_" + file_name.replace(".ui", os.extsep+"py")
            output_path = os.path.join(ui_package, file_name)
            
            print "Compiling", path, "to", output_path
            input_file = open(path)
            output_file = open(output_path, "w")
            PyQt4.uic.compileUi(input_file, output_file)
            input_file.close()
            output_file.close()
        
        return attrs
    
    def process_designer_plugins(self, attrs):
    
        if "qt_designer_plugins" not in attrs:
            return attrs
        
        plugins = attrs["qt_designer_plugins"]
        del attrs["qt_designer_plugins"]
        
        if "install" not in attrs["script_args"]:
            return attrs
        
        from PyQt4.QtCore import QLibraryInfo
        info = QLibraryInfo.location(QLibraryInfo.PluginsPath)
        plugins_path = os.path.join(unicode(info), "designer", "python")
        if not os.path.exists(plugins_path):
            os.makedirs(plugins_path)
        
        for plugin in plugins:
        
            path = plugin.replace("/", os.sep)
            directory, file_name = os.path.split(path)
            output_path = os.path.join(plugins_path, file_name)
            print "Copying", path, "to", plugins_path
            open(output_path, "wb").write(open(path, "rb").read())
        
        return attrs


setup(
    name="isplugin",
    version="1.0",
    author="Jorge Tornero",
    author_email="jtorlistas@gmail.com",
    url="http://imasdemase.com",
    description="Custom PyQt4 widgets and plugin for us it in QtDesigner",
    long_description="",
    packages=["isplugin"],
    qt_designer_plugins=["python/itemlistselectorplugin.py",
                         "python/coordeditorplugin.py",
                         "python/customcombodbplugin.py",
                         "python/customlineeditplugin.py",
                         "python/customdateeditplugin.py",
                         "python/customcheckboxplugin.py",
                         "python/customspinboxplugin.py",
                         "python/customdoublespinboxplugin.py",
                         "python/customplaintexteditplugin.py"],
    distclass = Distribution
    )
