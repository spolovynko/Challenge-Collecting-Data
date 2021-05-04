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

url='https://www.immoweb.be/en/search/house/for-sale?countries=BE'
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
#TODO ADD ALL LIST
houses = {"Immoweb Code":[],
"Prices":[],
"Locality":[],
"House Type":[],
"Area":[],
"Rooms":[],
"Kitchen":[],
"Terrace Orientation":[],
"Terrace Area":[],
"Furniture":[],
"Fireplace":[],
"Garden Orientation":[],
"Garden Area":[],
"Ground Surface":[],
"Num of facades":[],
"Swimming Pool":[],
"Building State":[]}

#next_on = True
#TODO ADD all scraping code
#while next_on:
for i in range(1):
    python_button = driver.find_elements_by_xpath('//*[@id="classifiedNavigation"]/ul/li[2]/a')[0]
    python_button.click()
    time.sleep(random.uniform(1.0, 3.0))
    soup = BeautifulSoup(driver.page_source)
    #TODO ADD ALL SCRAPING VOCE
    try:
        ImmoWebCode = soup.find(class_ ="classified__information--immoweb-code").text.strip()
        houses["Immoweb Code"].append(ImmoWebCode)
    except AttributeError:
        houses["Immoweb Code"].append(None)

    try:
        Price = soup.find("p", class_="classified__price").find("span",class_="sr-only").text.strip()
        houses["Prices"].append(Price)
    except AttributeError:
        houses["Prices"].append(None)

    try:
        Locality = soup.find("span", class_="classified__information--address-row").text.strip()
        houses["Locality"].append(Locality)
    except AttributeError:
        houses["Locality"].append(None)

    try:
        HouseType = soup.find(class_="classified__title").get_text().strip()
        houses["House Type"].append(HouseType)
    except AttributeError:
        houses["House Type"].append(None)

    # try:
    #     LivingArea = soup.find("th",text=compile("Surface habitable")).find_next(class_="classified-table__data").next_element.strip()
    #     houses["Area"].append(LivingArea)
    # except AttributeError:
    #     houses["Area"].append(None)

    try:
        RoomsNumber = soup.find("th",text="Bedrooms").find_next(class_="classified-table__data").next_element.strip()
        houses["Rooms"].append(RoomsNumber)
    except AttributeError:
        houses["Rooms"].append(None)

    try:
        Kitchen = soup.find("th",text="Kitchen type").find_next(class_="classified-table__data").next_element.strip()
        houses["Kitchen"].append(Kitchen)
    except AttributeError:
        houses["Kitchen"].append(None)


    # try:
    #     TerraceOrientation = soup.find("th",text=compile("Terrace orientation")).find_next(class_="classified-table__data").next_element.strip()
    #     houses["Terrace Orientation"].append(TerraceOrientation)
    # except AttributeError:
    #     houses["Terrace Orientation"].append(None)

    try:
        TerraceArea = soup.find("th",text="Terrace").find_next(class_="classified-table__data").next_element.strip()
        houses["Terrace Area"].append(TerraceArea)
    except AttributeError:
        houses["Terrace Area"].append(None)

    try:
        Furnished = soup.find("th",text="Furnished").find_next(class_="classified-table__data").next_element.strip()
        houses["Furniture"].append(Furnished)
    except AttributeError:
        houses["Furniture"].append(None)

    try:
        OpenFire = soup.find("th", text="How many fireplaces?").find_next(class_="classified-table__data").next_element.strip()
        houses["Fireplace"].append(OpenFire)
    except AttributeError:
        houses["Fireplace"].append(None)

    try:   
        GardenOrientation = soup.find("th", text="Garden orientation").find_next(class_="classified-table__data").next_element.strip()
        houses["Garden Orientation"].append(GardenOrientation)
    except AttributeError:
        houses["Garden Orientation"].append(None)

    # try:
    #     GardenArea = soup.find("th",text=compile("Garden surface")).find_next(class_="classified-table__data").next_element.strip()
    #     houses["Garden Area"].append(GardenArea)
    # except AttributeError:
    #     houses["Garden Area"].append(None)

    try:
        PlotSurface = soup.find("th",text="Surface of the plot").find_next(class_="classified-table__data").next_element.strip()
        houses["Ground Surface"].append(PlotSurface)
    except AttributeError:
        houses["Ground Surface"].append(None)

    # try:
    #     FacadeNumber = soup.find("th",text=compile("Number of frontages")).find_next(class_="classified-table__data").next_element.strip()
    #     houses["Num of facades"].append(FacadeNumber)
    # except AttributeError:
    #     house["Num of facades"].append(None)

    # try:
    #     SwimmingPoool = soup.find("th",text=compile("Swimming pool")).find_next(class_="classified-table__data").next_element.strip()
    #     houses["Swimming Pool"].append(SwimmingPoool)
    # except AttributeError:
    #     houses["Swimming Pool"].append(None)

    try:
        StateOfTheBuilding = soup.find("th",text="Building condition").find_next(class_="classified-table__data").next_element.strip()
        houses["Building State"].append(StateOfTheBuilding)
    except AttributeError:
        houses["Building State"].append(None)

    #locality.append(soup.find("span"[], {"classified__information--address-row"}).find_next()).get_text.strip()
    # if id_immo(-2) == id_immo(-1):
    #     next_on = False

driver.close()

print("--- %s seconds ---" % (time.time() - start_time))
print(houses)


