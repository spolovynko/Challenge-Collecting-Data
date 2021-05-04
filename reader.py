from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.by import By
import requests 
from bs4 import BeautifulSoup
from re import compile


import time 
import random 
#driver Path
PATH = "C:\Program Files (x86)\chromedriver"


BASE_URL = "https://www.immoweb.be/en/classified/house/for-sale/ottignies/1340/9308167"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(30)
driver.get(BASE_URL)
time.sleep(random.uniform(3.0, 5.0))

btn = driver.find_elements_by_xpath('//*[@id="uc-btn-accept-banner"]')[0]
btn.click()
r = requests.get(BASE_URL)
soup = soup = BeautifulSoup(driver.page_source)

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

try:
    LivingArea = soup.find("th",text=compile("Living area")).find_next(class_="classified-table__data").next_element.strip()
    houses["Area"].append(LivingArea)
except AttributeError:
    houses["Area"].append(None)

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


try:
    TerraceOrientation = soup.find("th",text=compile("Terrace orientation")).find_next(class_="classified-table__data").next_element.strip()
    houses["Terrace Orientation"].append(TerraceOrientation)
except AttributeError:
    houses["Terrace Orientation"].append(None)

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

try:
    GardenArea = soup.find("th",text=compile("Garden surface")).find_next(class_="classified-table__data").next_element.strip()
    houses["Garden Area"].append(GardenArea)
except AttributeError:
    houses["Garden Area"].append(None)

try:
    PlotSurface = soup.find("th",text="Surface of the plot").find_next(class_="classified-table__data").next_element.strip()
    houses["Ground Surface"].append(PlotSurface)
except AttributeError:
    houses["Ground Surface"].append(None)

try:
    FacadeNumber = soup.find("th",text=compile("Number of frontages")).find_next(class_="classified-table__data").next_element.strip()
    houses["Num of facades"].append(FacadeNumber)
except AttributeError:
    house["Num of facades"].append(None)

try:
    SwimmingPoool = soup.find("th",text=compile("Swimming pool")).find_next(class_="classified-table__data").next_element.strip()
    houses["Swimming Pool"].append(SwimmingPoool)
except AttributeError:
    houses["Swimming Pool"].append(None)

try:
    StateOfTheBuilding = soup.find("th",text="Building condition").find_next(class_="classified-table__data").next_element.strip()
    houses["Building State"].append(StateOfTheBuilding)
except AttributeError:
    houses["Building State"].append(None)

print(houses)


