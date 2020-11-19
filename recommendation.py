import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "./UI/recommendation.ui"))


class RecommendationWidget(Base, Form) :
	def __init__(self, parent = None) :
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.crown1_button.clicked.connect(self.crown1_switcher)
		self.crown2_button.clicked.connect(self.crown2_switcher)
		self.crown3_button.clicked.connect(self.crown3_switcher)

		self.time_button.clicked.connect(self.time_switcher)

		self.home_button.clicked.connect(self.home_switcher)
		self.sat_button.clicked.connect(self.sat_switcher)
		self.radio_button.clicked.connect(self.radio_switcher)
		self.glob_button.clicked.connect(self.glob_switcher)
		self.updown_button.clicked.connect(self.updown_switcher)

	def crown1_switcher(self) :
		if self.crown1_button.isChecked() :
			self.crown1_button.setIcon(QIcon('./images/yellow.png'))
			self.crown1_icon.setEnabled(True)
		else :
			self.crown1_button.setIcon(QIcon('./images/inactiver.png'))
			self.crown1_icon.setEnabled(False)

	def crown2_switcher(self) :
		if self.crown2_button.isChecked() :
			self.crown2_button.setIcon(QIcon('./images/yellow.png'))
			self.crown2_icon.setEnabled(True)
		else :
			self.crown2_button.setIcon(QIcon('./images/inactiver.png'))
			self.crown2_icon.setEnabled(False)

	def crown3_switcher(self) :
		if self.crown3_button.isChecked() :
			self.crown3_button.setIcon(QIcon('./images/reco_crown3.png'))
			self.crown3_icon.setEnabled(True)
		else :
			self.crown3_button.setIcon(QIcon('./images/inactiver.png'))
			self.crown3_icon.setEnabled(False)
	
	def time_switcher(self) :
		if self.time_button.isChecked() :
			self.time_button.setIcon(QIcon('./images/red.png'))
			self.hr_enter.setEnabled(True)
			self.min_enter.setEnabled(True)
			self.sec_enter.setEnabled(True)
		else :
			self.time_button.setIcon(QIcon('./images/inactiver.png'))
			self.hr_enter.setEnabled(False)
			self.min_enter.setEnabled(False)
			self.sec_enter.setEnabled(False)

	def updown_switcher(self) :
		if self.updown_button.isChecked() :
			self.updown_button.setIcon(QIcon('./images/red.png'))
			self.updown_icon.setEnabled(True)
		else :
			self.updown_button.setIcon(QIcon('./images/inactiver.png'))
			self.updown_icon.setEnabled(False)

	def home_switcher(self) :
		if self.home_button.isChecked() :
			self.home_button.setIcon(QIcon('./images/h_switch.png'))
			self.home_icon.setEnabled(True)
		else :
			self.home_button.setIcon(QIcon('./images/inactiver.png'))
			self.home_icon.setEnabled(False)

	def sat_switcher(self) :
		if self.sat_button.isChecked() :
			self.sat_button.setIcon(QIcon('./images/red.png'))
			self.sat_icon.setEnabled(True)
		else :
			self.sat_button.setIcon(QIcon('./images/inactiver.png'))
			self.sat_icon.setEnabled(False)

	def radio_switcher(self) :
		if self.radio_button.isChecked() :
			self.radio_button.setIcon(QIcon('./images/reco_crown3.png'))
			self.radio_icon.setEnabled(True)
			self.main_button.setEnabled(True)
		else :
			self.radio_button.setIcon(QIcon('./images/inactiver.png'))
			self.radio_icon.setEnabled(False)
			self.main_button.setEnabled(False)

	def glob_switcher(self) :
		if self.glob_button.isChecked() :
			self.glob_button.setIcon(QIcon('./images/active_icon.png'))
			self.glob_icon.setEnabled(True)
		else :
			self.glob_button.setIcon(QIcon('./images/inactiver.png'))
			self.glob_icon.setEnabled(False)



if __name__ == '__main__' :
	import sys
	app = QApplication(sys.argv)
	w = RecommendationWidget()
	w.show()
	sys.exit(app.exec())
