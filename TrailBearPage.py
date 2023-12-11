import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TrailBearLocators:
    LOCATOR_TrailBear_BUTTON_MYWORK = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/a[1]')
    LOCATOR_TrailBear_MYWORK_EL = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div[1]/p[1]')
    LOCATOR_TrailBear_BUTTON_REVIEWS = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/a[2]')
    LOCATOR_TrailBear_REVIEWS_EL = (By.XPATH, '//*[@id="feedback"]/div/div/h5')
    LOCATOR_TrailBear_BUTTON_FEEDBACK = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/a[3]')
    LOCATOR_TrailBear_FEEDBACK_EL = (By.XPATH, '//*[@id="feedback"]/footer/button')
    LOCATOR_TrailBear_BUTTON_VK = (By.XPATH, '//*[@id="feedback"]/footer/p[1]/a')
    LOCATOR_TrailBear_VK_EL = (By.XPATH, '//*[@id="owner_page_name"]')
    LOCATOR_TrailBear_BUTTON_WHATSAPP = (By.XPATH, '//*[@id="feedback"]/footer/p[2]/a')
    LOCATOR_TrailBear_WHATSAPP_EL = (By.XPATH, '//*[@id="main_block"]/div[1]/h2/p/text()')
    LOCATOR_TrailBear_BUTTON_TrailBear = (By.XPATH, '//*[@id="feedback"]/footer/button')
    LOCATOR_TrailBear_BUTTON = (By.XPATH, '//*[@id="feedback"]/button')
    LOCATOR_TrailBear_BUTTON_EL = (By.XPATH, '//*[@id="root"]/div/header/div')
    LOCATOR_TrailBear_FIELD_NAME = (By.XPATH, '//*[@id="feedback"]/div/div/form/label[1]/input')
    LOCATOR_TrailBear_FIELD_EMAIL = (By.XPATH, '//*[@id="feedback"]/div/div/form/label[2]/input')
    LOCATOR_TrailBear_FIELD_PHONE = (By.XPATH, '//*[@id="feedback"]/div/div/form/label[3]/input')
    LOCATOR_TrailBear_BUTTON_Submityourapplication = (By.XPATH, '//*[@id="feedback"]/div/div/form/button')
    LOCATOR_TrailBear_BUTTON_ORDER = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div[1]/button')
    LOCATOR_TrailBear_FIELD_ORDER_NAME = (By.XPATH, '/html/body/div[3]/div/div/div[2]/form/input[1]')
    LOCATOR_TrailBear_FIELD_ORDER_EMAIL = (By.XPATH, '/html/body/div[3]/div/div/div[2]/form/input[2]')
    LOCATOR_TrailBear_FIELD_ORDER_PHONE = (By.XPATH, '/html/body/div[3]/div/div/div[2]/form/input[3]')
    LOCATOR_TrailBear_BUTTON_ARRANGE = (By.XPATH, '/html/body/div[3]/div/div/div[2]/form/button')
    LOCATOR_TrailBear_FORM_ORDER_A_PRODUCT = (By.XPATH, '/html/body/div[3]/div/div/div[1]/div')

class TrailBearHelper(BasePage):

    def click_mywork(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON_MYWORK).click()

    def mens_bag(self):
        element_mywork = self.driverwait(TrailBearLocators.LOCATOR_TrailBear_MYWORK_EL)
        return element_mywork.text

    def click_reviews(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON_REVIEWS).click()

    def consultation(self):
        element_reviews = self.driverwait(TrailBearLocators.LOCATOR_TrailBear_REVIEWS_EL)
        return element_reviews.text

    def click_feedback(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON_FEEDBACK).click()

    def trail_bear(self):
        element_feedback = self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FEEDBACK_EL)
        return element_feedback.text

    def click_vk(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON_VK).is_enabled()



    def click_whatsapp(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON).click()



    def click_trailbear(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON_TrailBear).click()

    def click_button(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON).click()

    def handmade_products(self):
        element_button = self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON_EL)
        return element_button.text

    def submityourapplication(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FIELD_NAME).send_keys('Вадим')
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FIELD_EMAIL).send_keys('vadimalekseev640@gmail.com')
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FIELD_PHONE).send_keys('+79605701704')
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON_Submityourapplication).click()

    def order_a_product(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON_MYWORK).click()
        time.sleep(1)
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON_ORDER).click()
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FIELD_ORDER_NAME).send_keys('Вадим')
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FIELD_ORDER_EMAIL).send_keys('vadimalekseev640@gmail.com')
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FIELD_ORDER_PHONE).send_keys('+79605701704')
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_BUTTON_ARRANGE).click()

    def form_order(self):
        element_form = self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FORM_ORDER_A_PRODUCT)
        return element_form.text

