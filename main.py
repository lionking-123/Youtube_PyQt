from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from functools import partial
# from analytics import  AnalyticsWidget

import os
import sys
import time

# ============= Const variables define part =============

FROM_SPLASH, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./UI/splash.ui"))
FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./UI/main.ui"))
# FROM_RESET, _ = loadUiType(os.path.join(os.path.dirname(__file__), "reset.ui"))
# FROM_OPTIONS, _ = loadUiType(os.path.join(os.path.dirname(__file__), "options.ui"))

# ============= Thread Class ============

class ThreadProgress(QThread) :
    mysignal = pyqtSignal(int)
    
    def __init__(self, parent = None) :
        QThread.__init__(self, parent)
    
    def run(self) :
        i = 0
        while i < 101 :
            time.sleep(0.1)
            self.mysignal.emit(i)
            i += 1

# ============= Main Window part ==============

class Main(QMainWindow, FROM_MAIN) :
    def __init__(self, parent = None) :
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.login_btn.clicked.connect(self.load_main)
        self.reset_btn.clicked.connect(self.load_reset)
    
    def load_main(self) :
        QMessageBox.about(self, "Alert", "Load Main clicked!")
    
    def load_reset(self) :
        QMessageBox.about(self, "Alert", "Load Reset clicked!")
    
    def keyPressEvent(self, event) :
        if event.key() == Qt.Key_Tab :
            self.lineEdit.setFocus()
    
    def keyPressEvent(self, event) :
        if event.key() == Qt.Key_Enter :
            self.lineEdit.setFocus()

# ============= Splash part ============

class Splash(QMainWindow, FROM_SPLASH) :
    def __init__(self, parent = None) :
        super(Splash, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progress)
        progress.start()
    
    @pyqtSlot(int)
    def progress(self, i) :
        self.progressBar.setValue(i)
        self.progressBar.setFormat("Loading")
        if i == 100 :
            main = Main(self)
            self.close()
            main.show()

# ============= Application Start Point =============

def main() :
    app = QApplication(sys.argv)
    window = Splash()
    window.show()
    
    app.exec()

if __name__ == '__main__' :
    try :
        main()
    except Execption as why :
        print(why)
