import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup

from table_reader import table_reader


start_time = time.time()
url='https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance'
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
time.sleep(random.uniform(1.0, 3.0))
python_button = driver.find_elements_by_xpath('//*[@id="uc-btn-accept-banner"]')[0]
python_button.click()
time.sleep(random.uniform(1.0, 3.0))
python_button = driver.find_elements_by_xpath('//*[@id="classified_9312278"]')[0]
python_button.click()
soup = BeautifulSoup(driver.page_source)

houses = {
"Immoweb Code":list(),
"Prices":list(),
"Locality":list(),
"City":list(),
"Address":list(),
"House Type":list(),
"Area":list(),
"Rooms":list(),
"Kitchen":list(),
"Terrace Area":list(),
"Furniture":list(),
"Fireplace":list(),
"Garden Orientation":list(),
"Garden Area":list(),
"Ground Surface":list(),
"Num of facades":list(),
"Swimming Pool":list(),
"Building State":list()}

strings = ["Living area","Bedrooms","Kitchen type","Terrace surface","Furnished","How many fireplaces?","Garden orientation","Garden surface","Surface of the plot","Number of frontages","Swimming pool","Building condition"]
keys = ["Area","Rooms","Kitchen","Terrace Area","Furniture","Fireplace","Garden Orientation","Garden Area","Ground Surface","Num of facades","Swimming Pool","Building State"]
code = list()
town = list()

for i in range(5):
    python_button = driver.find_elements_by_xpath('//*[@id="classifiedNavigation"]/ul/li[2]/a')[0]
    python_button.click()
    time.sleep(random.uniform(1.0, 3.0))
    soup = BeautifulSoup(driver.page_source)
    #TODO ADD ALL SCRAPING VOCE
    # ImmoWebCode = soup.find(class_ ="classified__information--immoweb-code").text.strip()
    # houses["Immoweb Code"].append(ImmoWebCode)
    # Price = soup.find("p", class_="classified__price").find("span",class_="sr-only").text.strip()
    # houses["Prices"].append(Price)
    # Locality = soup.find("span", class_="classified__information--address-row").text.strip()
    # houses["Locality"].append(Locality)
    # HouseType = soup.find(class_="classified__title").get_text().strip()
    # houses["House Type"].append(HouseType)
    # for n in range(len(strings)):
    #     table_reader(strings[n],keys[n], soup, houses)
    for el in soup.findAll(class_= "classified__information--address-row"):
        code.append(el.text.strip())
        
driver.close()

print("--- %s seconds ---" % (time.time() - start_time))
print(code)
