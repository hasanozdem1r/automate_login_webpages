from automate_login import *

class Login_System:
    #class constructor
    def __init__(self,file_path):
        self._file_path=file_path
        self._file_dataframe=read_excel(file_path)

    def login_system(self):
        for index,row in self._file_dataframe.iterrows():
            #print(row["email"], row["password"], row["platform"])
            if (row["platform"].lower()=="linkedin"):
                print("Linkedin")
                object = Automate_Login(row["email"],row["password"])
                object.close_session()
                object.login_linkedin()
            elif (row["platform"].lower()=="google"):
                print("Google")
                object = Automate_Login(row["email"], row["password"])
                object.login_google_services()
                object.close_session()
            elif (row["platform"].lower()=="github"):
                print("Github")
                object = Automate_Login(row["email"], row["password"])
                object.login_github()
                object.close_session()
            else:
                print("Not Valid")


login=Login_System("D:\\my_works\\Not_Important\\Python\\PLURALSIGHT\\authentication.xlsx")
login.login_system()