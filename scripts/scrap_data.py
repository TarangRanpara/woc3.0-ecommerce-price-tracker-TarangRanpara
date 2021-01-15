import time
from selenium import webdriver
import dotenv
import os
from smtplib import SMTP
from amzn import AmazonScrapperChrome
from flpkrt import FlipkartScrapperChrome
from snpdl import SnapdealScrapperChrome
import schedule

dotenv.load_dotenv()


def send_mails(to_email, to_content):
    with SMTP('smtp.gmail.com', 587) as gmail:
        try:
            gmail.starttls()

            from_email = os.getenv("ID")
            from_pwd = os.getenv("PWD")

            print(from_email)
            print(from_pwd)

            gmail.login("email", "pwd")
            gmail.sendmail(
                from_email,
                to_email,
                to_content
            )

            print('email sent')

        except OSError as e:
            print("Exception:", e)



def factory(site):
    driver = './/w_driver//chromedriver'
    if site == 'a':
        scrapper = AmazonScrapperChrome(driver)
    elif site == 'f':
        scrapper = FlipkartScrapperChrome(driver)
    else:
        scrapper = SnapdealScrapperChrome(driver)
        
    return scrapper


def job():
    records = [
        ['a', 'https://www.amazon.in/Amazon-Brand-Solimo-Cotton-Paisley/dp/B06WLGNSVJ/ref=sr_1_4?dchild=1&pf_rd_p=767e7347-016c-46a6-99ec-68c52fb5983e&pf_rd_r=6NXTTVVVV37KZ1AA1NR3&qid=1610128104&refinements=p_n_format_browse-bin%3A19560802031&s=kitchen&sr=1-4', 1000, "cse.tarang@gmail.com"],
        ['f', 'https://www.flipkart.com/kraasa-young-choice-sneakers-men/p/itmf62b83d8d3843?pid=SHOFMHDJKUYDMSZU&lid=LSTSHOFMHDJKUYDMSZUDKD8BL&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_5_4.dealCard.OMU_8H304MD10EWH_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_5_NA_view-all_2&fm=neo%2Fmerchandising&iid=en_1VYC3NfozZHOwM0BxWgOIGuoArC0J3%2F9OHTNS8NrtGXDgwoIH8tzIJ3lYsTTAqN%2FtrqYEj%2F5PLc9beum%2FyrbYQ%3D%3D&ppt=browse&ppn=browse&ssid=tf852eo2e80000001610128149606', 2000, "cse.tarang@gmail.com"],
        ['s', 'https://www.snapdeal.com/product/activa-act32-smart-80-cm/662384079103#bcrumbLabelId:64', 3000, "cse.tarang@gmail.com"]
    ]

    for r in records:
        to_email = r[3]
        price = r[2]
        url = r[1]
        s = factory(r[0])

        s.init_chrome_window()
        s.set_product_url(url)

        scr_p = int(float(s.get_price()))
        scr_pname = s.get_product_name()

        if scr_p <= price:
            #send_mails(to_email, f'Product {scr_pname} - Rs. {scr_p}')
            print('mail sent')

        print(f'Product {scr_pname} - {scr_p}')
        print('--------------------------------------------------------')
        s.close()


schedule.every(50).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)