from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.uic import loadUi
from db.database import get_connection


class LoginWindow(QWidget):
    """
    Окно авторизации
    """

    def __init__(self):
        super().__init__()
        loadUi("ui/login.ui", self)

        self.btn_login.clicked.connect(self.login)
        self.btn_guest.clicked.connect(self.login_as_guest)

    def login(self):
        """
        Авторизация по логину и паролю
        """
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()

        if not username or not password:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Введите логин и пароль"
            )
            return

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                SELECT u.user_id, r.role_name
                FROM Users u
                JOIN Roles r ON u.role_id = r.role_id
                WHERE u.username = %s
                  AND u.password_hash = %s
            """

            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            connection.close()

        except Exception as error:
            QMessageBox.critical(
                self,
                "Ошибка базы данных",
                str(error)
            )
            return

        if user is None:
            QMessageBox.critical(
                self,
                "Ошибка авторизации",
                "Неверный логин или пароль"
            )
            return

        QMessageBox.information(
            self,
            "Успешный вход",
            f"Вы вошли как: {user['role_name']}"
        )

    def login_as_guest(self):
        """
        Вход как гость
        """
        QMessageBox.information(
            self,
            "Гостевой вход",
            "Вы вошли как гость"
        )