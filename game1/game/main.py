from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from game import process_game



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 988)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(image/112.jpeg);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hero1 = QtWidgets.QPushButton(self.centralwidget)
        self.hero1.setGeometry(QtCore.QRect(20, -20, 201, 201))
        self.hero1.setAutoFillBackground(False)
        self.hero1.setStyleSheet("image: url(image/1.jpg);")
        self.hero1.setText("")
        self.hero1.setObjectName("hero1")
        self.hero2 = QtWidgets.QPushButton(self.centralwidget)
        self.hero2.setGeometry(QtCore.QRect(20, 190, 201, 171))
        self.hero2.setStyleSheet("image: url(image/2.jpg);")
        self.hero2.setText("")
        self.hero2.setObjectName("hero2")
        self.hero3 = QtWidgets.QPushButton(self.centralwidget)
        self.hero3.setGeometry(QtCore.QRect(20, 370, 201, 191))
        self.hero3.setStyleSheet("image: url(image/3.jpg);")
        self.hero3.setText("")
        self.hero3.setObjectName("hero3")
        self.hero4 = QtWidgets.QPushButton(self.centralwidget)
        self.hero4.setGeometry(QtCore.QRect(20, 570, 201, 171))
        self.hero4.setStyleSheet("image: url(image/4.jpg);")
        self.hero4.setText("")
        self.hero4.setObjectName("hero4")
        self.hero5 = QtWidgets.QPushButton(self.centralwidget)
        self.hero5.setGeometry(QtCore.QRect(20, 750, 201, 181))
        self.hero5.setStyleSheet("image: url(image/5.jpg);")
        self.hero5.setText("")
        self.hero5.setObjectName("hero5")
        self.hero10 = QtWidgets.QPushButton(self.centralwidget)
        self.hero10.setGeometry(QtCore.QRect(900, 770, 211, 171))
        self.hero10.setStyleSheet("image: url(image/11.jpg);")
        self.hero10.setText("")
        self.hero10.setObjectName("hero10")
        self.hero8 = QtWidgets.QPushButton(self.centralwidget)
        self.hero8.setGeometry(QtCore.QRect(900, 390, 211, 191))
        self.hero8.setStyleSheet("image: url(image/8.jpg);")
        self.hero8.setText("")
        self.hero8.setObjectName("hero8")
        self.hero9 = QtWidgets.QPushButton(self.centralwidget)
        self.hero9.setGeometry(QtCore.QRect(900, 590, 211, 171))
        self.hero9.setStyleSheet("image: url(image/9.jpg);")
        self.hero9.setText("")
        self.hero9.setObjectName("hero9")
        self.hero6 = QtWidgets.QPushButton(self.centralwidget)
        self.hero6.setGeometry(QtCore.QRect(900, 20, 211, 181))
        self.hero6.setStyleSheet("image: url(image/6.jpg);")
        self.hero6.setText("")
        self.hero6.setObjectName("hero6")
        self.hero7 = QtWidgets.QPushButton(self.centralwidget)
        self.hero7.setGeometry(QtCore.QRect(900, 210, 211, 181))
        self.hero7.setStyleSheet("image: url(image/7.jpg);")
        self.hero7.setText("")
        self.hero7.setObjectName("hero7")
        self.blood1 = QtWidgets.QProgressBar(self.centralwidget)
        self.blood1.setGeometry(QtCore.QRect(20, 160, 191, 23))
        self.blood1.setProperty("value", 24)
        self.blood1.setObjectName("blood1")
        self.blood2 = QtWidgets.QProgressBar(self.centralwidget)
        self.blood2.setGeometry(QtCore.QRect(20, 330, 191, 23))
        self.blood2.setProperty("value", 24)
        self.blood2.setObjectName("blood2")
        self.blood3 = QtWidgets.QProgressBar(self.centralwidget)
        self.blood3.setGeometry(QtCore.QRect(20, 530, 191, 23))
        self.blood3.setProperty("value", 24)
        self.blood3.setObjectName("blood3")
        self.blood4 = QtWidgets.QProgressBar(self.centralwidget)
        self.blood4.setGeometry(QtCore.QRect(20, 710, 191, 23))
        self.blood4.setProperty("value", 24)
        self.blood4.setObjectName("blood4")
        self.blood5 = QtWidgets.QProgressBar(self.centralwidget)
        self.blood5.setGeometry(QtCore.QRect(20, 900, 191, 23))
        self.blood5.setProperty("value", 24)
        self.blood5.setObjectName("blood5")
        self.blood6 = QtWidgets.QProgressBar(self.centralwidget)
        self.blood6.setGeometry(QtCore.QRect(900, 180, 191, 23))
        self.blood6.setProperty("value", 24)
        self.blood6.setObjectName("blood6")
        self.blood7 = QtWidgets.QProgressBar(self.centralwidget)
        self.blood7.setGeometry(QtCore.QRect(900, 360, 191, 23))
        self.blood7.setProperty("value", 24)
        self.blood7.setObjectName("blood7")
        self.blood8 = QtWidgets.QProgressBar(self.centralwidget)
        self.blood8.setGeometry(QtCore.QRect(900, 560, 191, 23))
        self.blood8.setProperty("value", 24)
        self.blood8.setObjectName("blood8")
        self.blood9 = QtWidgets.QProgressBar(self.centralwidget)
        self.blood9.setGeometry(QtCore.QRect(900, 740, 191, 23))
        self.blood9.setProperty("value", 24)
        self.blood9.setObjectName("blood9")
        self.blood10 = QtWidgets.QProgressBar(self.centralwidget)
        self.blood10.setGeometry(QtCore.QRect(910, 910, 191, 23))
        self.blood10.setProperty("value", 24)
        self.blood10.setObjectName("blood10")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setAutoFillBackground(True)
        self.frame.setGeometry(QtCore.QRect(260, 0, 591, 781))

        self.txtOut = QtWidgets.QTextEdit(self.centralwidget)
        self.txtOut.setEnabled(True)
        self.txtOut.setGeometry(QtCore.QRect(260, 130, 591, 671))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtOut.setFont(font)
        self.txtOut.setAutoFillBackground(False)
        self.txtOut.setStyleSheet("border-image: url(image/聊天1.png);")
        self.txtOut.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.txtOut.setUndoRedoEnabled(True)
        self.txtOut.setAcceptRichText(True)
        self.txtOut.setObjectName("txtOut")

        self.txtOut1 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtOut1.setEnabled(True)
        self.txtOut1.setGeometry(QtCore.QRect(260, 0, 591, 122))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(33)
        self.txtOut1.setFont(font)
        self.txtOut1.setAutoFillBackground(False)
        self.txtOut1.setStyleSheet("border-image: url(image/111.pneg);")
        self.txtOut1.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.txtOut1.setUndoRedoEnabled(True)
        self.txtOut1.setAcceptRichText(True)
        self.txtOut1.setObjectName("txtOut1")
        self.txtOut1.setReadOnly(True)
        self.txtOut.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.hero1.clicked.connect(self.hero1_clicked)
        self.hero2.clicked.connect(self.hero2_clicked)
        self.hero3.clicked.connect(self.hero3_clicked)
        self.hero4.clicked.connect(self.hero4_clicked)
        self.hero5.clicked.connect(self.hero5_clicked)
        self.hero6.clicked.connect(self.hero6_clicked)
        self.hero7.clicked.connect(self.hero7_clicked)
        self.hero8.clicked.connect(self.hero8_clicked)
        self.hero9.clicked.connect(self.hero9_clicked)
        self.hero10.clicked.connect(self.hero10_clicked)

       # self.txtOut.setWindowOpacity(0.9)
        #self.txtOut.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.txtOut.setStyleSheet("color:black")
        self.txtOut1.setStyleSheet("color:blue")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_form()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def load_form(self):
        self.txtOut.append("Game Start")
        x = process_game.team1_role()
        y = process_game.team2_role()
        self.blood1.setValue(55)
        self.txtOut.append(str(x)+str(y))
        self.txtOut1.setText('Instruction to the game:'+'\n'+ 'Once the game starts, the system will form two teams automatically (Team one on the left and Team two on the right) and assign the roles to each team members with different amount of attributes. By clicking the hero profile, you could see the change of attributes of the hero after each attack. If a hero is dead, his profile will change and he can not attact others anymore. Once all 5 members from a team were killed, game will be over.')
        self.update_blood()

    def hero1_clicked(self):
        a=process_game.hero1click()
        self.txtOut.append(str(a))
        self.update_blood()

        self.change_profile()

    def hero2_clicked(self):
        a = process_game.hero2click()
        self.update_blood()
        self.txtOut.append(str(a))
        self.change_profile()

    def hero3_clicked(self):
        a = process_game.hero3click()
        self.update_blood()
        self.txtOut.append(str(a))
        self.change_profile()


    def hero4_clicked(self):
        a = process_game.hero4click()
        self.update_blood()
        self.txtOut.append(str(a))
        self.change_profile()

    def hero5_clicked(self):
        a = process_game.hero5click()
        self.update_blood()
        self.txtOut.append(str(a))
        self.change_profile()


    def hero6_clicked(self):
        a = process_game.hero6click()
        self.update_blood()
        self.txtOut.append(str(a))
        self.change_profile()

    def hero7_clicked(self):
        a = process_game.hero7click()
        self.update_blood()
        self.txtOut.append(str(a))
        self.change_profile()


    def hero8_clicked(self):
        a = process_game.hero8click()
        self.update_blood()
        self.txtOut.append(str(a))
        self.change_profile()


    def hero9_clicked(self):
        a = process_game.hero9click()
        self.update_blood()
        self.txtOut.append(str(a))
        self.change_profile()


    def hero10_clicked(self):
        a = process_game.hero10click()
        self.update_blood()
        self.txtOut.append(str(a))
        self.change_profile()
        
    # Change the profile of the hero if he dies
    def change_profile(self):
        a=process_game.hero_one.status
        if a=='dead':
            self.hero1.setStyleSheet("image: url(image/dead.jpeg);")
        b = process_game.hero_two.status
        if b == 'dead':
            self.hero2.setStyleSheet("image: url(image/dead.jpeg);")
        c = process_game.hero_three.status
        if c == 'dead':
            self.hero3.setStyleSheet("image: url(image/dead.jpeg);")
        d = process_game.hero_four.status
        if d == 'dead':
            self.hero4.setStyleSheet("image: url(image/dead.jpeg);")
        e = process_game.hero_five.status
        if e == 'dead':
            self.hero5.setStyleSheet("image: url(image/dead.jpeg);")
        f = process_game.hero_six.status
        if f == 'dead':
            self.hero6.setStyleSheet("image: url(image/dead.jpeg);")
        g = process_game.hero_seven.status
        if g == 'dead':
            self.hero7.setStyleSheet("image: url(image/dead.jpeg);")
        h = process_game.hero_eight.status
        if h == 'dead':
            self.hero8.setStyleSheet("image: url(image/dead.jpeg);")
        i = process_game.hero_nine.status
        if i == 'dead':
            self.hero9.setStyleSheet("image: url(image/dead.jpeg);")
        j = process_game.hero_ten.status
        if j == 'dead':
            self.hero10.setStyleSheet("image: url(image/dead.jpeg);")

    # Update the blood amount to the display box
    def update_blood(self):
        self.blood1.setValue(int(process_game.hero_one.blood/10))
        self.blood2.setValue(int(process_game.hero_two.blood/10))
        self.blood3.setValue(int(process_game.hero_three.blood/10))
        self.blood4.setValue(int(process_game.hero_four.blood/10))
        self.blood5.setValue(int(process_game.hero_five.blood/10))
        self.blood6.setValue(int(process_game.hero_six.blood/10))
        self.blood7.setValue(int(process_game.hero_seven.blood/10))
        self.blood8.setValue(int(process_game.hero_eight.blood/10))
        self.blood9.setValue(int(process_game.hero_nine.blood/10))
        self.blood10.setValue(int(process_game.hero_ten.blood/10))


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mainwindow)

    mainwindow.show()
    sys.exit(app.exec())



