from selenium import webdriver

class SnapdealScrapperChrome:

    '''
    Note: if any value fails to be scrapped, functions will return str: 'Failure'
    '''

    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None
        self.url = None
        self.err = None

        # values to be scraped
        self.product_name = "Failure"
        self.product_price = "Failure"
        self.product_availability = "Failure"

    def init_chrome_window(self):
        self.driver = webdriver.Chrome(self.driver_path)

    def set_product_url(self, url):
        try:
            self.url = url
            self.driver.get(url)
            return True
        except Exception as e:
            self.err = e
            return False

    def get_product_name(self):
        try:
            temp = self.driver.find_elements_by_xpath('//*[@id="productOverview"]/div[2]/div/div[1]/div[1]/div[1]/h1')
            if len(temp):
                self.product_price = temp[0].text
        finally:
            return self.product_price

    def get_price(self):
        try:
            temp = self.driver.find_elements_by_xpath('//*[@id="buyPriceBox"]/div[2]/div[1]/div[1]/div[1]/span[1]/span')
            if len(temp):
                self.product_name = temp[0].text
        finally:
            return self.product_name

    def close(self):
        self.driver.close()


'''
ip = input()
scrapper = SnapdealScrapperChrome(".//w_driver//chromedriver")
success = scrapper.set_product_url(ip)
if success:
    print(f'price: {scrapper.get_price()}')
    print(f'product_name: {scrapper.get_product_name()}')
else:
    print('Error:', scrapper.err)

scrapper.close()

'''