import sys
from PyQt6.QtWidgets import QApplication, QWidget
from windows.login_ui import Ui_LoginWindow


def main():
    app = QApplication(sys.argv)

    window = QWidget()
    ui = Ui_LoginWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()