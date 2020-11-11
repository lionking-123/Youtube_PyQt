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
FROM_RESET, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./UI/reset.ui"))
FROM_OPTIONS, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./UI/options.ui"))

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

# ============= Main Window Part ==============

class Main_window(QMainWindow, FROM_OPTIONS) :
    def __init__(self, parent = None) :
        super(Main_window, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        px = QPixmap("./images/main.png")
        px = px.scaled(self.size(), Qt.IgnoreAspectRatio)
        self.back.setPixmap(px)

        self.setWindowIcon(QIcon('./images/icon.png'))

        # btns = (self.users_btn, self.hoem_btn, self.trending_btn, self.categories_btn, self.recommend_btn, self.worldwide_btn, self.reco.btn)


    def closeEvent(self, event) :
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes :
            self.hide()
            self.dialog = Login(self)
            self.dialog.show()
            event.ignore()
        else :
            event.ignore()

# ============= Reset Window Part =============

class Reset_window(QMainWindow, FROM_RESET) :
    def __init__(self, parent = None) :
        super(Reset_window, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        px = QPixmap("./images/reset.png")
        px = px.scaled(self.size(), Qt.IgnoreAspectRatio)
        self.back.setPixmap(px)
        
        self.setWindowIcon(QIcon('./images/icon.png'))

        self.resetLink.clicked.connect(self.resetlink)
    
    def resetlink(self) :
        reply = QMessageBox.question(self, 'Password Reset', 'A password Reset link has been sent to your email',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    
    def closeEvent(self, event) :
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes :
            self.hide()
            self.dialog = Login(self)
            self.dialog.show()
            event.ignore()
        else :
            event.ignore()
    
# ============= Login Window part ==============

class Login(QMainWindow, FROM_MAIN) :
    def __init__(self, parent = None) :
        super(Login, self).__init__(parent)
        self.setupUi(self)

        px = QPixmap("./images/login.png")
        px = px.scaled(self.size(), Qt.IgnoreAspectRatio)
        self.back.setPixmap(px)
        
        self.setWindowIcon(QIcon('./images/icon.png'))

        self.login_btn.clicked.connect(self.load_main)
        self.reset_btn.clicked.connect(self.load_reset)
    
    def load_main(self) :
        self.hide()
        self.dialog = Main_window(self)
        self.dialog.show()
    
    def load_reset(self) :
        self.hide()
        self.dialog = Reset_window(self)
        self.dialog.show()
    
    def keyPressEvent(self, event) :
        if event.key() == Qt.Key_Tab :
            self.lineEdit.setFocus()
    
    def keyPressEvent(self, event) :
        if event.key() == Qt.Key_Enter :
            self.lineEdit.setFocus()
    
    def closeEvent(self, event) :
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the application?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes :
            self.close()
        else :
            event.ignore()

# ============= Splash part ============

class Splash(QMainWindow, FROM_SPLASH) :
    def __init__(self, parent = None) :
        super(Splash, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        px = QPixmap("./images/logo.png")
        px = px.scaled(self.splash_image.size(), Qt.IgnoreAspectRatio)
        self.splash_image.setPixmap(px)
        
        self.setWindowIcon(QIcon('./images/icon.png'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progress)
        progress.start()
    
    @pyqtSlot(int)
    def progress(self, i) :
        self.progressBar.setValue(i)
        self.progressBar.setFormat("Loading ...")
        if i == 100 :
            self.close()
            login = Login(self)
            login.show()

# ============= Application Start Point =============

def main() :
    app = QApplication(sys.argv)
    window = Splash()
    window.show()
    
    app.exec()

if __name__ == '__main__' :
    try :
        main()
    except Exception as why :
        print(why)
