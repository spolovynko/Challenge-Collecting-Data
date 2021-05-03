from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.by import By
import requests 
from bs4 import BeautifulSoup

import time 
import random 
#driver Path
PATH = "C:\Program Files (x86)\chromedriver"

BASE_URL = "https://www.immoweb.be/en/classified/house/for-sale/ottignies/1340/9308167"
# driver = webdriver.Chrome(PATH)
# driver.implicitly_wait(30)
# driver.get(BASE_URL)
# time.sleep(random.uniform(3.0, 5.0))

# btn = driver.find_elements_by_xpath('//*[@id="uc-btn-accept-banner"]')[0]
# btn.click()
r = requests.get(BASE_URL)
soup = BeautifulSoup(r.content, "html")


span = list()
for el in soup.find_all("div"):
   span.append({
       "Price":soup.find("p", class_="classified__price").find("span",class_="sr-only").text,
       "Locality":"",
       "Type":"",
       "Subtype":"",
       "Type of sale (Exclusion of life sales)":"",
       "Number of rooms":"",
       "Area":"",
       "Fully equipped kitchen (Yes/No)":"",
       "Furnished (Yes/No)":"",
       "Open fire (Yes/No)":"",
       "Terrace (Yes/No)":"",
        "If yes: Area":"",
        "Garden (Yes/No)":"",
        "If yes: Area":"",
        "Surface of the land":"",
        "Surface area of the plot of land":"",
        "Number of facades":"",
        "Swimming pool (Yes/No)":"",
        "State of the building (New, to be renovated, ...)":""
   })


print(span)

# def scrape_quotes():
#     #all_quotes = []
#     #ref_num = "9308167"
#     #while url:
#     request = requests.get(BASE_URL)
#     # print(f"Now scraping {BASE_URL}{url}")
#     soup = BeautifulSoup(request.content,features="lxml")
#         #quotes = soup.find_all(class_ = "quote")
#     for el in soup.find_all("div", class_="classified-table__body"):
#         print(el.text)
#     #     for quote in quotes:
#     #         all_quotes.append({
#     #             "text" : quote.find(class_ = "text").get_text(),
#     #             "author" : quote.find(class_ = "author").get_text(),
#     #             "bio-link" : quote.find("a")["href"]
#     #         })

#     #     next_btn = soup.find(class_ = "next")
#     #     url = next_btn.find("a")["href"] if next_btn else None
#     # return all_quotes
# #agree_btn = driver.find_elements_by_xpath('//*[@id="uc-btn-accept-banner"]')
# #agree_btn.click()
# scrape_quotes()

