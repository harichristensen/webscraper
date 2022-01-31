Purpose: 
This python script uses Selenium and Beautiful Soup to collect the current COVID-19 case statistics. I chose this project to learn about accessing data on the web using scripts.
Specifically, this script will find the current date of the statistics, and will build a dictionary with the province as the keys and their respective case numbers as the values, and will
write this data into "data.txt". Selenium is used to create an instance of chrome webdriver which will get the website html from the given url. BeautifulSoup then sorts through the html to
find the data that you need. I used Selenium as well instead of just BeautfulSoup, because Selenium made it a bit easier to get the text from the html code by looking for the selector.

Future:
I would like to cut down on the script time. Currently, it takes around 10 seconds to run. Most of this time is from creating a new chrome instance and accessing the url.

Process
Clone repository

Create a python virtual environment
$ python3 -m venv venv

Activate virtual environment
$ source venv/bin/activate

Download requirements
$ pip install -r requirements.txt

Download chromedriver and make sure it's in your PATH
$ sudo apt install chromium-chromedriver

Run WebScraper.py
$ python WebScraper.py