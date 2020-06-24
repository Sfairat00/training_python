from selenium import webdriver
from fixture.session_contact import SessionContactHelper
from fixture.profile import ProfileContactHelper

class Application_contact:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_contact = SessionContactHelper(self)
        self.profile = ProfileContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/edit.php")

    def destroy(self):
        self.wd.quit()


