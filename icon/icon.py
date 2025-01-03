#write a small explain of icone button used in the code
#write a code
#write a code to show the icon on the button

import sys
from PySide6.QtWidgets import QApplication, QWidget,  QHBoxLayout, QPushButton,QLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

app = QApplication(sys.argv)

window = QWidget()
layout = QHBoxLayout()

text = QLabel('This is button 1')
button = QPushButton("click me")
icon = QIcon("icon.png")
button.setIcon(icon)
button.setIconSize(QSize(64,64))  

layout.addWidget(button)


text2 = QLabel('This is button 2')
button2 = QPushButton("click me")
icon2 = QIcon("icon2.png")
button.setIcon(icon2)
button.setIconSize(QSize(64,64))
layout.addWidget(button2)


layout = QHBoxLayout()
text3 = QLabel('This is button 3')
button3 = QPushButton("click me")
icon3 = QIcon("icon3.png")
button.setIcon(icon3)
button.setIconSize(QSize(64,64))
layout.addWidget(button3)

'''layout.addWidget(text)
layout.addWidget(text2)
layout.addWidget(text3)'''
window.setLayout(layout)
window.setLayout(layout)
window.setLayout(layout)
window.setWindowTitle("Main Window")
window.show()

sys.exit(app.exec())

