from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text_box import TextBox
from framework.elements.label import Label
from framework.elements.button import Button


class HomePage(BasePage):
    txb_login = TextBox(search_condition=By.XPATH,
                        locator='//*[contains(@class, "auth-input") and contains(@class, "auth-input_primary")]['
                                '@type="text"]', name='Login')
    txb_password = TextBox(search_condition=By.XPATH,
                           locator="//input[@placeholder='Choose Password']", name='login')
    btn_login = Button(search_condition=By.XPATH,
                       locator='//button[contains(@class, "auth-button")][@type="submit"]', name='Login')

    lbl_menu = Label(search_condition=By.XPATH, locator='//li[@class="b-main-navigation__item"]//a',
                     name='Menu')

    lbl_menu_bank = Label(search_condition=By.XPATH, locator="//div[contains(@class, 'social-likes')]",
                          name="menu_bank")
    registration_btn = Button(search_condition=By.XPATH, locator="//a[@class='start__link']",
                              name="Registration button")

    def __init__(self):
        super().__init__(search_condition=By.XPATH, locator="//a[@class='start__link']",
                         page_name=self.__class__.__name__)
        super().wait_for_page_opened()

    def click_on_registration_button(self):
        self.registration_btn.click()
