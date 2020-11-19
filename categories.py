import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "./UI/category.ui"))

class CategoriesWidget(Base, Form) :
	def __init__(self, parent = None) :
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.music_button.clicked.connect(self.music_switcher)
		self.game_button.clicked.connect(self.game_switcher)
		self.news_button.clicked.connect(self.news_switcher)
		self.video_button.clicked.connect(self.video_switcher)

		self.below_button.clicked.connect(self.below_switcher)
		self.home_button.clicked.connect(self.home_switcher)
		self.saw_button.clicked.connect(self.saw_switcher)
		self.glob_button.clicked.connect(self.glob_switcher)

	def music_switcher(self) :
		if self.music_button.isChecked() :
			self.music_button.setIcon(QIcon('./images/red.png'))
			self.music_active.setEnabled(True)
		else :
			self.music_button.setIcon(QIcon('./images/inactiver.png'))
			self.music_active.setEnabled(False)

	def game_switcher(self) :
		if self.game_button.isChecked() :
			self.game_button.setIcon(QIcon('./images/red.png'))
			self.game_active.setEnabled(True)
		else :
			self.game_button.setIcon(QIcon('./images/inactiver.png'))
			self.game_active.setEnabled(False)

	def news_switcher(self) :
		if self.news_button.isChecked() :
			self.news_button.setIcon(QIcon('./images/red.png'))
			self.news_active.setEnabled(True)
		else :
			self.news_button.setIcon(QIcon('./images/inactiver.png'))
			self.news_active.setEnabled(False)
	
	def video_switcher(self) :
		if self.video_button.isChecked() :
			self.video_button.setIcon(QIcon('./images/red.png'))
			self.video_active.setEnabled(True)
		else :
			self.video_button.setIcon(QIcon('./images/inactiver.png'))
			self.video_active.setEnabled(False)



	def below_switcher(self) :
		if self.below_button.isChecked() :
			self.below_button.setIcon(QIcon('./images/yellow.png'))
			self.below_icon.setEnabled(True)
			self.middle_puzzle.setEnabled(True)
		else :
			self.below_button.setIcon(QIcon('./images/inactiver.png'))
			self.below_icon.setEnabled(False)
			self.middle_puzzle.setEnabled(False)

	def home_switcher(self) :
		if self.home_button.isChecked() :
			self.home_button.setIcon(QIcon('./images/h_switch.png'))
			self.home_icon.setEnabled(True)
		else :
			self.home_button.setIcon(QIcon('./images/inactiver.png'))
			self.home_icon.setEnabled(False)

	def saw_switcher(self) :
		if self.saw_button.isChecked() :
			self.saw_button.setIcon(QIcon('./images/red.png'))
			self.saw_icon.setEnabled(True)
		else :
			self.saw_button.setIcon(QIcon('./images/inactiver.png'))
			self.saw_icon.setEnabled(False)

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
	w = CategoriesWidget()
	w.show()
	sys.exit(app.exec())
