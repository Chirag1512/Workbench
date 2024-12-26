import sys
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QTableWidget
from PySide6.QtGui import QColor

color =[
    ("red", "FF0000"),
    ("green", "00FF00"),
    ("blue", "0000FF"),
    ("black", "000000"),
    ("white", "FFFFFF")
]

def get_rgb_from_hexa(code):
    rgb = tuple(int(code[i:i+2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])

app = QApplication()

table = QTableWidget()
table.setRowCount(len(color))
table.setColumnCount(len(color[0])+1)
table.setHorizontalHeaderLabels(["Name", "Hexa", "Color"])

for i, (name, hexa) in enumerate(color):
    iteam_name = QTableWidgetItem(name)
    iteam_hexa = QTableWidgetItem(hexa)
    iteam_color = QTableWidgetItem()
    iteam_color.setBackground(get_rgb_from_hexa(hexa))
    table.setItem(i, 0, iteam_name)
    table.setItem(i, 1, iteam_hexa)
    table.setItem(i, 2, iteam_color)    

table.show()
sys.exit(app.exec_())

