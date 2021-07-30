from init import *

authentication_df=read_excel("D:\\my_works\\Not_Important\\Python\\PLURALSIGHT\\authentication.xlsx")
email=authentication_df['email'][0]
password=authentication_df['password'][0]
platform=authentication_df['platform'][0]

class Automate_Login:

    def __init__(self,email,password):
        self.driver = webdriver.Chrome("C:\\Users\\bear_s_computer\\Desktop\\APPS\\Browser\\chromedriver.exe")
        self.email=email
        self.password=password

    #this method use to login gmail mail service
    def login_gmail(self):
        self.driver.get("https://www.gmail.com")
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(self.email)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()

    def login_github(self):
        self.driver.get("https://github.com/login")
        sleep(1)
        self.driver.find_element_by_id("login_field").send_keys(self.email)
        sleep(1)
        self.driver.find_element_by_id("password").send_keys(self.password)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()



object=Automate_Login(email=email,password=password)

#object.login_gmail()
object.login_github()