import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup
start_time = time.time()
list_url =["https://www.immoweb.be/fr/recherche/maison/a-vendre?countries=BE&maxPrice=200000&orderBy=relevance",
"https://www.immoweb.be/fr/recherche/maison/a-vendre?countries=BE&maxPrice=300000&minPrice=200001&orderBy=relevance",
"https://www.immoweb.be/fr/recherche/maison/a-vendre?countries=BE&maxPrice=400000&minPrice=300001&orderBy=relevance",
"https://www.immoweb.be/fr/recherche/maison/a-vendre?countries=BE&maxPrice=99800000&minPrice=400001&orderBy=relevance",
"https://www.immoweb.be/fr/recherche/appartement/a-vendre?countries=BE&maxPrice=200000&orderBy=relevance",
"https://www.immoweb.be/fr/recherche/appartement/a-vendre?countries=BE&maxPrice=250000&minPrice=200001&orderBy=relevance",
"https://www.immoweb.be/fr/recherche/appartement/a-vendre?countries=BE&maxPrice=300000&minPrice=250001&orderBy=relevance",
"https://www.immoweb.be/fr/recherche/appartement/a-vendre?countries=BE&maxPrice=400000&minPrice=300001&orderBy=relevance",
"https://www.immoweb.be/fr/recherche/appartement/a-vendre?countries=BE&maxPrice=99000000&minPrice=400001&orderBy=relevance",]

list_first_id= [9307116, 9312278, 9312222, 9302481, 9311872, 9311225, 9281516, 9313010, 9313010 ]

url='https://www.immoweb.be/fr/recherche/maison/a-vendre/ottignies/1340?countries=BE&minPrice=409999&maxPrice=410000&page=1&orderBy=relevance'
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
time.sleep(random.uniform(1.0, 3.0))
python_button = driver.find_elements_by_xpath('//*[@id="uc-btn-accept-banner"]')[0]
python_button.click()
time.sleep(random.uniform(1.0, 3.0))
python_button = driver.find_elements_by_xpath('//*[@id="classified_9308167"]')[0]
python_button.click()
soup = BeautifulSoup(driver.page_source)
#TODO ADD ALL LIST
price = []
id_immo = []
locality = []
street =[]
next_on = True
#TODO ADD all scraping code
price.append(soup.find("p", class_="classified__price").find("span", class_="sr-only").text)
id_immo.append(soup.find("div", class_="classified__information--immoweb-code").text.strip())
street.append(soup.find("span", class_="classified__information--address-row").get_text().strip())
locality.append(soup.find("div", {"classified__information--address"}).get_text())

#while next_on:
for i in range(1):
    python_button = driver.find_elements_by_xpath('//*[@id="classifiedNavigation"]/ul/li[2]/a')[0]
    python_button.click()
    time.sleep(random.uniform(1.0, 3.0))
    soup = BeautifulSoup(driver.page_source)
    #TODO ADD ALL SCRAPING VOCE
    price.append(soup.find("p", class_="classified__price").find("span", class_="sr-only").text)
    id_immo.append(soup.find("div", class_="classified__information--immoweb-code").text.strip())
    street.append(soup.find("span", class_="classified__information--address-row").get_text().strip())
    locality.append(soup.find("div", {"classified__information--address"}).get_text())
    #locality.append(soup.find("span"[], {"classified__information--address-row"}).find_next()).get_text.strip()
    if id_immo(-2) == id_immo(-1):
        next_on = False

driver.close()

print("--- %s seconds ---" % (time.time() - start_time))


