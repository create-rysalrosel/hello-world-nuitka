from PySide6.QtWidgets import QApplication, QMessageBox
import sys

app = QApplication(sys.argv)
msg = QMessageBox()
msg.setText("Hello World!")
msg.exec()
