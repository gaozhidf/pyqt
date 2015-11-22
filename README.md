##Pyqt

###1. Prepare
apt-get install pyqt4-designer

apt-get install pyqt4-dev-tools

###2. Filetree
For example:

**Mynote**

 - app
    - view
        - \__init__.py
        - ui_mainwindow.py
        - ui_mainwindow.ui
    - \__init__.py
    - MainWindow.py
 - main.py
 
###3.  Transform
- Create .py from .ui  
pyuic4 ui_mainwindow.ui > ui_mainwindow.py  

- Create .py from .qrc  
pyrcc4 -o icon_rc.py icon.qrc
 
