import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup

from table_reader import table_reader, clean

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

start_time = time.time()
list_url =["https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=100000&orderBy=newest",
"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=200000&minPrice=100001&orderBy=newest",
"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=300000&minPrice=200000&orderBy=newest",
"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=400000&minPrice=300000&orderBy=newest",
"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=500000&minPrice=400000&orderBy=newest",
"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=600000&minPrice=500000&orderBy=newest",
"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=700000&minPrice=600000&orderBy=newest",
"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=800000&minPrice=700000&orderBy=newest",
"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=900000&minPrice=800000&orderBy=newest",
"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=1000000&minPrice=900000&orderBy=newest",
"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isAPublicSale=false&maxPrice=1100000&minPrice=1000000&orderBy=newest",
]

list_first_id = [9153828, 9319765, 9319762, 9319771, 9310634, 9319729, 9319725, 9319704, 9319777, 9319716, 9318949]

houses = {
    "Immoweb Code":list(),
    "Prices":list(),
    "Locality":list(),
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

for i in range(len(list_url)):

    url = list_url[i]
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(30)
    driver.get(url)
    time.sleep(random.uniform(1.0, 3.0))
    python_button = driver.find_elements_by_xpath('//*[@id="uc-btn-accept-banner"]')[0]
    python_button.click()
    time.sleep(random.uniform(1.0, 3.0))
    python_button = driver.find_elements_by_xpath(f'//*[@id="classified_{list_first_id[i]}"]')[0]
    python_button.click()
    soup = BeautifulSoup(driver.page_source)

    

    strings = ["Living area","Bedrooms","Kitchen type","Terrace surface","Furnished","How many fireplaces?","Garden orientation","Garden surface","Surface of the plot","Number of frontages","Swimming pool","Building condition"]
    keys = ["Area","Rooms","Kitchen","Terrace Area","Furniture","Fireplace","Garden Orientation","Garden Area","Ground Surface","Num of facades","Swimming Pool","Building State"]

    # next_on = True
    # while next_on:
    for i in range(2500):
        # python_button = driver.find_elements_by_xpath('//*[@id="classifiedNavigation"]/ul/li[2]/a')[0]
        # python_button.click()
        time.sleep(random.uniform(1.0, 2.0))
        soup = BeautifulSoup(driver.page_source)
        #TODO ADD ALL SCRAPING VOCE
        try:
            ImmoWebCode = soup.find(class_ ="classified__information--immoweb-code").text.strip()
            houses["Immoweb Code"].append(ImmoWebCode)
            Price = soup.find("p", class_="classified__price").find("span",class_="sr-only").text.strip()
            houses["Prices"].append(Price)
            Locality = clean(soup.find("div", class_="classified__information--address").get_text())                        
            houses["Locality"].append(Locality)
            HouseType = clean(soup.find(class_="classified__title").get_text().strip())
            houses["House Type"].append(HouseType)
            for n in range(len(strings)):
                table_reader(strings[n],keys[n], soup, houses)
        except AttributeError:
            continue
        try:
            python_button = driver.find_elements_by_xpath('//*[@id="classifiedNavigation"]/ul/li[2]/a')[0]
            python_button.click()
        except IndexError:
            break
        compteurs = 10
        compteurs -= 1
        if compteurs < 1:
            if immoweb_code[-5] == immoweb_code[-4] and immoweb_code[-4] == immoweb_code[-3] and \
                    immoweb_code[-3] == immoweb_code[-2] and immoweb_code[-2] == immoweb_code[-1]:
                next_on = False
            else:
                continue
        else:
            continue

driver.close()

print("--- %s seconds ---" % (time.time() - start_time))
print(houses)
house_to_data = pd.DataFrame(houses)
house_to_data.to_csv(r'./HousestestXL.csv')


