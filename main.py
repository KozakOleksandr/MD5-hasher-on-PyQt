import sys 
from PyQt5.QtWidgets import QApplication
from qt_app import MD5HasherApp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MD5HasherApp()
    window.show()
    sys.exit(app.exec_())
    