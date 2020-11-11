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

        self.setWindowIcon(QIcon('./images/icon.png'))

        btns = (self.users_btn, self.home_btn, self.trending_btn, self.categories_btn, self.recommend_btn, self.worldwide_btn, self.reco_btn)
        for i, btn in enumerate(btns) :
            btn.clicked.connect(partial(self.stackedWidget.setCurrentIndex, i))
        
        self.users.setStyleSheet("background-color : red;")
        self.users_label.setStyleSheet("background-color : rgba(255, 255, 255, 50);")
        self.users_btn.setIcon(QIcon('./images/users_pressed.png'))
        self.users_btn.clicked.connect(self.users_button_fn)
        self.home_btn.clicked.connect(self.home_button_fn)
        self.trending_btn.clicked.connect(self.trending_button_fn)
        self.recommend_btn.clicked.connect(self.recommend_button_fn)
        self.categories_btn.clicked.connect(self.categories_button_fn)
        self.worldwide_btn.clicked.connect(self.worldwide_button_fn)
        self.reco_btn.clicked.connect(self.reco_button_fn)
    
    def users_button_fn(self) :
        self.users.setStyleSheet("background-color : red;")
        self.users_label.setStyleSheet("background-color : rgba(255, 255, 255, 50);")
        self.users_btn.setIcon(QIcon('./images/users_pressed.png'))

        self.home.setStyleSheet("background-color : transparent;")
        self.home_label.setStyleSheet("background-color : transparent;")
        self.home_btn.setIcon(QIcon('./images/home_icon.png'))

        self.trending.setStyleSheet("background-color : transparent;")
        self.trending_label.setStyleSheet("background-color : transparent;")
        self.trending_btn.setIcon(QIcon('./images/trending_icon.png'))

        self.categories.setStyleSheet("background-color : transparent;")
        self.categories_label.setStyleSheet("background-color : transparent;")
        self.categories_btn.setIcon(QIcon('./images/categories_icon.png'))

        self.recommend.setStyleSheet("background-color : transparent;")
        self.recommend_label.setStyleSheet("background-color : transparent;")
        self.recommend_btn.setIcon(QIcon('./images/wifi_icon.png'))

        self.worldwide.setStyleSheet("background-color : transparent;")
        self.worldwide_label.setStyleSheet("background-color : transparent;")
        self.worldwide_btn.setIcon(QIcon('./images/global_icon.png'))

        self.reco.setStyleSheet("background-color : transparent;")
        self.reco_label.setStyleSheet("background-color : transparent;")
        self.reco_btn.setIcon(QIcon('./images/recommend_icon.png'))

    def home_button_fn(self) :
        self.users.setStyleSheet("background-color : transparent;")
        self.users_label.setStyleSheet("background-color : transparent;")
        self.users_btn.setIcon(QIcon('./images/users_icon.png'))

        self.home.setStyleSheet("background-color : #70ad47;")
        self.home_label.setStyleSheet("background-color : rgba(255, 255, 255, 50);")
        self.home_btn.setIcon(QIcon('./images/home_pressed.png'))

        self.trending.setStyleSheet("background-color : transparent;")
        self.trending_label.setStyleSheet("background-color : transparent;")
        self.trending_btn.setIcon(QIcon('./images/trending_icon.png'))

        self.categories.setStyleSheet("background-color : transparent;")
        self.categories_label.setStyleSheet("background-color : transparent;")
        self.categories_btn.setIcon(QIcon('./images/categories_icon.png'))

        self.recommend.setStyleSheet("background-color : transparent;")
        self.recommend_label.setStyleSheet("background-color : transparent;")
        self.recommend_btn.setIcon(QIcon('./images/wifi_icon.png'))

        self.worldwide.setStyleSheet("background-color : transparent;")
        self.worldwide_label.setStyleSheet("background-color : transparent;")
        self.worldwide_btn.setIcon(QIcon('./images/global_icon.png'))

        self.reco.setStyleSheet("background-color : transparent;")
        self.reco_label.setStyleSheet("background-color : transparent;")
        self.reco_btn.setIcon(QIcon('./images/recommend_icon.png'))
    
    def trending_button_fn(self) :
        self.users.setStyleSheet("background-color : transparent;")
        self.users_label.setStyleSheet("background-color : transparent;")
        self.users_btn.setIcon(QIcon('./images/users_icon.png'))

        self.home.setStyleSheet("background-color : transparent;")
        self.home_label.setStyleSheet("background-color : transparent;")
        self.home_btn.setIcon(QIcon('./images/home_icon.png'))

        self.trending.setStyleSheet("background-color : red;")
        self.trending_label.setStyleSheet("background-color : rgba(255, 255, 255, 50);")
        self.trending_btn.setIcon(QIcon('./images/trending_pressed.png'))

        self.categories.setStyleSheet("background-color : transparent;")
        self.categories_label.setStyleSheet("background-color : transparent;")
        self.categories_btn.setIcon(QIcon('./images/categories_icon.png'))

        self.recommend.setStyleSheet("background-color : transparent;")
        self.recommend_label.setStyleSheet("background-color : transparent;")
        self.recommend_btn.setIcon(QIcon('./images/wifi_icon.png'))

        self.worldwide.setStyleSheet("background-color : transparent;")
        self.worldwide_label.setStyleSheet("background-color : transparent;")
        self.worldwide_btn.setIcon(QIcon('./images/global_icon.png'))

        self.reco.setStyleSheet("background-color : transparent;")
        self.reco_label.setStyleSheet("background-color : transparent;")
        self.reco_btn.setIcon(QIcon('./images/recommend_icon.png'))
    
    def categories_button_fn(self) :
        self.users.setStyleSheet("background-color : transparent;")
        self.users_label.setStyleSheet("background-color : transparent;")
        self.users_btn.setIcon(QIcon('./images/users_icon.png'))

        self.home.setStyleSheet("background-color : transparent;")
        self.home_label.setStyleSheet("background-color : transparent;")
        self.home_btn.setIcon(QIcon('./images/home_icon.png'))

        self.trending.setStyleSheet("background-color : transparent;")
        self.trending_label.setStyleSheet("background-color : transparent;")
        self.trending_btn.setIcon(QIcon('./images/trending_icon.png'))

        self.categories.setStyleSheet("background-color : #ffc000;")
        self.categories_label.setStyleSheet("background-color : rgba(255, 255, 255, 50);")
        self.categories_btn.setIcon(QIcon('./images/categories_pressed.png'))

        self.recommend.setStyleSheet("background-color : transparent;")
        self.recommend_label.setStyleSheet("background-color : transparent;")
        self.recommend_btn.setIcon(QIcon('./images/wifi_icon.png'))

        self.worldwide.setStyleSheet("background-color : transparent;")
        self.worldwide_label.setStyleSheet("background-color : transparent;")
        self.worldwide_btn.setIcon(QIcon('./images/global_icon.png'))

        self.reco.setStyleSheet("background-color : transparent;")
        self.reco_label.setStyleSheet("background-color : transparent;")
        self.reco_btn.setIcon(QIcon('./images/recommend_icon.png'))
    
    def recommend_button_fn(self) :
        self.users.setStyleSheet("background-color : transparent;")
        self.users_label.setStyleSheet("background-color : transparent;")
        self.users_btn.setIcon(QIcon('./images/users_icon.png'))

        self.home.setStyleSheet("background-color : transparent;")
        self.home_label.setStyleSheet("background-color : transparent;")
        self.home_btn.setIcon(QIcon('./images/home_icon.png'))

        self.trending.setStyleSheet("background-color : transparent;")
        self.trending_label.setStyleSheet("background-color : transparent;")
        self.trending_btn.setIcon(QIcon('./images/trending_icon.png'))

        self.categories.setStyleSheet("background-color : transparent;")
        self.categories_label.setStyleSheet("background-color : transparent;")
        self.categories_btn.setIcon(QIcon('./images/categories_icon.png'))

        self.recommend.setStyleSheet("background-color : red;")
        self.recommend_label.setStyleSheet("background-color : rgba(255, 255, 255, 50);")
        self.recommend_btn.setIcon(QIcon('./images/wifi_pressed.png'))

        self.worldwide.setStyleSheet("background-color : transparent;")
        self.worldwide_label.setStyleSheet("background-color : transparent;")
        self.worldwide_btn.setIcon(QIcon('./images/global_icon.png'))

        self.reco.setStyleSheet("background-color : transparent;")
        self.reco_label.setStyleSheet("background-color : transparent;")
        self.reco_btn.setIcon(QIcon('./images/recommend_icon.png'))
    
    def worldwide_button_fn(self) :
        self.users.setStyleSheet("background-color : transparent;")
        self.users_label.setStyleSheet("background-color : transparent;")
        self.users_btn.setIcon(QIcon('./images/users_icon.png'))

        self.home.setStyleSheet("background-color : transparent;")
        self.home_label.setStyleSheet("background-color : transparent;")
        self.home_btn.setIcon(QIcon('./images/home_icon.png'))

        self.trending.setStyleSheet("background-color : transparent;")
        self.trending_label.setStyleSheet("background-color : transparent;")
        self.trending_btn.setIcon(QIcon('./images/trending_icon.png'))

        self.categories.setStyleSheet("background-color : transparent;")
        self.categories_label.setStyleSheet("background-color : transparent;")
        self.categories_btn.setIcon(QIcon('./images/categories_icon.png'))

        self.recommend.setStyleSheet("background-color : transparent;")
        self.recommend_label.setStyleSheet("background-color : transparent;")
        self.recommend_btn.setIcon(QIcon('./images/wifi_icon.png'))

        self.worldwide.setStyleSheet("background-color : #2e75b6;")
        self.worldwide_label.setStyleSheet("background-color : rgba(255, 255, 255, 50);")
        self.worldwide_btn.setIcon(QIcon('./images/global_pressed.png'))

        self.reco.setStyleSheet("background-color : transparent;")
        self.reco_label.setStyleSheet("background-color : transparent;")
        self.reco_btn.setIcon(QIcon('./images/recommend_icon.png'))
    
    def reco_button_fn(self) :
        self.users.setStyleSheet("background-color : transparent;")
        self.users_label.setStyleSheet("background-color : transparent;")
        self.users_btn.setIcon(QIcon('./images/users_icon.png'))

        self.home.setStyleSheet("background-color : transparent;")
        self.home_label.setStyleSheet("background-color : transparent;")
        self.home_btn.setIcon(QIcon('./images/home_icon.png'))

        self.trending.setStyleSheet("background-color : transparent;")
        self.trending_label.setStyleSheet("background-color : transparent;")
        self.trending_btn.setIcon(QIcon('./images/trending_icon.png'))

        self.categories.setStyleSheet("background-color : transparent;")
        self.categories_label.setStyleSheet("background-color : transparent;")
        self.categories_btn.setIcon(QIcon('./images/categories_icon.png'))

        self.recommend.setStyleSheet("background-color : transparent;")
        self.recommend_label.setStyleSheet("background-color : transparent;")
        self.recommend_btn.setIcon(QIcon('./images/wifi_icon.png'))

        self.worldwide.setStyleSheet("background-color : transparent;")
        self.worldwide_label.setStyleSheet("background-color : transparent;")
        self.worldwide_btn.setIcon(QIcon('./images/global_icon.png'))

        self.reco.setStyleSheet("background-color : #548235;")
        self.reco_label.setStyleSheet("background-color : rgba(255, 255, 255, 50);")
        self.reco_btn.setIcon(QIcon('./images/recommend_pressed.png'))
    
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
