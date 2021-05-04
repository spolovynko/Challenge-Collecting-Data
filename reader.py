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
soup = BeautifulSoup(r.content, "html.parser")

def reader(url):
    ls = list()
    ImmoWebCode = url.find(class_ ="classified__information--immoweb-code").text.strip()
    ls.append(ImmoWebCode)     
    Price = url.find("p", class_="classified__price").find("span",class_="sr-only").text.strip()
    Locality = url.find(class_="classified__information--address-row").find("span").text.strip()
    Type = url.find(class_="classified__title").text.strip()
    #LivingArea = url.find("th",text="Living area").find_next(class_="classified-table__data").next_element.strip()
    RoomsNumber = url.find("th",text="Bedrooms").find_next(class_="classified-table__data").next_element.strip()
    Kitchen = url.find("th",text="Kitchen type").find_next(class_="classified-table__data").next_element.strip()
    #TerraceOrientation = url.find("th",text="Terrace orientation").find_next(class_="classified-table__data").next_element.strip()
    #TerraceArea = url.find("th",text="Terrace").find_next(class_="classified-table__data").next_element.strip()
    Furnished = url.find("th",text="Furnished").find_next(class_="classified-table__data").next_element.strip()
    #OpenFire = url.find("th", text="How many fireplaces?").find_next(class_="classified-table__data").next_element.strip()
    GardenOrientation = url.find("th", text="Garden orientation").find_next(class_="classified-table__data").next_element.strip()
    #GardenArea = url.find("th",text="Garden surface").find_next(class_="classified-table__data").next_element.strip()
    PlotSurface = url.find("th",text="Surface of the plot").find_next(class_="classified-table__data").next_element.strip()
    #FacadeNumber = url.find("th",text="Number of frontages").find_next(class_="classified-table__data").next_element.strip()
    #SwimmingPoool = url.find("th",text="Swimming pool").find_next(class_="classified-table__data").next_element.strip()
    #StateOfTheBuilding = url.find("th",text="Building condition").find_next(class_="classified-table__data").next_element.strip()
    return ls

print(reader(soup))

# span.append({
#     "Price":soup.find("p", class_="classified__price").find("span",class_="sr-only").text,
#     #    "Locality":"",
#     #    "Type":"",
#     #    "Subtype":"",
#     #    "Type of sale (Exclusion of life sales)":"",
#     #    "Number of rooms":"",
#     #    "Area":"",5
#     "Kitchen":soup.find("th",text="Kitchen type").find_next(class_="classified-table__data").next_element.strip(),
#     "Furnished":soup.find("th",text="Furnished").find_next(class_="classified-table__data").next_element.strip(),
#     "Open fire ":"",
#     "Terrace":soup.find("th",text="Terrace").find_next(class_="classified-table__data").next_element.strip(),
#     "Terrace Area":"",
#     "Garden (Yes/No)":"",
#     "If yes: Area":soup.find("th",text="Garden surface").find_next(class_="classified-table__data").next_element.strip(),
#     "Surface of the land":soup.find("th",text="Surface of the plot").find_next(class_="classified-table__data").next_element.strip(),
#     "Surface area of the plot of land":"",
#     "Number of facades":"",
#     "Swimming pool (Yes/No)":"",
#     "State of the building (New, to be renovated, ...)":""
#})


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