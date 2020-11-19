import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "./UI/geo.ui"))

class GeoWidget(Base, Form) :
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.AfWidget.setVisible(False)
		for index in range(self.AfWidget.count()) :
			self.AfWidget.item(index).setIcon(QIcon('./images/disabled_icon.png'))
		self.AfWidget.itemClicked.connect(self.clickevent)
		self.AfWidget.itemDoubleClicked.connect(self.clickeventer)

		self.AsWidget.setVisible(False)
		for index in range(self.AsWidget.count()) :
			self.AsWidget.item(index).setIcon(QIcon('./images/disabled_icon.png'))
		self.AsWidget.itemClicked.connect(self.clickevent)
		self.AsWidget.itemDoubleClicked.connect(self.clickeventer)

		self.CaWidget.setVisible(False)
		for index in range(self.CaWidget.count()) :
			self.CaWidget.item(index).setIcon(QIcon('./images/disabled_icon.png'))
		self.CaWidget.itemClicked.connect(self.clickevent)
		self.CaWidget.itemDoubleClicked.connect(self.clickeventer)

		self.CarWidget.setVisible(False)
		for index in range(self.CarWidget.count()) :
			self.CarWidget.item(index).setIcon(QIcon('./images/disabled_icon.png'))
		self.CarWidget.itemClicked.connect(self.clickevent)
		self.CarWidget.itemDoubleClicked.connect(self.clickeventer)

		self.EuWidget.setVisible(False)
		for index in range(self.EuWidget.count()) :
			self.EuWidget.item(index).setIcon(QIcon('./images/disabled_icon.png'))
		self.EuWidget.itemClicked.connect(self.clickevent)
		self.EuWidget.itemDoubleClicked.connect(self.clickeventer)

		self.NaWidget.setVisible(False)
		for index in range(self.NaWidget.count()) :
			self.NaWidget.item(index).setIcon(QIcon('./images/disabled_icon.png'))
		self.NaWidget.itemClicked.connect(self.clickevent)
		self.NaWidget.itemDoubleClicked.connect(self.clickeventer)

		self.OcWidget.setVisible(False)
		for index in range(self.OcWidget.count()) :
			self.OcWidget.item(index).setIcon(QIcon('./images/disabled_icon.png'))
		self.OcWidget.itemClicked.connect(self.clickevent)
		self.OcWidget.itemDoubleClicked.connect(self.clickeventer)

		self.SaWidget.setVisible(False)
		for index in range(self.SaWidget.count()) :
			self.SaWidget.item(index).setIcon(QIcon('./images/disabled_icon.png'))
		self.SaWidget.itemClicked.connect(self.clickevent)
		self.SaWidget.itemDoubleClicked.connect(self.clickeventer)

		self.geo_na.clicked.connect(self.na_switcher)
		self.geo_ca.clicked.connect(self.ca_switcher)
		self.geo_sa.clicked.connect(self.sa_switcher)
		self.geo_oc.clicked.connect(self.oc_switcher)
		self.geo_euro.clicked.connect(self.euro_switcher)
		self.geo_car.clicked.connect(self.car_switcher)
		self.geo_as.clicked.connect(self.as_switcher)
		self.geo_af.clicked.connect(self.af_switcher)

		self.geo_home.clicked.connect(self.home_switcher)
		self.geo_trending.clicked.connect(self.trending_switcher)
		self.geo_cat.clicked.connect(self.categories_switcher)
		self.geo_reco.clicked.connect(self.reco_switcher)


	def clickevent(self, item) :
		item.setIcon(QIcon('./images/enabled_icon.png'))

	def clickeventer(self, item) :
		item.setIcon(QIcon('./images/disabled_icon.png'))

	def na_switcher(self) :
		if self.geo_na.isChecked() :
			self.geo_na.setIcon(QIcon('./images/geo_active.png'))
			self.NaWidget.setVisible(True)
		else :
			self.geo_na.setIcon(QIcon('./images/geo_off.png'))
			self.NaWidget.setVisible(False)

	def ca_switcher(self) :
		if self.geo_ca.isChecked() :
			self.geo_ca.setIcon(QIcon('./images/geo_active.png'))
			self.CaWidget.setVisible(True)
		else :
			self.geo_ca.setIcon(QIcon('./images/geo_off.png'))
			self.CaWidget.setVisible(False)
	
	def sa_switcher(self) :
		if self.geo_sa.isChecked() :
			self.geo_sa.setIcon(QIcon('./images/geo_active.png'))
			self.SaWidget.setVisible(True)
		else :
			self.geo_sa.setIcon(QIcon('./images/geo_off.png'))
			self.SaWidget.setVisible(False)
	
	def oc_switcher(self) :
		if self.geo_oc.isChecked() :
			self.geo_oc.setIcon(QIcon('./images/geo_active.png'))
			self.OcWidget.setVisible(True)
		else :
			self.geo_oc.setIcon(QIcon('./images/geo_off.png'))
			self.OcWidget.setVisible(False)

	def euro_switcher(self) :
		if self.geo_euro.isChecked() :
			self.geo_euro.setIcon(QIcon('./images/geo_active.png'))
			self.EuWidget.setVisible(True)
		else :
			self.geo_euro.setIcon(QIcon('./images/geo_off.png'))
			self.EuWidget.setVisible(False)

	def car_switcher(self) :
		if self.geo_car.isChecked() :
			self.geo_car.setIcon(QIcon('./images/geo_active.png'))
			self.CarWidget.setVisible(True)
		else :
			self.geo_car.setIcon(QIcon('./images/geo_off.png'))
			self.CarWidget.setVisible(False)

	def as_switcher(self) :
		if self.geo_as.isChecked() :
			self.geo_as.setIcon(QIcon('./images/geo_active.png'))
			self.AsWidget.setVisible(True)
		else :
			self.geo_as.setIcon(QIcon('./images/geo_off.png'))
			self.AsWidget.setVisible(False)

	def af_switcher(self) :
		if self.geo_af.isChecked() :
			self.geo_af.setIcon(QIcon('./images/geo_active.png'))
			self.AfWidget.setVisible(True)
		else :
			self.geo_af.setIcon(QIcon('./images/geo_off.png'))
			self.AfWidget.setVisible(False)

	def home_switcher(self) :
		if self.geo_home.isChecked() :
			self.geo_home.setIcon(QIcon('./images/geo_home.png'))
		else :
			self.geo_home.setIcon(QIcon('./images/geo_item_inactive.png'))

	def trending_switcher(self) :
		if self.geo_trending.isChecked() :
			self.geo_trending.setIcon(QIcon('./images/geo_trending.png'))
		else :
			self.geo_trending.setIcon(QIcon('./images/geo_item_inactive.png'))

	def categories_switcher(self) :
		if self.geo_cat.isChecked() :
			self.geo_cat.setIcon(QIcon('./images/geo_cat.png'))
		else :
			self.geo_cat.setIcon(QIcon('./images/geo_item_inactive.png'))

	def reco_switcher(self) :
		if self.geo_reco.isChecked() :
			self.geo_reco.setIcon(QIcon('./images/geo_trending.png'))
		else :
			self.geo_reco.setIcon(QIcon('./images/geo_item_inactive.png'))

if __name__ == '__main__' :
	import sys
	app = QApplication(sys.argv)
	w = GeoWidget()
	w.show()
	sys.exit(app.exec())
	