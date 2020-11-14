import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "./UI/trending.ui"))

class TrendingWidget(Base, Form) :
	def __init__(self, parent = None) :
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.home_icon.setEnabled(False)
		self.trending.setEnabled(False)
		self.glob_icon.setEnabled(False)

		self.trend_button.clicked.connect(self.trend_switcher)
		self.pop_button.clicked.connect(self.pop_switcher)
		self.home_button.clicked.connect(self.home_switcher)
		self.glob_button.clicked.connect(self.glob_switcher)

		self.trending.clicked.connect(self.trend_proc)

	def trend_switcher(self) :
		if self.trend_button.isChecked() :
			self.trend_button.setIcon(QIcon('./images/pop_active.png'))
			self.trending.setEnabled(True)
		else :
			self.trend_button.setIcon(QIcon('./images/inactiver.png'))
			self.trending.setEnabled(False)

	def glob_switcher(self) :
		if self.glob_button.isChecked() :
			self.glob_button.setIcon(QIcon('./images/active_icon.png'))
			self.glob_icon.setEnabled(True)
		else :
			self.glob_button.setIcon(QIcon('./images/inactiver.png'))
			self.glob_icon.setEnabled(False)

	def pop_switcher(self) :
		if self.pop_button.isChecked() :
			self.pop_button.setIcon(QIcon('./images/pop_active.png'))
		else :
			self.pop_button.setIcon(QIcon('./images/inactiver.png'))

	def home_switcher(self) :
		if self.home_button.isChecked() :
			self.home_button.setIcon(QIcon('./images/h_switch.png'))
			self.home_icon.setEnabled(True)
		else :
			self.home_button.setIcon(QIcon('./images/inactiver.png'))
			self.home_icon.setEnabled(False)

	def trend_proc(self) :
		print("Trend is clicked")

if __name__ == '__main__' :
	import sys
	app = QApplication(sys.argv)
	w = trendingWidget()
	w.show()
	sys.exit(app.exec())
