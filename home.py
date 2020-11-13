import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import urllib
import os
import time
import requests
import json
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "./UI/home.ui"))

# ========= Thread Progress Part ==========

class ThreadProgress(QThread) :
    mysignal = pyqtSignal(int)
    def __init__(self, parent = None) :
        QThread.__init__(self, parent)

    def run(self):
        i = 0
        while i < 101 :
            time.sleep(0.1)
            self.mysignal.emit(i)
            i += 25

# ========== Home Widget part =========

class HomeWidget(Base, Form) :
	def __init__(self, parent = None) :
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.video_num = 0
		self.hasFile = ""
		self.timer = QTimer()

		self.nitro.setEnabled(False)
		self.smallstart.setEnabled(False)
		self.smallstop.setEnabled(False)
		self.glob_icon.setEnabled(False)
		self.hr_enter.setValidator(QIntValidator(0, 100))
		self.min_enter.setValidator(QIntValidator(0, 60))
		self.sec_enter.setValidator(QIntValidator(0, 60))

		self.progresser = ThreadProgress(self)
		self.progresser.mysignal.connect(self.progress)

		self.youtube_enter.textChanged.connect(self.getvideo)
		self.time_button.clicked.connect(self.time_switcher)
		self.nitro_btn.clicked.connect(self.nitro_switcher)
		self.glob_button.clicked.connect(self.glob_switcher)
		self.fileload_btn.clicked.connect(self.openFileNameDialog)
		self.start.clicked.connect(self.runner_with_url)
		self.nitro.clicked.connect(self.runner_with_file)
		self.smallstop.clicked.connect(self.time_stopper)
		self.smallstart.clicked.connect(self.time_runner)
	
	def time_switcher(self) :
		if self.nitro_btn.isChecked() is False :
			self.time_button.setChecked(False)
			return
		
		if self.time_button.isChecked() :
			self.smallstart.setEnabled(True)
			self.smallstop.setEnabled(True)
			self.hr_enter.setEnabled(True)
			self.min_enter.setEnabled(True)
			self.sec_enter.setEnabled(True)
			self.time_button.setIcon(QIcon('./images/home_switch.png'))
		else :
			self.smallstart.setEnabled(False)
			self.smallstop.setEnabled(False)
			self.hr_enter.setEnabled(False)
			self.min_enter.setEnabled(False)
			self.sec_enter.setEnabled(False)
			self.time_button.setIcon(QIcon('./images/inactiver.png'))
	
	def nitro_switcher(self) :
		if self.nitro_btn.isChecked() :
			self.start.setEnabled(False)
			self.nitro.setEnabled(True)
			self.nitro_btn.setIcon(QIcon('./images/home_switch.png'))
		else :
			self.start.setEnabled(True)
			self.nitro.setEnabled(False)
			self.nitro_btn.setIcon(QIcon('./images/inactiver.png'))
			if self.time_button.isChecked() :
				self.time_button.click()
				self.smallstart.setEnabled(False)
				self.smallstop.setEnabled(False)
				self.hr_enter.setEnabled(False)
				self.min_enter.setEnabled(False)
				self.sec_enter.setEnabled(False)
				self.time_button.setIcon(QIcon('./images/inactiver.png'))

	def glob_switcher(self) :
		if self.glob_button.isChecked() :
			self.glob_button.setIcon(QIcon('./images/home_switch.png'))
			self.glob_icon.setEnabled(True)
		else :
			self.glob_button.setIcon(QIcon('./images/inactiver.png'))
			self.glob_icon.setEnabled(False)

	def runner_with_url(self) :
		url = self.youtube_enter.toPlainText()
		if self.capture(url) :
			self.start.setIcon(QIcon('./images/bigstopactive.png'))
			self.progresser.start()
		else :
			QMessageBox.about(self, "Information", "On Youtube, there is no this link!")

	def runner_with_file(self) :
		if self.hasFile == "" :
			QMessageBox.about(self, "Information", "Nothing file is selected. Please select file.")
		else :
			cnt = 0
			f = open(self.hasFile, "r")
			for x in f :
				url = x.replace('\n', '')
				if self.capture(url) :
					self.youtube_enter.setPlainText(url)
					cnt += 1
					
					for i in range(5) :
						self.progressBarMassive.setValue(i * 25)
						self.progressBarMassive.setFormat("Massive Recommendation")
						self.capture(url)
					
					self.progressBarMassive.setValue(0)
					self.progressBarMassive.setFormat("0%")

				else :
					QMessageBox.about(self, "Information", "On Youtube, there is no link as '" + x + "'.")
			
			f.close()
			QMessageBox.about(self, "Video Recommends", str(cnt) + " video(es) is recommended 100 times per one video to the territory Dominica")

	def time_stopper(self) :
		print("stoped")
	
	def time_runner(self) :
		print("started")
	
	def getvideo(self) :
		url = self.youtube_enter.toPlainText()
		if self.capture(url) is False :
			QMessageBox.about(self, "Information", "On Youtube, there is no this link.")

	def capture(self, urltext) :
		try :
			idtext = urltext.split('v=')
			idvalue = idtext[1]
			payload = {'id' : idvalue, 'part' : 'snippet', 'maxResults' : 25, 'key' : 'AIzaSyCDEiEIr3Gmbc7MWg6ozynviiAlpyOBH9A'}
			l = requests.Session().get('https://www.googleapis.com/youtube/v3/videos?', params = payload)    
			resp_dict = json.loads(l.content)
			for i in resp_dict['items'] :
				trending = i['snippet']['thumbnails']['default']['url']
			
			pixmap = QPixmap()
			data = urllib.request.urlopen(trending).read()
			pixmap.loadFromData(data)
			videoBox = pixmap.scaled(QSize(246, 136))
			self.videoBox.setPixmap(videoBox)
			return True
			
		except :
			return False

	def openFileNameDialog(self) :
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options = options)
		
		if fileName :
			count = 0
			f = open(fileName, "r")
			for x in f :
				count += 1
			
			if count > 0 :
				self.fileload_btn.setIcon(QIcon('./images/down_icon.png'))
				self.hasFile = fileName
			else :
				self.fileload_btn.setIcon(QIcon('./images/down_pressed.png'))
				self.hasFile = ""

			f.close()
		else :
			self.fileload_btn.setIcon(QIcon('./images/down_pressed.png'))
			self.hasFile = ""
		
	@pyqtSlot(int)
	def progress(self, i):
		self.progressBar.setValue(i)
		self.progressBar.setFormat("Recommending Video")
		
		url = self.youtube_enter.toPlainText()
		self.capture(url)

		if self.progressBar.value() == self.progressBar.maximum() :
			QMessageBox.about(self, "Video Recommends","1 video is recommended 100 times to the territory Dominica")
				
			self.progressBar.setValue(0)
			self.progressBar.setFormat("0%")
			self.start.setIcon(QIcon('./images/bigrunactive.png'))

if __name__ == '__main__' :
	import sys
	app = QApplication(sys.argv)
	w = HomeWidget()
	w.show()
	sys.exit(app.exec())
