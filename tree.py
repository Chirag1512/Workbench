import sys
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

data = {
    "project A": ["file1.txt", "file2.mp4", "file3.jpg"],
    "project B": ["abc.py", "xyz.txt", "123.png"],
    "project C": [""]
}

app = QApplication(sys.argv)
tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Name", "Type"])

items = []

for key, values in data.items():
    item = QTreeWidgetItem([key])
    for value in values:
        ext = value.split(".")[-1].upper()
        child = QTreeWidgetItem([value, ext])
        item.addChild(child)
    items.append(item)
tree.insertTopLevelItems(0, items)

tree.show()
sys.exit(app.exec_())