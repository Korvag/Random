import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
okButton = QPushButton('Ok')
cancelButton = QPushButton('Cancel')
test = QLineEdit()
test.setEchoMode(QLineEdit.Password)
word = test
print (str(test))
label = QLabel('Subscribe')
label.setFont(QFont('Arial',20))

hbox = QHBoxLayout()
hbox.addStretch(1)
hbox.addWidget(okButton)
hbox.addWidget(cancelButton)
hbox.addWidget(test)
vbox = QVBoxLayout()
vbox.addStretch(1)
vbox.addWidget(label)
vbox.addLayout(hbox)

win = QWidget()
win.setLayout(vbox)
win.setWindowTitle('TESTTEST')
win.show()
sys.exit(app.exec_())


