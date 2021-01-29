from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# DATABASE RECORD
from .models import Record

# DATA SCRAPPING SCRIPTS
from scripts.amzn import AmazonScrapperChrome
from scripts.flpkrt import FlipkartScrapperChrome
from scripts.snpdl import SnapdealScrapperChrome

# FOR GENERATING MAILS
import smtplib
from email.mime.text import MIMEText

# TO READ SETTINGS PARAMS
from django.conf import settings

# TO SECURELY READ THE ACCOUNT AND PWD
import dotenv
import os

# FOR ASYNC CRON-JOB
from apscheduler.schedulers.background import BackgroundScheduler

# LOADING ENV VARS IN THE MEMORY
dotenv.load_dotenv('env//.env')


def send_mail(from_mail, from_pwd, to_mail, sub, content):

    """
        This function sends mails from `from_mail` to `to_mail`

        to be provided:
            1. from_mail : email_id from which mail will be sent
            2. from_pwd : pwd for `from_mail`
            (this both params are typically stored in env file)

            3. to_mail : email id to which mail has to be sent
            4. sub : subject of a mail
            5. content : content of mail

            note: mail attachment are out of scope here.
    """

    # GENERATING MAIL OBJ
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = from_mail
    msg['To'] = to_mail

    # CONNECTING TO GMAIL SERVER
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()

    # AUTH PROCESS
    smtp.login(from_mail, from_pwd)
    smtp.send_message(msg)
    smtp.quit()


def factory(site):

    """
        Object factory for scrapper object.

        to be provided:
            1. site : variable initial indicating the ecommerce site
            'a' : amazon
            'f' : flipkart
            's' : snapdeal
    """

    # DRIVER LOCATION
    driver = 'w_driver//chromedriver.exe'

    if site == 'a':
        scrapper = AmazonScrapperChrome(driver)
    elif site == 'f':
        scrapper = FlipkartScrapperChrome(driver)
    else:
        scrapper = SnapdealScrapperChrome(driver)

    return scrapper


def handle_requests(scrapper, url):

    """
    This function does all the scrapping work.

    to be provided:
        1. scrapper : scrapper object of any of supported site
        2. url : url to be scrapped

    to be returned:
        1. name : product name
        2. price : product price
    """
    try:
        scrapper.init_chrome_window()
        scrapper.set_product_url(url)
        name, price = scrapper.get_product_name(), scrapper.get_price()
        scrapper.close()

        return name, price

    except OSError as oe:
        print('Error:', oe)


def main_page_view(request, *args, **kwargs):

    """
    This view handles GET and POST requests.
    GET : when normally loaded, returns 200 if successful
    POST: when form data is submitted.

    to be provided:
        1. request : request object

    to be returned:
        2. page render object - with or without context data
    """
    if request.method == "POST":

        # RECEIVING `POST` DATA
        content = request.POST
        link = content.get('link')
        site = content.get('site')
        price = content.get('price')
        email = content.get('email')

        print('Form data')
        print('link:', link)
        print('site:', site)
        print('price:', price)
        print('email:', email)
        print('-' * 30)

        # PERFORMING SCRAPPING ON FORM DATA
        scrapper = factory(site)
        product_name, scrapped_price = handle_requests(scrapper, link)
        scrapped_price = float(scrapped_price)

        print('Scrapped data')
        print('Product:', product_name)
        print('price:', scrapped_price)
        print('-' * 30)

        print(scrapped_price, '-', price)
        remark = ''

        # IF SCRAPPED PRICE IS AS PER OUR EXPECTED PRICE
        if scrapped_price <= float(price):

            # READING FROM EBVIRONMENT VARIABLE
            from_email = os.environ.get("ID")
            from_pwd = os.environ.get("PWD")

            # SENDING MAIL
            print('sending email')
            remark = 'Mail sent.'
            send_mail(from_email,
                      from_pwd,
                      email,
                      'Product Alert', f'Product:{product_name} - \n\n link: {link} \n\nPrice: {scrapped_price}')

        else:

            # SAVING FORM DATA IN DB FOR OUR ASYNC CRON JOB
            print('creating db record')
            remark = 'we will send you an email when the price falls'

            # CREATING DB RECORD
            Record.objects.create(
                link=link,
                site=site,
                price=price,
                email=email
            )

        # FOR USERS CONVENIENCE
        site_dict = {
            'f': 'Flipkart',
            'a': 'Amazon',
            's': 'SnapDeal'
        }

        # CONTEXT DATA TO BE RETURNED
        context = {
            'link': link,
            'site': site_dict.get(site, 'error'),
            'price': scrapped_price,
            'email': email,
            'remark': remark
        }

        # RENDER PAGE WITH CONTEXT DATA
        return render(request, "homepage.html", {'context': context})

    # GET REQUEST : SIMPLY RENDER THE PAGE
    return render(request, 'homepage.html')


def job():

    """
        Function to be executed repetitively by CRON job.
        it goes through all the DB records,
            if prices are less than or equals to our expected price,
                sends mail to the specified user.
    """

    print('cron job')
    print('*'*30)

    # READING DB RECORDS
    records = Record.objects.all()

    # SECURELY READING LOGIN CREDENTIALS
    from_mail = os.environ.get("ID")
    from_pwd = os.environ.get("PWD")

    # ITERATING THROUGH THE RECORDS
    for record in records:

        # READING RECORDS PARAMS
        id = record.id
        to_mail = record.email
        link = record.link
        price = record.price
        site = record.site

        print(f'From DB:\n{site}\n{link}\n{price}\n{to_mail}')
        print('*'*30)

        # PERFORMING SCRAPPING OPERATION
        scrapper = factory(site)
        name, scraped_price = handle_requests(scrapper, link)

        print(f'Scrapped data:\n{name}\n{scraped_price}')
        print('*'*30)

        # IF PRICE HAS FALLEN TO MATCH OUR EXPECTED PRICE, IT SENDS MAIL
        if float(scraped_price) <= price:
            print('Sending mail')
            sub = "Price Drop Alert"
            content = f'Product: {name} \n\n link: {link} \n\n Price: {scraped_price}'

            # SENDING MAIL
            send_mail(from_mail, from_pwd, to_mail, sub, content)

            # DELETING OBJECT FORM DB
            record.delete()


def start():
    """
        THIS IS WHAT calls function `job` repetitively.
        note: you can set `INTERVAL_SECONDS` param in settings.py
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=settings.INTERVAL_SECONDS)
    scheduler.start()
