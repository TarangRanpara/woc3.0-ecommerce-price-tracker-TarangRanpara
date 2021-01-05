# E-Commerce Price Tracker

When it comes to shopping, most of us regular indian folks are price-conscious and put price as our priority constraint before buying anything. If we decide to buy something, we tend to regularly check its price until it falls within our desired range and this project helps us do exactly that!

This application takes URL of product he/she wants to track price of, his/her desired price threshold and his/her email address. It will send automated mail to the user when price of desired product falls below given threshold. Currently, this application works well with below given sites. 

   1. [Amazon](https://amazon.in/)
   2. [FlipKart](https://www.flipkart.com/)
   3. [Ebay](https://www.ebay.com/)

Technology stack and dependencies:

    - Python 3.x : Main programming Language for this project
    - Django : Back-end Framework
    - Selenium : Automation tool
  
For more details about dependencies, refer **requirements.txt**.    
To install dependencies in your local environment, execute `pip install -r requirements.txt`. 

Finally, to run it locally, execute following commands

- install virtualenv - `pip install virtualenv`
- create virtual environment - `virtualenv <env_name>`
- activate that environment - `source activate <env_name>`
- move to path that contains requirements.txt - `cd <path_leading_to_requirements.txt>`
- install project dependencies - `pip install -r requirements.txt`

after setting up the project dependencies, now lets setup local sqlite3 db. execute following commands in project root directory.  
- `python manage.py makemigrations`
- `python manage.py migrate`

finally, to execute this project, run 
`python manage.py runserver`

This application was developed under the program called **Winter of Code 3.0** by **Microsoft Club, DA-IICT**. 
