from utilities.manage_pages import *


class TestSanityScenarios:
    def test_home_page_logo(self, pages):
        pages.home_page.navi_to_homepage()
        assert pages.home_page.is_logo_displayed(), "Logo is not displayed"

    def test_login_action(self, pages):
        pages.home_page.navi_to_login()
        pages.login_page.login_action("user4Test@example.com", "userPassword")
        assert pages.login_page.get_user_name() == "Sam One", "Login fails"

    def test_create_user(self, pages):
        pages.home_page.navi_to_login()
        pages.create_user_page.create_user_action("user4Test2323@example.com", "John", "Doe", "123456", "1", "January", "2000")
