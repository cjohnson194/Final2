from PyQt5.QtWidgets import *
from welcome import *
from login import *
from register import *
from login_succ import *
from forgotpass import *
import csv
import pandas as pd

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

username = ''


class MainWindow(QMainWindow, Ui_Welcome):
    """
    class that runs the welcome screen
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Method to establish button and corresponding methods
        """
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.login = Login()
        self.register = Register()
        self.welcomeButton_register.clicked.connect(self.openregister)
        self.welcomeButton_login.clicked.connect(self.openlogin)

    def openregister(self) -> None:
        """
        Method that opens up register screen, needs fixed
        """
        # DEBUG: close main window
        self.register.show()
        self.hide()

    def openlogin(self) -> None:
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
    def __init__(self, *args, **kwargs) -> None:
        """
        Method to establish button and corresponding methods
        """
        super(Register, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.RegisterPushButton_back.clicked.connect(lambda: self.welcome())
        self.RegisterPushButton_register.clicked.connect(lambda: self.register())
        self.register_output_label.setText('')

        #hides/shows password line when clicked
        self.eyepass_button_register.clicked.connect(self.toggle_password_visibility_pass)
        self.eyepass_button_register_2.clicked.connect(self.toggle_password_visibility_con)

    def welcome(self) -> None:
        """
        Method to go back to welcome screen
        """
        self.mainscreen = MainWindow()
        self.mainscreen.show()
        self.hide()

    def register(self) -> None:
        """
        Method to register new users
        """
        # get values
        username = self.registerLineEdit_username.text()
        password = self.registerLineEdit_password.text()
        con_password = self.registerLineEdit_password_con.text()
        fname = self.registerLineEdit_firstname.text()
        lname = self.registerLineEdit_lastname.text()
        email = self.registerLineEdit_email.text()
        phone_num = self.registerLineEdit_phone_number.text()

        # radiobutton values
        gender = 'N/A'
        if self.female_button.isChecked():
            gender = 'Female'
        elif self.male_button.isChecked():
            gender = 'Male'
        elif self.noanswer_button.isChecked():
            gender = 'N/A'
        
        try:
            sample_usernames = []
            sample = open('sample.csv', 'r')
            content = csv.reader(sample)
            for line in content:
                sample_usernames.append(line[5])
            sample.close()
        except FileNotFoundError:
            self.register_output_label.setText('No Sample file detected. Please run sample.py before continuing.')

        if username == '' or password == '' or con_password == '' or fname == '' or lname == '' or email == '' or phone_num == '' or (self.female_button.isChecked() == False and self.male_button.isChecked() == False and self.noanswer_button.isChecked() == False):
            self.register_output_label.setText('Please enter all necessary information')
        elif username in sample_usernames:
            self.register_output_label.setText('Username is taken. Please choose another one.')
        elif password != con_password:
            self.register_output_label.setText('Confirmation Password and Password do not match. Please try again!')
        else:
            with open('sample.csv', 'a', newline='') as sample:
                content = csv.writer(sample)
                content.writerow([fname, lname, gender, email, phone_num, username, password])
            self.register_output_label.setText('Registration Successful! :-)')
    
    def toggle_password_visibility_pass(self) -> None:
        """
        Method to change visibility in password Lineedit
        """
        if self.registerLineEdit_password.echoMode() == QLineEdit.Normal:
            self.registerLineEdit_password.setEchoMode(QLineEdit.Password)
        else:
            self.registerLineEdit_password.setEchoMode(QLineEdit.Normal)
    
    def toggle_password_visibility_con(self) -> None:
        """
        Method to change visibility in confirmation password Lineedit
        """
        if self.registerLineEdit_password_con.echoMode() == QLineEdit.Normal:
            self.registerLineEdit_password_con.setEchoMode(QLineEdit.Password)
        else:
            self.registerLineEdit_password_con.setEchoMode(QLineEdit.Normal)

class Login(QMainWindow, Ui_Login):
    """
    class that runs the login screen
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Method to establish button and corresponding methods
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.LoginpushButton_back.clicked.connect(lambda: self.welcome())
        self.LoginpushButton_login.clicked.connect(lambda: self.login())
        self.button_forgot_password.clicked.connect(lambda: self.forgot_password())
        self.login_output_label.setText('')

        #hides/shows password line when clicked
        self.eyepass_login.clicked.connect(self.toggle_password_visibility)

    def welcome(self) -> None:
        """
        Method to go back to welcome screen
        """
        self.mainscreen = MainWindow() 
        self.mainscreen.show()
        self.hide()

    def login(self) -> None:
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
                        sample_data.append([line[5], line[6]])
                # check if login is in CSV file
                for sample in sample_data:
                    if sample == login:
                        self.login_output_label.setText('Login successful :-)')
                        self.login_succ(username, password)
                    else:
                        self.login_output_label.setText('Login unsuccessful. Please try again or Register. :-)')
            except FileNotFoundError:
                self.login_output_label.setText('No Sample file detected. Please run sample.py before continuing.')

    def toggle_password_visibility(self) -> None:
        """
        Method to change visibility on password Lineedit
        """
        if self.LoginlineEdit_password.echoMode() == QLineEdit.Normal:
            self.LoginlineEdit_password.setEchoMode(QLineEdit.Password)
        else:
            self.LoginlineEdit_password.setEchoMode(QLineEdit.Normal)
    
    def forgot_password(self) -> None:
        """
        Method to take user to forgot password GUI
        """
        forgot_pass = ForgotPass()
        forgot_pass.show()
        self.hide()
    
    def login_succ(self, username: str, password: str) -> None:
        """
        Method to open the successful login GUI and send username and password
        :param username: username entered in login GUI
        :param password: password entered in login GUI
        """
        self.login_succ = LoginSucc(username, password)
        self.login_succ.show()
        self.hide()

class LoginSucc(QMainWindow, Ui_LoginSucc):
    """
    Class that runs the window that shows up when someone successfully logs in
    """
    def __init__(self, username: str, password: str, *args, **kwargs) -> None:
        """
        Method to establish button and corresponding methods
        :param username: username entered in login GUI
        :param password: password entered in login GUI
        """
        super(LoginSucc, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.username = username
        self.password = password
        self.cat_image.clicked.connect(lambda: self.happy_login())

    def happy_login(self):
        """
        Method that displays user's first and last name when they have logged in and clicked cat photo
        """
        self.label_click_me.hide()

        flnames = list()
        with open('sample.csv', 'r') as sample:
            content = csv.reader(sample)
            for line in content:
                if line[5] == self.username and line[6] == self.password:
                    flnames.append(line[0])
                    flnames.append(line[1])
        self.succ_login_label.setText(f'Welcome {flnames[0]} {flnames[1]}')

class ForgotPass(QMainWindow, Ui_ForgotPass):
    """
    class that runs the login screen
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Method to establish button and corresponding methods
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.ForgotPass_button_back.clicked.connect(lambda: self.login())
        self.ForgotPass_button_submit.clicked.connect(lambda: self.submit())

        # hide/show passwords
        self.ForgotPass_eyepass_login.hide()
        self.ForgotPass_eyepass_login_2.hide()
        self.ForgotPass_eyepass_login.clicked.connect(lambda: self.toggle_visibility())
        self.ForgotPass_eyepass_login_2.clicked.connect(lambda: self.toggle_visibility_2())
    
    def login(self) -> None:
        """
        Method to take user back to login GUI
        """
        login = Login()
        login.show()
        self.hide()

    def submit(self) -> None:
        """
        Method to locate user's account and allow them to change their password
        """
        num = 0
        if self.ForgotPass_label_phone_number.text() == 'Phone Number':
            # get inputs from user
            global username
            username = self.ForgotPassLineEdit_username.text()
            email = self.ForgotPassLineEdit_email.text()
            phone_num = self.ForgotPassLineEdit_phone_number.text()

            sample_users = []
            sample_emails = []
            sample_phone_numbers = []

            try:
                with open('sample.csv', 'r') as sample:
                    content = csv.reader(sample)
                    for line in content:
                        sample_users.append(line[5])
                        sample_emails.append(line[3])
                        sample_phone_numbers.append(line[4])
            except FileNotFoundError:
                self.ForgotPass_label_output.setText('No Sample file detected. Please run sample.py before continuing.')

            if username == '' or email == '' or phone_num == '':
                self.ForgotPass_label_output.setText('Please enter all necessary information.')
            elif username not in sample_users:
                self.ForgotPass_label_output.setText("Username not in system. Please register new user.")
            elif email not in sample_emails or phone_num not in sample_phone_numbers:
                self.ForgotPass_label_output.setText("Email or phone number not in system. Please register new user.")
            else:
                for num in range(len(sample_users)):
                    if username == sample_users[num] and email == sample_emails[num] and phone_num == sample_phone_numbers[num]:
                        self.ForgotPass_label_output.setText('Information found!')
                        # switch GUI to a change password one
                        self.ForgotPass_label_email.hide()
                        self.ForgotPassLineEdit_email.hide()
                        self.ForgotPassLineEdit_phone_number.clear()
                        self.ForgotPassLineEdit_username.clear()
                        self.ForgotPass_label_phone_number.setText('New Password')
                        self.ForgotPassLineEdit_phone_number.setEchoMode(QLineEdit.Password)
                        self.ForgotPass_label_username.setText('Confirm New Password')
                        self.ForgotPassLineEdit_username.setEchoMode(QLineEdit.Password)
                        self.ForgotPass_eyepass_login.show()
                        self.ForgotPass_eyepass_login_2.show()
        else:
            # get user inputs
            password = self.ForgotPassLineEdit_phone_number.text()
            con_password = self.ForgotPassLineEdit_username.text()

            # change password in CSV File
            if password != con_password:
                self.ForgotPass_label_output.setText('Passwords do not match. Please try again.')
            else:
                pass_index = 0
                container = []
                with open('sample.csv', 'r') as sample:
                    content = csv.reader(sample)
                    for line in content:
                        container.append(line)
                        if line[5] == username:
                            pass_index = container.index(line)
                # use panda module to change password
                new_pass = pd.read_csv("sample.csv")
                new_pass.loc[(pass_index-1), 'Password'] = password
                new_pass.to_csv('sample.csv', index=False)
                self.ForgotPass_label_output.setText("Password changed. Select 'Back' to get back to login screen.")

    def toggle_visibility(self) -> None:
        """
        Method to change visibility in phone number Lineedit
        """
        if self.ForgotPassLineEdit_phone_number.echoMode() == QLineEdit.Normal:
            self.ForgotPassLineEdit_phone_number.setEchoMode(QLineEdit.Password)
        else:
            self.ForgotPassLineEdit_phone_number.setEchoMode(QLineEdit.Normal)
    
    def toggle_visibility_2(self) -> None:
        """
        Method to change visibility in email Lineedit
        """
        if self.ForgotPassLineEdit_username.echoMode() == QLineEdit.Normal:
            self.ForgotPassLineEdit_username.setEchoMode(QLineEdit.Password)
        else:
            self.ForgotPassLineEdit_username.setEchoMode(QLineEdit.Normal)
