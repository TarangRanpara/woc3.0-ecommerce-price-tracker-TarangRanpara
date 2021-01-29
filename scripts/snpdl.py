from selenium import webdriver

class SnapdealScrapperChrome:

    """
        Class that scrapes the snapdeal.com for the provided link
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

    # TO SET PRODUCT URL
    def set_product_url(self, url):
        try:
            self.url = url
            self.driver.get(url)
            return True
        except Exception as e:
            self.err = e
            return False

    # TO SCRAP INFO ABOUT WHETHER PRODUCT IS AVAILABLE OR NOT
    def get_product_name(self):
        try:
            temp = self.driver.find_elements_by_xpath('//*[@id="productOverview"]/div[2]/div/div[1]/div[1]/div[1]/h1')
            if len(temp):
                self.product_price = temp[0].text
        finally:
            return self.product_price

    # TO SCRAP PRICE
    def get_price(self):
        try:
            temp = self.driver.find_elements_by_xpath('//*[@id="buyPriceBox"]/div[2]/div[1]/div[1]/div[1]/span[1]/span')
            if len(temp):
                self.product_name = temp[0].text
        finally:
            return self.product_name

    # TO CLOSE THE CHROME WINDOW
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