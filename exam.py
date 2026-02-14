import sys
import pymysql
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(895, 845)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 600, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 710, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 70, 181, 181))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QIcon("IconHotel.jpg"))
        self.pushButton_3.setIconSize(QSize(170,170))

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(330, 350, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(330, 450, 221, 31))
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(330,550,270,40))
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(330, 390, 231, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 510, 231, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formi = Form
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Войти"))
        self.pushButton_2.setText(_translate("Form", "Войти как гость"))
        self.label.setText(_translate("Form", "Введите логин"))
        self.label_2.setText(_translate("Form", "Введите пароль"))
        self.label_3.setText(_translate("Form", ""))
        self.pushButton_2.clicked.connect(self.show_window_guest)
        self.pushButton.clicked.connect(self.check_user)
    def show_window_guest(self):
        self.okno = QtWidgets.QWidget()
        self.okoshko = Ui_Gost()
        self.okoshko.setupUi(self.okno)
        self.okno.show()
        self.formi.hide()
    def show_window_director(self):
        self.okno = QtWidgets.QWidget()
        self.okoshko = Ui_director()
        self.okoshko.setupUi(self.okno)
        self.okno.show()
        self.formi.hide()
    def show_user_okno(self):
        self.okno = QtWidgets.QWidget()
        self.okoshi = Ui_User()
        self.okoshi.setupUi(self.okno)
        self.okno.show()
        self.formi.hide()
    def show_meneger_okno(self):
        self.okno = QtWidgets.QWidget()
        self.okosho = Ui_Form_Meneger()
        self.okosho.setupUi(self.okno)
        self.formi.hide()
        self.okno.show()
    def check_user(self):
        self.login = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        if not self.login or not self.password:
            self.label_3.setText("Введите логин и пароль!")
        else:
            try:
                connection = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='Hotel'
                )
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM User WHERE name_user = %s and password_user = %s"
                    cursor.execute(sql,(self.login,self.password))
                    result = cursor.fetchall()
                    if not result:
                        self.label_3.setText("Неверные данные")
                        return
                    user = result[0]
                    if user[1]=="manager":
                        self.show_meneger_okno()
                    if user[1]=="director":
                        self.show_window_director()
                    if user[1] =='user':
                        self.show_user_okno()
            except pymysql.Error as E:
                return  0
            finally:
                cursor.close()

class Ui_Gost(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(755, 580)
        self.listView = QtWidgets.QTableWidget(parent=Form)
        self.listView.setGeometry(QtCore.QRect(0, 110, 761, 471))
        self.listView.setObjectName("listView")
        self.load_table_fre_rooom()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
    def load_table_fre_rooom(self):
        try:
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='Hotel'
            )
            with connection.cursor() as cursor:
                sql = "SELECT *FROM fre_room"
                cursor.execute(sql)
                result = cursor.fetchall()
                if result:
                    self.listView.setColumnCount(len(result[0]))
                    headers = ["id_room","name_categoria","number_floor","status_clining","name_booking"]
                    self.listView.setHorizontalHeaderLabels(headers[:len(result[0])])
                    for row_number,row_data in enumerate(result):
                        self.listView.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.listView.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
                            self.listView.resizeColumnsToContents()
        except pymysql.Error as e:
            return 0


                    

class Ui_director(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(755, 580)
        Form.setWindowTitle("Добро пожаловать в программу,директор!")
        self.listView = QtWidgets.QListView(parent=Form)
        self.listView.setGeometry(QtCore.QRect(0, 110, 761, 471))
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добро пожаловать в программу,директор!"))

    class Ui_Form_Meneger(object):
        def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.resize(537, 450)
            self.tabWidget = QtWidgets.QTabWidget(parent=Form)
            self.tabWidget.setGeometry(QtCore.QRect(0, 100, 541, 351))
            self.tabWidget.setObjectName("tabWidget")
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.tableWidget = QtWidgets.QTableWidget(parent=self.tab)
            self.tableWidget.setGeometry(QtCore.QRect(0, 0, 541, 321))
            self.tableWidget.setObjectName("tableWidget")
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)
            self.pushButton = QtWidgets.QPushButton(parent=self.tab)
            self.pushButton.setGeometry(QtCore.QRect(0, 210, 93, 28))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.pushButton.setFont(font)
            self.pushButton.setObjectName("pushButton")
            self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab)
            self.pushButton_2.setGeometry(QtCore.QRect(140, 210, 93, 28))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.pushButton_2.setFont(font)
            self.pushButton_2.setObjectName("pushButton_2")
            self.tabWidget.addTab(self.tab, "")
            self.tab_2 = QtWidgets.QWidget()
            self.tab_2.setObjectName("tab_2")
            self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.tab_2)
            self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 541, 321))
            self.tableWidget_2.setObjectName("tableWidget_2")
            self.tableWidget_2.setColumnCount(0)
            self.tableWidget_2.setRowCount(0)
            self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab_2)
            self.pushButton_3.setGeometry(QtCore.QRect(0, 220, 93, 28))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.pushButton_3.setFont(font)
            self.pushButton_3.setObjectName("pushButton_3")
            self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab_2)
            self.pushButton_4.setGeometry(QtCore.QRect(150, 220, 93, 28))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.pushButton_4.setFont(font)
            self.pushButton_4.setObjectName("pushButton_4")
            self.tabWidget.addTab(self.tab_2, "")
            self.tab_3 = QtWidgets.QWidget()
            self.tab_3.setObjectName("tab_3")
            self.tableWidget_3 = QtWidgets.QTableWidget(parent=self.tab_3)
            self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 541, 321))
            self.tableWidget_3.setObjectName("tableWidget_3")
            self.tableWidget_3.setColumnCount(0)
            self.tableWidget_3.setRowCount(0)
            self.pushButton_5 = QtWidgets.QPushButton(parent=self.tab_3)
            self.pushButton_5.setGeometry(QtCore.QRect(170, 250, 93, 28))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.pushButton_5.setFont(font)
            self.pushButton_5.setObjectName("pushButton_5")
            self.pushButton_6 = QtWidgets.QPushButton(parent=self.tab_3)
            self.pushButton_6.setGeometry(QtCore.QRect(0, 250, 93, 28))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.pushButton_6.setFont(font)
            self.pushButton_6.setObjectName("pushButton_6")
            self.tabWidget.addTab(self.tab_3, "")

            self.retranslateUi(Form)
            self.tabWidget.setCurrentIndex(2)
            QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.pushButton.setText(_translate("Form", "Добавить"))
            self.pushButton_2.setText(_translate("Form", "Изменить"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
            self.pushButton_3.setText(_translate("Form", "Добавить"))
            self.pushButton_4.setText(_translate("Form", "Изменить"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
            self.pushButton_5.setText(_translate("Form", "Изменить"))
            self.pushButton_6.setText(_translate("Form", "Добавить"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Page"))

class Ui_Form_Meneger(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(537, 450)
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 100, 541, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 541, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton.setGeometry(QtCore.QRect(0, 210, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 210, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 541, 321))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 220, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 220, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(parent=self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 541, 321))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 250, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 250, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.show_table_room_vce()
        self.show_clients()
        self.show_table_broni()
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.pushButton_2.setText(_translate("Form", "Изменить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.pushButton_3.setText(_translate("Form", "Добавить"))
        self.pushButton_4.setText(_translate("Form", "Изменить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.pushButton_5.setText(_translate("Form", "Изменить"))
        self.pushButton_6.setText(_translate("Form", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Page"))
        self.pushButton.clicked.connect(self.show_dobavlenie)
        self.pushButton_6.clicked.connect(self.show_dovalnenie_nomera)

    def show_dobavlenie(self):
        self.okno = QtWidgets.QWidget()
        self.okoshko = Ui_dobavlenie()
        self.okoshko.setupUi(self.okno)
        self.okoshko.parent_window = self
        self.okno.show()
    def show_dovalnenie_nomera(self):
        self.okno = QtWidgets.QWidget()
        self.okosho = Ui_dobavlenie_nomere()
        self.okosho.setupUi(self.okno)
        self.okosho.parent_window = self
        self.okno.show()

    def show_table_broni(self):
        try:
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='Hotel'
            )
            with connection.cursor() as cursor:
                sql = "SELECT *FROM broni"
                cursor.execute(sql)
                result = cursor.fetchall()
                if result:
                    self.tableWidget_2.setColumnCount(len(result[0]))
                    headers =["id_broni","name_categoria","number_floor","data_start","data_end"]
                    self.tableWidget_2.setHorizontalHeaderLabels(headers[:len(result[0])])
                    for row_count,row_data in enumerate(result):
                        self.tableWidget_2.insertRow(row_count)
                        for row_number,data in enumerate(row_data):
                            self.tableWidget_2.setItem(row_count,row_number,QtWidgets.QTableWidgetItem(str(data)))
                            self.tableWidget_2.resizeColumnsToContents()
        except pymysql.Error as e:
            return 0
    def show_table_room_vce(self):
        try:
            self.tableWidget_3.clear()
            self.tableWidget_3.setColumnCount(0)
            self.tableWidget_3.setRowCount(0)
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='Hotel'
            )
            with connection.cursor() as cusor:
                sql = "SELECT * FROM vce_rooom"
                cusor.execute(sql)
                result = cusor.fetchall()
                if result:
                    self.tableWidget_3.setColumnCount(len(result[0]))
                    headers = ["id_room","name_categoria","number_floor","status_clining","name_booking"]
                    self.tableWidget_3.setHorizontalHeaderLabels(headers[:len(result[0])])
                    for row_number, row_data in enumerate(result):
                        self.tableWidget_3.insertRow(row_number)
                        for colum_count, row in enumerate(row_data):
                            self.tableWidget_3.setItem(row_number,colum_count,QtWidgets.QTableWidgetItem(str(row)))
                            self.tableWidget_3.resizeColumnsToContents()
        except pymysql.Error as e:
            return e
    def show_clients(self):

        try:
            self.tableWidget.clear()
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='Hotel'
            )
            with connection.cursor() as cursor:
                sql = "SELECT * FROM user WHERE id_user != 1 and id_user != 2"
                cursor.execute(sql)
                result = cursor.fetchall()
                if result:
                    self.tableWidget.setColumnCount(len(result[0]))
                    headers = ["id","name"]
                    self.tableWidget.setHorizontalHeaderLabels(headers[:len(result[0])])
                    for row_number,row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_count,data in enumerate(row_data):
                            self.tableWidget.setItem(row_number,column_count,QtWidgets.QTableWidgetItem(str(data)))
                            self.tableWidget.resizeColumnsToContents()
        except pymysql.Error as e:
            return  0

class Ui_dobavlenie(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle("Добавление клиента")
        Form.resize(408, 431)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 340, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:red;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 181, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label2 = QtWidgets.QLabel(parent=Form)
        self.label2.setGeometry(QtCore.QRect(10,140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label")
        self.lineEdit2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit2.setGeometry(QtCore.QRect(140, 140, 181, 31))
        self.lineEdit2.setObjectName("lineEdit")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление клиента"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.label.setText(_translate("Form", "Имя"))
        self.label2.setText(_translate("Form", "ID"))
        self.pushButton.clicked.connect(self.function_dobavlenie)

    def function_dobavlenie(self):
        try:
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='Hotel'
            )
            with connection.cursor() as cursor:
                name = self.lineEdit.text()
                id = self.lineEdit2.text()
                sql = "INSERT INTO client (id_client,name_client) VALUES (%s,%s)"
                cursor.execute(sql,(id,name))
                QtWidgets.QMessageBox.information(self.pushButton,"УСПЕХ", "Добавили")
                connection.commit()
                connection.close()
                if hasattr(self, "parent_window"):
                    self.parent_window.show_clients()

                self.pushButton.window().close()
        except pymysql.Error as e:
            return 0

class Ui_dobavlenie_nomere(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle("Добавление номера")
        Form.setFixedSize(400,400)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 80, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 311, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 70, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 110, 141, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 150, 141, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 220, 141, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 280, 141, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 340, 161, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление номера"))
        self.label.setText(_translate("Form", "ID"))
        self.label_2.setText(_translate("Form", "Категория"))
        self.label_3.setText(_translate("Form", "Этаж"))
        self.label_4.setText(_translate("Form", "Статус(1-занят, 2-свободен)"))
        self.label_5.setText(_translate("Form", "Уборка(1-чистый,2-гразный)"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.pushButton.clicked.connect(self.dobavlenie)
    def dobavlenie(self):
        try:
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='Hotel'
            )
            with connection.cursor() as cursor:
                id = self.lineEdit.text()
                cat = self.lineEdit_2.text()
                flo = self.lineEdit_3.text()
                st_b = self.lineEdit_4.text()
                st_cl = self.lineEdit_5.text()
                sql = "INSERT INTO room (id_room,id_cat,id_fl,id_cl,id_b) VALUES (%s,%s,%s,%s,%s)"
                cursor.execute(sql,(id,cat,flo,st_b,st_cl))
                QtWidgets.QMessageBox.information(self.pushButton, "Добавление номера", "Успешное добавление")
                connection.commit()
                connection.close()
                if hasattr(self,'parent_window'):
                    self.parent_window.show_table_room_vce()
                self.pushButton.window().close()

        except pymysql.Error as e:
            return  0
class Ui_User(object):


    def show_vce(self):
        try:
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='Hotel'
            )
            with connection.cursor() as cursor:
                sql = "SELECT *FROM fre_room"
                cursor.execute(sql)
                result = cursor.fetchall()
                if result:
                    self.tableView.setColumnCount(len(result[0]))
                    headers = ["id_broni","name_categoria","number_floor","data_start","data_end"]
                    self.tableView.setHorizontalHeaderLabels(headers[:len(result[0])])
                    for row_count,row_data in enumerate(result):
                        self.tableView.insertRow(row_count)
                        for column_count,data in enumerate(row_data):
                            self.tableView.setItem(row_count,column_count,QtWidgets.QTableWidgetItem(str(data)))
                            self.tableView.resizeColumnsToContents()
        except pymysql.Error as e:
            return 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
