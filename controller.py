from PyQt5.QtWidgets import *
from welcome import *
from login import *
from register import *
import csv

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# widget = QStackedWidget


class MainWindow(QMainWindow, Ui_Welcome):
    """
    class that runs the welcome screen
    """
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        #self.welcome = MainWindow()
        self.login = Login()
        self.register = Register()
        self.welcomeButton_register.clicked.connect(self.openregister)
        self.welcomeButton_login.clicked.connect(self.openlogin)

    def openregister(self):
        """
        Method that opens up register screen, needs fixed
        """
        # DEBUG: close main window
        self.register.show()
        self.hide()



    def openlogin(self):
        """
        Method that opens the login screen, needs fixed
        """
        # DEBUG: close main window
        self.login.show()
        self.hide()


class Register(QMainWindow, Ui_Register):
    """
    class that runs the register screen
    """
    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.RegisterPushButton_back.clicked.connect(lambda: self.welcome())
        self.RegisterPushButton_register.clicked.connect(lambda: self.register())
        self.register_output_label.setText('')

    def welcome(self):
        """
        Method to go back to welcome screen
        """
        self.mainscreen = MainWindow()
        self.mainscreen.show()
        self.hide()


    def register(self):
        """
        Method to register new users
        """
        # get values
        username = self.registerLineEdit_username.text()
        password = self.registerLineEdit_password.text()

        if username == '' and password == '':
            self.register_output_label.setText('Please enter a username and password')
        elif username == '' and password != '':
            self.register_output_label.setText('Please enter a username')
        elif password == '' and username != '':
            self.register_output_label.setText('Please enter a password')
        else:
            with open('sample.csv', 'a', newline='') as sample:
                content = csv.writer(sample)
                content.writerow([username, password])
            self.register_output_label.setText('Registration Successful! :-)')


class Login(QMainWindow, Ui_Login):
    """
    class that runs the login screen
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.LoginpushButton_back.clicked.connect(lambda: self.welcome())
        self.LoginpushButton_login.clicked.connect(lambda: self.login())
        self.login_output_label.setText('')

    def welcome(self):
        """
        Method to go back to welcome screen
        """
        self.mainscreen = MainWindow()
        self.mainscreen.show()
        self.hide()

    def login(self):
        """
        Method to handle if login button is pressed
        """
        # get inputs
        username = self.LoginlineEdit_username.text()
        password = self.LoginlineEdit_password.text()
        login = [username, password]
        sample_data = []

        # make sure there was input
        if username == '' and password == '':
            self.login_output_label.setText('Please input Username and Password.')
        elif username == '' and password != '':
            self.login_output_label.setText('Please enter Username')
        elif password == '' and username != '':
            self.login_output_label.setText('Please enter Password')
        else:
            # if CSV file exists, open and read all values and compare with login
            try:
                with open('sample.csv', 'r') as sample:
                    content = csv.reader(sample)
                    for line in content:
                        sample_data.append(line)
                # check if login is in CSV file
                for sample in sample_data:
                    if sample == login:
                        self.login_output_label.setText('Login successful :-)')
                    else:
                        self.login_output_label.setText('Login unsuccessful. Please try again or Register. :-)')
            except FileNotFoundError:
                self.login_output_label.setText('No logins created. Please register before continuing. :-)')

