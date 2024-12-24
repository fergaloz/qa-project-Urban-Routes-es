from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import data
from selenium.webdriver import Keys, ActionChains
from helpers import retrieve_phone_code




class UrbanRoutesPage:
    logo = (By.CLASS_NAME, 'logo')
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    TAXI_CONTAINER = (By.CLASS_NAME, 'workflow-subcontainer')
    TAXI_BUTTON = (By.CLASS_NAME, 'button.button.round')
    COMFORT_TARIFF = (By.CLASS_NAME, 'tcard-title')
    PHONE_FIELD = (By.CLASS_NAME, 'np-button')
    INPUT_PHONE = (By.ID, 'phone')
    SUBMIT_BUTTON = (By.CLASS_NAME, 'button.button.full')

    SEND_NEW_CODE = (By.XPATH, "//button[@type='button']")
    CLOSE_CODE_TAB = (By.CSS_SELECTOR, 'button.close-button.section-close')
    PP_FIELD = (By.CLASS_NAME, 'pp-button.filled')
    ADD_CARD = (By.CLASS_NAME, 'pp-row.disabled')
    INPUT_CARD = (By.CLASS_NAME, 'card-input')
    INPUT_CODE = (By.NAME, 'code')
    ADD_CARD_BUTTON = (By.XPATH, '//button[contains(@class, "button full") and text()="Agregar"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'button.close-button.section-close')
    ADD_MESSAGE = (By.ID, 'comment')
    REQS_BLANKET = (By.CLASS_NAME, 'slider.round')
    REQS_ICE_CREAM = (By.CLASS_NAME, 'counter-plus')
    before_click = (By.CLASS_NAME, 'counter-value')
    ORDER_BOTTON = (By.CLASS_NAME, 'smart-button')
    FIND_TAXI = (By.CLASS_NAME, 'order-header-title')
    INFO_TAXI_DRIVER = (By.CLASS_NAME, 'order-number')



    def __init__(self, driver):
        self.driver = driver

    def set_from(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'logo')))
        self.driver.find_element(*self.from_field).send_keys(data.ADDRESS_FROM)

    def set_to(self):
        self.driver.find_element(*self.to_field).send_keys(data.ADDRESS_TO)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self):  # PASO QUE COMBINA DESDE Y HASTA
        self.set_from()
        self.set_to()


    def click_taxi_button(self):
        WebDriverWait(self.driver,5).until(expected_conditions.presence_of_element_located(self.TAXI_CONTAINER))
        taxi_click=WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(self.TAXI_BUTTON))
        taxi_click.click()

    def click_comfort_button(self):

        self.driver.find_elements(*self.COMFORT_TARIFF)[4].click()

    def select_comfort(self):                         #PASO PARA SELECCIONAR COMFORT
        self.click_taxi_button()
        self.click_comfort_button()


    def click_phone_field(self):
        self.driver.find_element(*self.PHONE_FIELD).click()

    def input_phone(self):
        self.driver.find_element(*self.INPUT_PHONE).send_keys(data.PHONE_NUMBER)

    def next_field(self):
        self.driver.find_elements(*self.SUBMIT_BUTTON)[0].click()

    def sms_code(self):
        confirmation_code = retrieve_phone_code(self.driver)
        confirmation_code



    def close_tab(self):
        self.driver.find_elements(*self.CLOSE_CODE_TAB)[1].click()

    def phone_number(self):                      #PASO PARA RELLENAR EL NUMERO DE TELEFONO
        self.click_phone_field()
        self.input_phone()
        self.next_field()
        self.sms_code()
        self.close_tab()


    def select_method_payment(self):
        self.driver.find_element(*self.PP_FIELD).click()

    def select_add_card(self):
        self.driver.find_element(*self.ADD_CARD).click()

    def input_card_number(self):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'card-input')))
        add_card = self.driver.find_element(*self.INPUT_CARD)
        add_card.send_keys(data.CARD_NUMBER)
        add_card.send_keys(Keys.SPACE)
        card_value = add_card.get_attribute('value')
        assert '1234 5678 9100' in card_value, f'El valor del campo no contiene "1234 5678 9100". Valor actual: {card_value}"'

    def input_code_number(self):
        add_code = self.driver.find_element(*self.INPUT_CODE)
        add_code.send_keys(data.CARD_CODE)
        add_code.send_keys(Keys.SPACE)
        code_value = add_code.get_attribute('value')
        assert '111' in code_value, f'El valor del campo no contiene "111". Valor actual: {code_value}"'

    def click_add_card_button(self):
        self.driver.find_element(*self.ADD_CARD_BUTTON).click()
        self.driver.find_elements(*self.CLOSE_BUTTON)[2].click()

    def add_card(self):                              #PASO PARA AGREGAR UNA TARJETA
        self.select_method_payment()
        self.select_add_card()
        self.input_card_number()
        self.input_code_number()
        self.click_add_card_button()


    def new_message(self):
        add_message = self.driver.find_element(*self.ADD_MESSAGE)
        add_message.send_keys(data.MESSAGE_FOR_DRIVER)
        message_value = add_message.get_attribute('value')
        assert 'Muestrame el camino' in message_value, f'El valor del campo no contiene "Muestrame el camino". Valor actual: {message_value}"'

    def add_blanket(self):
        self.driver.find_element(*self.REQS_BLANKET).click()

    def add_ice_cream(self):
        ice_cream = self.driver.find_elements(*self.REQS_ICE_CREAM)
        before_click = self.driver.find_elements(*self.before_click)[0]
        value = int(before_click.text)
        actions = ActionChains(self.driver)
        actions.double_click(ice_cream[0]).perform()
        after_click = int(before_click.text)
        assert  after_click == value + 2, f'counter-plus disabled'

    def order_taxi(self):
        self.driver.find_element(*self.ORDER_BOTTON).click()
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located(self.FIND_TAXI))


















