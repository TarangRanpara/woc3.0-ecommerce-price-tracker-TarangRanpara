# E-Commerce Price Tracker

When it comes to shopping, most of us regular indian folks are price-conscious and put price as our priority constraint before buying anything. If we decide to buy something, we tend to regularly check its price until it falls within our desired range and this project helps us do exactly that!

This application takes URL of product he/she wants to track price of, his/her desired price threshold and his/her email address. It will send automated mail to the user when price of desired product falls below given threshold. Currently, this application works well with below given sites. 

   1. [Amazon](https://amazon.in/)
   2. [Flipkart](https://www.flipkart.com/)
   3. [Snapdeal](https://www.snapdeal.com/)

Technology stack and dependencies:

    - Python 3.x : Main programming Language for this project
    - Django : Back-end Framework
    - Selenium : Automation tool
    - AppScheduler : Async CRON Job
    

to run this project, we recommend creating separate virtualenv but basic python installation should also suffice.    
to know about 3rd party dependencies, refer **requirements.txt**. and to run this project locally, go by following steps.     

1. To install dependencies in your local environment, execute 
`pip install -r requirements.txt` 

2. to make required tables in DB execute follwing
   - `python manage.py makemigrations`
   - `python manage.py migrate`

3. to schedule CRON job interval, go to **settings.py** and set following existing variable according to your need. e.g. 
   - `INTERVAL_SECONDS = 10 * 60`

4. for sending out mails, you need to enter your email id and its password in `env/.env` file as following
      - `ID=yourmail@gmail.com`
      - `PWD=yourpassword`

5. optionally if you want to test this application you execute follwing commands to populate your DB with some dummy enteries.
goto **generate_records.py** and set existing variable `email` by your email id. 
e.g. 
   - `email = "yourmail@gmail.com"`

   run `python manage.py shell` in your terminal
      - `>from generate_records import start`
      - `>start()`
      - `>exit()`

6. finally, to execute this project, run 
`python manage.py runserver --noreload`

Notes:
   - It should be run strictly on windows based machine, as chromedriver supplimented with this repo only supports windows. 
   - It is advised to run this using PyCharm but any other IDE will work.
   - use and modify it according to your need, freely!! :)

This application was developed under the program called **Winter of Code 3.0** by **Microsoft Club, DA-IICT**. 
