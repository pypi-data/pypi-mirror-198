from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 468)
        MainWindow.setMinimumSize(QtCore.QSize(473, 468))
        MainWindow.setMaximumSize(QtCore.QSize(473, 468))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setMinimumSize(QtCore.QSize(473, 447))
        self.content.setMaximumSize(QtCore.QSize(473, 447))
        self.content.setAutoFillBackground(False)
        self.content.setStyleSheet("background-color: rgb(101, 255, 111)")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMinimumSize(QtCore.QSize(450, 398))
        self.login_area.setMaximumSize(QtCore.QSize(450, 398))
        self.login_area.setStyleSheet("border-radius: 10px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.pushButton_conversor = QtWidgets.QPushButton(self.login_area)
        self.pushButton_conversor.setGeometry(QtCore.QRect(80, 320, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_conversor.setFont(font)
        self.pushButton_conversor.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(75, 255, 87);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_conversor.setObjectName("pushButton_conversor")
        self.label = QtWidgets.QLabel(self.login_area)
        self.label.setGeometry(QtCore.QRect(151, 10, 138, 63))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 15px;\n"
"    padding: 15px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_dados_met = QtWidgets.QPushButton(self.login_area)
        self.pushButton_dados_met.setGeometry(QtCore.QRect(80, 260, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_dados_met.setFont(font)
        self.pushButton_dados_met.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(75, 255, 87);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_dados_met.setObjectName("pushButton_dados_met")
        self.pushButton_calc_dist = QtWidgets.QPushButton(self.login_area)
        self.pushButton_calc_dist.setGeometry(QtCore.QRect(80, 200, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_calc_dist.setFont(font)
        self.pushButton_calc_dist.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(75, 255, 87);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_calc_dist.setObjectName("pushButton_calc_dist")
        self.pushButton_mapa = QtWidgets.QPushButton(self.login_area)
        self.pushButton_mapa.setGeometry(QtCore.QRect(80, 140, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_mapa.setFont(font)
        self.pushButton_mapa.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(75, 255, 87);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_mapa.setObjectName("pushButton_mapa")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GeoPyLib"))
        self.pushButton_conversor.setText(_translate("MainWindow", "Conversor de Coordenadas"))
        self.label.setText(_translate("MainWindow", "GeoPyLib"))
        self.pushButton_dados_met.setText(_translate("MainWindow", "Dados Meterologicos"))
        self.pushButton_calc_dist.setText(_translate("MainWindow", "Calcular Distância"))
        self.pushButton_mapa.setText(_translate("MainWindow", "Visualizar Mapa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
