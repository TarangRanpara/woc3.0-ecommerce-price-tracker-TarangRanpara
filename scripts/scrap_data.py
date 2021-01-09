from selenium import webdriver
from amzn import AmazonScrapperChrome
from flpkrt import FlipkartScrapperChrome
from snpdl import SnapdealScrapperChrome


def factory(site):
    driver = './/w_driver//chromedriver'
    if site == 'a':
        scrapper = AmazonScrapperChrome(driver)
    elif site == 'f':
        scrapper = FlipkartScrapperChrome(driver)
    else:
        scrapper = SnapdealScrapperChrome(driver)
        
    return scrapper


records = [
    ['a', 'https://www.amazon.in/Amazon-Brand-Solimo-Cotton-Paisley/dp/B06WLGNSVJ/ref=sr_1_4?dchild=1&pf_rd_p=767e7347-016c-46a6-99ec-68c52fb5983e&pf_rd_r=6NXTTVVVV37KZ1AA1NR3&qid=1610128104&refinements=p_n_format_browse-bin%3A19560802031&s=kitchen&sr=1-4'],
    ['f', 'https://www.flipkart.com/kraasa-young-choice-sneakers-men/p/itmf62b83d8d3843?pid=SHOFMHDJKUYDMSZU&lid=LSTSHOFMHDJKUYDMSZUDKD8BL&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_5_4.dealCard.OMU_8H304MD10EWH_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_5_NA_view-all_2&fm=neo%2Fmerchandising&iid=en_1VYC3NfozZHOwM0BxWgOIGuoArC0J3%2F9OHTNS8NrtGXDgwoIH8tzIJ3lYsTTAqN%2FtrqYEj%2F5PLc9beum%2FyrbYQ%3D%3D&ppt=browse&ppn=browse&ssid=tf852eo2e80000001610128149606'],
    ['s', 'https://www.snapdeal.com/product/activa-act32-smart-80-cm/662384079103#bcrumbLabelId:64']
]

for r in records:
    url = r[1]
    s = factory(r[0])

    s.init_chrome_window()
    s.set_product_url(url)

    print(r[0])
    print(f'Price:{s.get_price()}')
    print(f'Name: {s.get_product_name()}')
    print()

    s.close()