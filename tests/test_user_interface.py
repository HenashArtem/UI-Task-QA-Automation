from framework.browser.browser import Browser
from tests.pages.home_page import HomePage
from tests.pages.registration_page import RegistrationPage
from tests.config.urls import Urls
from tests.test_data.test_data import TestData
from tests.test_utils.generate_test_data import GenerateTestData
import allure


class Test(object):
    def test_user_interface_registration(self, create_browser):
        with allure.MASTER_HELPER.step("First step"):
            Browser.get_browser().set_url(url=Urls.TEST_STAND_URL)

            home_page = HomePage()

            home_page.wait_for_page_opened()
            assert home_page.is_opened() is True, "Home page loaded incorrectly"

            home_page.click_on_registration_button()

            registration_page = RegistrationPage()

            registration_page.wait_for_page_opened()

            registration_page.wait_page_to_load()
            assert registration_page.is_registration_card_number_correct(TestData.first_card_num) is True, \
                "Card 1 for filling information wasn't opened"

            generate_test_data = GenerateTestData()

            email = generate_test_data.generate_email(TestData.email_size)
            password = generate_test_data.generate_password(TestData.password_size, email[1])
            domain = generate_test_data.generate_domain(TestData.domain_size)

            registration_page.enter_the_password(password)
            registration_page.enter_the_email(email)
            registration_page.enter_the_domain(domain)
            registration_page.select_random_element_in_the_dropdown_menu()
            registration_page.click_checkbox_terms_of_use()
            registration_page.click_next_page_in_the_first_reg_card()

            registration_page.wait_page_to_load()
            assert registration_page.is_registration_card_number_correct(TestData.second_card_num) is True, \
                "Card 2 for filling information wasn't opened"

            registration_page.select_random_checkboxes(TestData.num_of_interests_checkboxes)
            registration_page.upload_image(TestData.file_name, TestData.file_extension)
            registration_page.click_next_page_btn_on_the_second_reg_card()

            registration_page.wait_page_to_load()
            assert registration_page.is_registration_card_number_correct(TestData.third_card_num) is True, \
                "Card 3 for filling information wasn't opened"

    def test_close_help_window(self, create_browser):
        with allure.MASTER_HELPER.step("Second step"):
            Browser.get_browser().set_url(url=Urls.TEST_STAND_URL)

            home_page = HomePage()

            home_page.wait_for_page_opened()
            assert home_page.is_opened() is True, "Home page loaded incorrectly"

            home_page.click_on_registration_button()

            registration_page = RegistrationPage()

            registration_page.wait_for_page_opened()
            registration_page.close_help_window()
            assert registration_page.is_help_window_hidden() is True, "Help window wasn't closed"

    def test_accept_cookies(self, create_browser):
        with allure.MASTER_HELPER.step("Third step"):
            Browser.get_browser().set_url(url=Urls.TEST_STAND_URL)

            home_page = HomePage()

            home_page.wait_for_page_opened()
            assert home_page.is_opened() is True, "Home page loaded incorrectly"

            home_page.click_on_registration_button()

            registration_page = RegistrationPage()

            registration_page.wait_for_page_opened()
            registration_page.accept_cookies()
            assert registration_page.is_cookies_window_closed() is False, "Cookies window wasn't closed"

    def test_timer_check(self, create_browser):
        with allure.MASTER_HELPER.step("Fourth step"):
            Browser.get_browser().set_url(url=Urls.TEST_STAND_URL)

            home_page = HomePage()

            home_page.wait_for_page_opened()
            assert home_page.is_opened() is True, "Home page loaded incorrectly"

            home_page.click_on_registration_button()

            registration_page = RegistrationPage()

            registration_page.wait_for_page_opened()
            assert registration_page.get_time_from_timer() == TestData.timer_expected_time, "time runs incorrectly"
