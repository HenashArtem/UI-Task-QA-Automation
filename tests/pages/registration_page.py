# coding=utf-8

import random
import os

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from framework.elements.button import Button
from framework.elements.checkbox import Checkbox
from framework.elements.dropdown_menu import DropdownMenu
from framework.elements.label import Label
from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage
from framework.utils.upload_file import UploadFile


class RegistrationPage(BasePage):
    txb_password = TextBox(search_condition=By.XPATH, locator="//input[contains(@placeholder, 'hoose') and "
                                                              "contains(@placeholder, 'assword')]",
                           name="Password textbox")
    txb_email = TextBox(search_condition=By.XPATH,
                        locator="//input[contains(@placeholder, 'our') and contains(@placeholder, 'mail')]",
                        name='Email input')
    txb_domain = TextBox(search_condition=By.XPATH, locator="//input[@placeholder = 'Domain']",
                         name='Domain input')
    checkbox_terms_of_use = Checkbox(search_condition=By.XPATH,
                                     locator="//label[@for = 'accept-terms-conditions']", name='Checkbox terms of use')
    next_page_button = Button(search_condition=By.XPATH,
                              locator="//a[contains(@class,'button') and contains(@class,'secondary') and text("
                                      ")='Next']", name='Next page button')
    dropdown_menu = DropdownMenu(search_condition=By.XPATH, locator="//div[@class = 'dropdown__opener']",
                                 name='Dropdown menu')
    dropdown_list_of_el = DropdownMenu(search_condition=By.XPATH, locator="//div[@class= 'dropdown__list']//div",
                                       name='Dropdown menu list')
    close_hurry_up_window = Label(search_condition=By.XPATH, locator="//span[contains(@class, 'modal') and "
                                                                     "contains(@class, 'close')]//span",
                                  name='Button close hurry up window')
    interests_checkboxes_list = Checkbox(search_condition=By.XPATH,
                                         locator="//span[contains(@class,'checkbox small')]//label",
                                         name="Interests checkboxes list")
    names_list_in_interests_checkboxes = Label(search_condition=By.XPATH, locator="//span[@class = 'checkbox small']//"
                                                                                  "following-sibling::span[text()]",
                                               name="Hurry up window")
    unselect_all_checkbox = Checkbox(search_condition=By.XPATH, locator="//label[@for = 'interest_unselectall']",
                                     name="Unselect all checkbox")
    image_upload_button = Button(search_condition=By.XPATH, locator="//a[contains(@class,'pload') and "
                                                                    "contains(@class,'utton')]",
                                 name='Image upload button')
    download_the_avatar_btn = Button(search_condition=By.XPATH, locator="//button[contains(@class, 'upload-button')]",
                                     name="Download avatar button")
    next_page_btn_in_interests_menu = Button(search_condition=By.XPATH, locator="//button[@name='button' and "
                                                                                "text()='Next']",
                                             name='Next page button in interests menu')
    help_form_container = Label(search_condition=By.XPATH, locator="//div[contains(@class, "
                                                                   "'help-form__container')]",
                                name="Help form container")
    close_help_window_btn = Button(search_condition=By.XPATH, locator="//button[contains(@class, 'ottom')]",
                                   name="Close help window button")
    cookies_window = Button(search_condition=By.XPATH, locator="//button[contains(@type, 'button') and text("
                                                               ")='Not really, no']", name="Cookies window")
    time_from_timer = Label(search_condition=By.XPATH, locator="//div[contains(@class, 'timer')]",
                            name='Time from timer')
    registration_card_number = Label(search_condition=By.XPATH, locator="//div[contains(@class, "
                                                                        "'page-indicator')]",
                                     name='Registration card number')
    help_window_raise_btn = Button(search_condition=By.XPATH, locator="//span[@class='icon icon-chevron-up']",
                                   name="Raise help window button")

    def __init__(self):
        super().__init__(search_condition=By.XPATH,
                         locator="//div[contains(@class, 'timer')]",
                         page_name=self.__class__.__name__)
        super().wait_for_page_opened()

    def is_registration_card_number_correct(self, expected_card_num):
        if self.registration_card_number.is_displayed():
            registration_card_number_text = self.registration_card_number.get_text().split()
            return registration_card_number_text[0] == expected_card_num
        else:
            raise NoSuchElementException(f"Element {RegistrationPage.registration_card_number.get_name()} with locator:"
                                         f"{RegistrationPage.registration_card_number.get_locator()} isn't exist")

    def enter_the_password(self, password):
        self.txb_password.wait_for_clickable()
        self.txb_password.click()
        self.txb_password.clear_field()
        self.txb_password.send_keys(password)

    def enter_the_email(self, email):
        self.txb_email.wait_for_clickable()
        self.txb_email.click()
        self.txb_email.clear_field()
        self.txb_email.send_keys(email)

    def enter_the_domain(self, domain):
        self.txb_domain.wait_for_clickable()
        self.txb_domain.click()
        self.txb_domain.clear_field()
        self.txb_domain.send_keys(domain)

    def select_random_element_in_the_dropdown_menu(self):
        self.dropdown_menu.wait_for_clickable()
        self.dropdown_menu.click()
        elements_list = self.dropdown_list_of_el.get_elements()
        random_choice = random.choice(elements_list)
        random_choice.click()

    def click_checkbox_terms_of_use(self):
        if not self.checkbox_terms_of_use.is_selected():
            self.checkbox_terms_of_use.click()

    def click_next_page_in_the_first_reg_card(self):
        self.next_page_button.wait_for_clickable()
        self.next_page_button.click()

    def select_random_checkboxes(self, num_of_checkbox):
        self.unselect_all_checkbox.wait_for_clickable()
        self.unselect_all_checkbox.click()

        interests_checkboxes_list = self.interests_checkboxes_list.get_elements()

        for index, value in enumerate(interests_checkboxes_list):
            if interests_checkboxes_list[index].get_attribute("for") == "interest_unselectall" or \
                    interests_checkboxes_list[index].get_attribute("for") == "interest_selectall":
                interests_checkboxes_list.remove(value)

        for i in range(num_of_checkbox):
            random_choice = random.choice(interests_checkboxes_list)
            random_choice.click()
            interests_checkboxes_list.remove(random_choice)

    def upload_image(self, file_name, file_extension):

        files_to_upload_path = os.path.abspath(r'tests\test_data\files_to_upload')
        image_file_path = files_to_upload_path + f"\\{str(file_name)}" + f".{file_extension}"
        if os.path.exists(f'{image_file_path}'):
            self.image_upload_button.wait_for_is_present()
            self.image_upload_button.click()
            UploadFile.upload_file(image_file_path)
        else:
            raise Exception(f"File {file_name} isn't exist")

    def click_next_page_btn_on_the_second_reg_card(self):
        self.next_page_btn_in_interests_menu.wait_for_clickable()
        self.next_page_btn_in_interests_menu.click()

    def close_help_window(self):
        self.help_form_container.wait_for_is_present()
        self.close_help_window_btn.click()

    def is_help_window_hidden(self):
        return self.help_window_raise_btn.is_element_invisible()

    def accept_cookies(self):
        self.cookies_window.wait_for_is_present()
        self.cookies_window.click()

    def is_cookies_window_closed(self):
        return self.cookies_window.is_displayed()

    def get_time_from_timer(self):
        self.time_from_timer.wait_for_is_present()
        return self.time_from_timer.get_text()
