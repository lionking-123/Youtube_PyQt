import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "./UI/geo_countries.ui"))

class GeoCountriesWidget(Base, Form) :
	def __init__(self, parent = None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.count = 0

		for index in range(self.listWidget.count()) :
			self.listWidget.item(index).setIcon(QIcon('./images/manually_icon.png'))

		self.enabled.clicked.connect(self.enabled_fn)
		self.disabled.clicked.connect(self.disabled_fn)
		self.manually.clicked.connect(self.manually_fn)
		self.listWidget.itemClicked.connect(self.clickevent)
		self.listWidget.itemDoubleClicked.connect(self.clickeventer)
		
	def enabled_fn(self) :
		self.count=0
		for index in range(self.listWidget.count()) :
			self. listWidget.item(index).setIcon(QIcon('./images/enabled_icon.png'))

	def disabled_fn(self) :
		self.count=0
		for index in range(self.listWidget.count()) :
			self.listWidget.item(index).setIcon(QIcon('./images/disabled_icon.png'))

	def manually_fn(self) :
		self.count=1
		for index in range(self.listWidget.count()) :
			self.listWidget.item(index).setIcon(QIcon('./images/manually_icon.png'))

	def clickevent(self,item) :
		item.setIcon(QIcon('./images/enabled_icon.png'))

	def clickeventer(self,item) :
		item.setIcon(QIcon('./images/disabled_icon.png'))

if __name__ == '__main__' :
	import sys
	app = QApplication(sys.argv)
	w = GeoCountriesWidget()
	w.show()
	sys.exit(app.exec())
