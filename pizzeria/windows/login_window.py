from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.uic import loadUi
from pizzeria.db.database import get_connection


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("ui/login.ui", self)

        self.btn_login.clicked.connect(self.login)
        self.btn_guest.clicked.connect(self.login_as_guest)

    def login(self):
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()

        if not username or not password:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Введите логин и пароль"
            )
            return

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT r.role_name
            FROM Users u
            JOIN Roles r ON u.role_id = r.role_id
            WHERE u.username = %s AND u.password_hash = %s
            """,
            (username, password)
        )

        user = cursor.fetchone()
        connection.close()

        if user:
            QMessageBox.information(
                self,
                "Успешная авторизация",
                f"Роль: {user['role_name']}"
            )
        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Неверный логин или пароль"
            )

    def login_as_guest(self):
        QMessageBox.information(
            self,
            "Гость",
            "Вы вошли как гость"
        )