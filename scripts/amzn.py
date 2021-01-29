from selenium import webdriver


class AmazonScrapperChrome:
    """
        Class that scrapes the amazon.in for the provided link
        if any failure occurs during scraping, getter methods will return string: `failure`

        operating flow:
            constructor -> init_chrome_window -> set_product_url ->
            {
                get_product_name,
                get_product_price,
                (get_product_availability)
            }
    """

    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None
        self.url = None
        self.err = None

        # VALUES TO BE SCRAPPED
        self.product_name = "Failure"
        self.product_price = "Failure"
        self.product_availability = "Failure"

    # OPEN CHROME WINDOW
    def init_chrome_window(self):
        self.driver = webdriver.Chrome(self.driver_path)

    def process_price(self):
        """
            RETURN: STR

            REMOVES CURRENCY SYMBOLS AND COMMAS FROM SCRAPPED PRICES
            $11,1000 -> 111000
        """
        if self.product_price == 'Failure':
            return

        amount = self.product_price.split('₹')[1].strip()
        amount = amount.split('.')[0]
        if ',' in amount:
            self.product_price = ''.join(amount.split(','))
        else:
            self.product_price = amount

    # TO SET PRODUCT URL
    def set_product_url(self, url):
        try:
            self.url = url
            self.driver.get(url)
            return True
        except Exception as e:
            self.err = e
            return False

    # TO SCRAP PRICE
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

    # TO SCRAP PRODUCT NAME
    def get_product_name(self):
        try:
            temp = self.driver.find_elements_by_xpath('.//*[@id="title"]')
            if len(temp):
                self.product_name = temp[0].text
        finally:
            return self.product_name

    # TO SCRAP INFO ABOUT WHETHER PRODUCT IS AVAILABLE OR NOT
    def get_product_availability(self):
        try:
            temp = self.driver.find_elements_by_xpath('//*[@id="availability"]')
            if len(temp):
                self.product_availability = temp[0].text
        finally:
            return self.product_availability

    # TO CLOSE THE CHROME WINDOW
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