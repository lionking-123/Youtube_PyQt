import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "geo_two.ui"))

class GeoTwoWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		

		if self.stackedWidget.currentIndex()==0:
			current=self.stackedWidget.currentWidget()
			current.earth_on.clicked.connect(self.loadcountries)
			current.earth_button.clicked.connect(self.loadoff)

			

	def loadcountries(self):
		current=self.stackedWidget.currentWidget()
		current.earth_button.setIcon(QIcon('active_icon'))
		size = QSize(35, 35) 
		current.earth_button.setIconSize(size)
		current.backlabel.setVisible(True)
		self.stackedWidget.setCurrentIndex(1)
		current=self.stackedWidget.currentWidget()
		current.back.clicked.connect(self.backfn)

	def loadoff(self):
		current=self.stackedWidget.currentWidget()
		current.earth_button.setIcon(QIcon(''))
		size = QSize(45, 45) 
		current.earth_button.setIconSize(size)
		current.backlabel.setVisible(False)


	def backfn(self):
		self.stackedWidget.setCurrentIndex(0)


		




	    

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = EnergyWidget()
	w.show()
	sys.exit(app.exec_())