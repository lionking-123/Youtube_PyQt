import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "./UI/users.ui"))

class UsersWidget(Base, Form) :
	def __init__(self, parent = None) :
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.pwdshow_btn.clicked.connect(self.pwd_sh)

	def pwd_sh(self) :
		if self.pwdshow_btn.isChecked() :
			self.pwdshow_btn.setIcon(QIcon('./images/pwdH.png'))
			self.password.setEchoMode(QLineEdit.Normal)
			self.confirm.setEchoMode(QLineEdit.Normal)
		else :
			self.pwdshow_btn.setIcon(QIcon('./images/pwdS.png'))
			self.password.setEchoMode(QLineEdit.Password)
			self.confirm.setEchoMode(QLineEdit.Password)
		
if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = UsersWidget()
	w.show()
	sys.exit(app.exec())
