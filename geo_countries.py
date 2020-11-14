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
		
	def enabled_fn(self) :
		self.count=0
		for index in range(self.listWidget.count()) :
			self. listWidget.item(index).setIcon(QIcon('./images/enabled_icon.png'))

		self.enabled.setStyleSheet("color: green;background-color:transparent;border:0px;")
		self.disabled.setStyleSheet("color: rgb(111,131,119);background-color:transparent;border:0px;")
		self.manually.setStyleSheet("color: rgb(111,131,119);background-color:transparent;border:0px;")

	def disabled_fn(self):
		self.count=0
		for index in range(self.listWidget.count()):
			self.listWidget.item(index).setIcon(QIcon('disabled_icon'))

		
		self.disabled.setStyleSheet("color: red;background-color:transparent;border:0px;")
		self.manually.setStyleSheet("color: rgb(111,131,119);background-color:transparent;border:0px;")
		self.enabled.setStyleSheet("color: rgb(111,131,119);background-color:transparent;border:0px;")

	def manually_fn(self):
		self.count=1
		for index in range(self.listWidget.count()):
			self.listWidget.item(index).setIcon(QIcon('manually_icon'))

		self.listWidget.itemClicked.connect(self.clickevent)
		self.listWidget.itemDoubleClicked.connect(self.clickeventer)
		self.manually.setStyleSheet("color: rgb(111,131,119);background-color:transparent;border:0px;")
		self.enabled.setStyleSheet("color: rgb(111,131,119);background-color:transparent;border:0px;")
		self.disabled.setStyleSheet("color: rgb(111,131,119);background-color:transparent;border:0px;")


	def clickevent(self,item):
		item.setIcon(QIcon('enabled_icon'))

	def clickeventer(self,item):
		item.setIcon(QIcon('disabled_icon'))
		
		
	







	


		# if counter==1:
		# 	item.setIcon(QIcon('enabled_icon'))
		# elif counter==2:
		# 	item.setIcon(QIcon('disabled_icon'))
		# elif counter==3:
		# 	item.setIcon(QIcon('manually_icon'))

	
		
		


		









	    

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = EnergyWidget()
	w.show()
	sys.exit(app.exec_())