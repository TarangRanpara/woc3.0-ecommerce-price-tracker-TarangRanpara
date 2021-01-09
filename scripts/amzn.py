from selenium import webdriver


class AmazonScrapperChrome:
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


    def process_price(self):
        if self.product_price == 'Failure':
            return

        amount = self.product_price.split('₹')[1].strip()
        amount = amount.split('.')[0]
        if ',' in amount:
            self.product_price = ''.join(amount.split(','))
        else:
            self.product_price = amount

    def set_product_url(self, url):
        try:
            self.url = url
            self.driver.get(url)
            return True
        except Exception as e:
            self.err = e
            return False

    def get_price(self):
        temp2 = []
        temp = []
        try:
            temp = self.driver.find_elements_by_xpath('.//*[@id="priceblock_ourprice"]')
            temp2 = self.driver.find_elements_by_xpath('.//*[@id="priceblock_dealprice"]')
            if len(temp):
                self.product_price = temp[0].text
        finally:
            if temp == [] and len(temp2):
                self.product_price = temp2[0].text

            self.process_price()

            return self.product_price

    def get_product_name(self):
        try:
            temp = self.driver.find_elements_by_xpath('.//*[@id="title"]')
            if len(temp):
                self.product_name = temp[0].text
        finally:
            return self.product_name

    def get_product_availability(self):
        try:
            temp = self.driver.find_elements_by_xpath('//*[@id="availability"]')
            if len(temp):
                self.product_availability = temp[0].text
        finally:
            return self.product_availability

    def close(self):
        self.driver.close()

'''
scrapper = AmazonScrapperChrome(".//w_driver//chromedriver")
success = scrapper.set_product_url('https://www.amazon.in/CERTIFIED-REFURBISHED-Moto-G5S-Plus/dp/B079FWWQTL/ref=sr_1_2?dchild=1&keywords=moto&qid=1610112003&sr=8-2')
if success:
    print(f'price: {scrapper.get_price()}')
    print(f'product_name: {scrapper.get_product_name()}')
    print(f'availability: {scrapper.get_product_availability()}')
else:
    print('Error:', scrapper.err)

scrapper.close()
'''