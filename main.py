import data
from clase import UrbanRoutesPage

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""


    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def urban_page(self):
        self.driver.get(data.urban_routes_url)
        self.urban_routes_page = UrbanRoutesPage(self.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        set_address = UrbanRoutesPage(self.driver)
        set_address.set_route()

    def test_select_comfort(self):
        self.driver.get(data.urban_routes_url)
        set_comfort = UrbanRoutesPage(self.driver)
        set_comfort.set_route()
        set_comfort.select_comfort()

    def test_input_phone(self):
        self.driver.get(data.urban_routes_url)
        set_phone = UrbanRoutesPage(self.driver)
        set_phone.set_route()
        set_phone.select_comfort()
        set_phone.phone_number()

    def test_add_card(self):
        self.driver.get(data.urban_routes_url)
        set_add_card = UrbanRoutesPage(self.driver)
        set_add_card.set_route()
        set_add_card.select_comfort()
        set_add_card.phone_number()
        set_add_card.add_card()

    def test_new_message(self):
        self.driver.get(data.urban_routes_url)
        set_new_message = UrbanRoutesPage(self.driver)
        set_new_message.set_route()
        set_new_message.select_comfort()
        set_new_message.phone_number()
        set_new_message.add_card()

    def test_add_blanket(self):
        self.driver.get(data.urban_routes_url)
        set_blanket = UrbanRoutesPage(self.driver)
        set_blanket.set_route()
        set_blanket.select_comfort()
        set_blanket.phone_number()
        set_blanket.add_card()
        set_blanket.add_blanket()

    def test_ice_cream(self):
        self.driver.get(data.urban_routes_url)
        set_ice_cream = UrbanRoutesPage(self.driver)
        set_ice_cream.set_route()
        set_ice_cream.select_comfort()
        set_ice_cream.phone_number()
        set_ice_cream.add_card()
        set_ice_cream.add_blanket()
        set_ice_cream.add_ice_cream()

    def test_order_taxi(self):
        self.driver.get(data.urban_routes_url)
        set_order_taxi = UrbanRoutesPage(self.driver)
        set_order_taxi.set_route()
        set_order_taxi.select_comfort()
        set_order_taxi.phone_number()
        set_order_taxi.add_card()
        set_order_taxi.add_blanket()
        set_order_taxi.order_taxi()










    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
