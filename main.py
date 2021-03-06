#!/usr/bin/env python3

import lib.db as db
from gui.faktureramerawindow import FaktureraMeraWindow


from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    if not db.openDatabase():  
        sys.exit(1)

    faktureramera = FaktureraMeraWindow() 
    
    faktureramera.show()    

    sys.exit(app.exec_())
