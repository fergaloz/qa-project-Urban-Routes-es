import data
from pages import UrbanRoutesPage

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def urban_page(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.urban_routes_page = UrbanRoutesPage(self.driver)

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_address = UrbanRoutesPage(self.driver)
        set_address.set_route()

    def test_select_comfort(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_comfort = UrbanRoutesPage(self.driver)
        self.test_set_route()
        set_comfort.select_comfort()

    def test_input_phone(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_phone = UrbanRoutesPage(self.driver)
        self.test_set_route()
        self.test_select_comfort()
        set_phone.phone_number()

    def test_add_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_add_card = UrbanRoutesPage(self.driver)
        self.test_input_phone()
        set_add_card.add_card()

    def test_new_message(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_new_message = UrbanRoutesPage(self.driver)
        self.test_add_card()
        set_new_message.new_message()

    def test_add_blanket(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_blanket = UrbanRoutesPage(self.driver)
        self.test_new_message()
        set_blanket.add_blanket()

    def test_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_ice_cream = UrbanRoutesPage(self.driver)
        self.test_add_blanket()
        set_ice_cream.add_ice_cream()

    def test_order_taxi(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        set_order_taxi = UrbanRoutesPage(self.driver)
        self.test_ice_cream()
        set_order_taxi.order_taxi()












    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
