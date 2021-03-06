from model.profile import Profile

class ProfileHelper:

    def __init__(self, app):
        self.app = app


    def contact_creation(self):
        wd = self.app.wd
        self.contact_creation()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def create_contact(self, profile):
        wd = self.app.wd
        self.open_new_conttact()
        self.fill_new_contact(profile)
        self.save_new_contact()
        self.return_home_page()
        self.profile_cache = None


    def save_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def fill_new_contact(self, profile):
        wd = self.app.wd
        self.change_field_value("firstname", profile.firstname)
        self.change_field_value("lastname", profile.lastname)
        self.change_field_value("nickname", profile.nickname)
        self.change_field_value("address", profile.address)
        self.change_field_value("mobile", profile.mobile)
        self.change_field_value("email", profile.email)
        self.change_field_date("bday", profile.bday)
        self.change_field_date("bmonth", profile.bmonth)
        self.change_field_value("byear", profile.byear)
        self.change_field_value("address2", profile.address2)

    def change_field_date(self, field_data, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_data).click()
            wd.find_element_by_name(field_data).send_keys(text)
            wd.find_element_by_name(field_data).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_new_conttact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.profile_cache = None


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        #open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #fill form
        self.fill_new_contact(new_contact_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.profile_cache = None


    def count(self):
        wd = self.app.wd
        self.select_first_contact()
        return len(wd.find_elements_by_name("selected[]"))

    profile_cache = None


    def get_contact_list(self):
        if self.profile_cache is None:
            wd = self.app.wd
            self.profile_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.profile_cache.append(Profile(firstname=text, id=id))
        return list(self.profile_cache)

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()




















