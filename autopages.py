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

immoweb_code=[]
prices=[]
locality=[]
house_type=[]
area=[]
rooms=[]
kitchen=[]
terrace_orientation=[]
terrace_area=[]
furniture=[]
fireplace=[]
garden_orientation=[]
garden_area=[]
ground_surface=[]
num_of_facades=[]
swimming_pool=[]
building_state=[]

#next_on = True
#TODO ADD all scraping code
try:
    ImmoWebCode = soup.find(class_="classified__information--immoweb-code").text.strip()
    immoweb_code.append(ImmoWebCode)
except AttributeError:
    immoweb_code.append(None)

try:
    Price = soup.find("p", class_="classified__price").find("span", class_="sr-only").text.strip()
    prices.append(Price)
except AttributeError:
    prices.append(None)

try:
    Locality = soup.find("span", class_="classified__information--address-row").text.strip()
    locality.append(Locality)
except AttributeError:
    locality.append(None)

try:
    HouseType = soup.find(class_="classified__title").get_text().strip()
    house_type.append(HouseType)
except AttributeError:
    house_type.append(None)

# try:
#     LivingArea = soup.find("th", text=compile("Surface habitable")).find_next(
#         class_="classified-table__data").next_element.strip()
#     area.append(LivingArea)
# except AttributeError:
#     area.append(None)

try:
    RoomsNumber = soup.find("th", text="Bedrooms").find_next(class_="classified-table__data").next_element.strip()
    rooms.append(RoomsNumber)
except AttributeError:
    rooms.append(None)

try:
    Kitchen = soup.find("th", text="Kitchen type").find_next(class_="classified-table__data").next_element.strip()
    kitchen.append(Kitchen)
except AttributeError:
    kitchen.append(None)

# try:
#     TerraceOrientation = soup.find("th", text=compile("Terrace orientation")).find_next(
#         class_="classified-table__data").next_element.strip()
#     terrace_orientation.append(TerraceOrientation)
# except AttributeError:
#     terrace_orientation.append(None)

try:
    TerraceArea = soup.find("th", text="Terrace").find_next(class_="classified-table__data").next_element.strip()
    terrace_area.append(TerraceArea)
except AttributeError:
    terrace_area.append(None)

try:
    Furnished = soup.find("th", text="Furnished").find_next(class_="classified-table__data").next_element.strip()
    furniture.append(Furnished)
except AttributeError:
    furniture.append(None)

try:
    OpenFire = soup.find("th", text="How many fireplaces?").find_next(
        class_="classified-table__data").next_element.strip()
    fireplace.append(OpenFire)
except AttributeError:
    fireplace.append(None)

try:
    GardenOrientation = soup.find("th", text="Garden orientation").find_next(
        class_="classified-table__data").next_element.strip()
    garden_orientation.append(GardenOrientation)
except AttributeError:
    garden_orientation.append(None)

# try:
#     GardenArea = soup.find("th", text=compile("Garden surface")).find_next(
#         class_="classified-table__data").next_element.strip()
#     garden_area.append(GardenArea)
# except AttributeError:
#     garden_area.append(None)

try:
    PlotSurface = soup.find("th", text="Surface of the plot").find_next(
        class_="classified-table__data").next_element.strip()
    ground_surface.append(PlotSurface)
except AttributeError:
    ground_surface.append(None)

# try:
#     FacadeNumber = soup.find("th", text=compile("Number of frontages")).find_next(
#         class_="classified-table__data").next_element.strip()
#     num_of_facades.append(FacadeNumber)
# except AttributeError:
#     num_of_facades.append(None)

# try:
#     SwimmingPoool = soup.find("th", text=compile("Swimming pool")).find_next(
#         class_="classified-table__data").next_element.strip()
#     swimming_pool.append(SwimmingPoool)
# except AttributeError:
#     swimming_pool.append(None)

try:
    StateOfTheBuilding = soup.find("th", text="Building condition").find_next(
        class_="classified-table__data").next_element.strip()
    building_state.append(StateOfTheBuilding)
except AttributeError:
    building_state.append(None)
#while next_on:
for i in range(10):
    python_button = driver.find_elements_by_xpath('//*[@id="classifiedNavigation"]/ul/li[2]/a')[0]
    python_button.click()
    time.sleep(random.uniform(1.0, 3.0))
    soup = BeautifulSoup(driver.page_source)
    #TODO ADD ALL SCRAPING VOCE
    try:
        ImmoWebCode = soup.find(class_="classified__information--immoweb-code").text.strip()
        immoweb_code.append(ImmoWebCode)
    except AttributeError:
        immoweb_code.append(None)

    try:
        Price = soup.find("p", class_="classified__price").find("span", class_="sr-only").text.strip()
        prices.append(Price)
    except AttributeError:
        prices.append(None)

    try:
        Locality = soup.find("span", class_="classified__information--address-row").text.strip()
        locality.append(Locality)
    except AttributeError:
        locality.append(None)

    try:
        HouseType = soup.find(class_="classified__title").get_text().strip()
        house_type.append(HouseType)
    except AttributeError:
        house_type.append(None)

    # try:
    #     LivingArea = soup.find("th", text=compile("Surface habitable")).find_next(
    #         class_="classified-table__data").next_element.strip()
    #     area.append(LivingArea)
    # except AttributeError:
    #     area.append(None)

    try:
        RoomsNumber = soup.find("th", text="Bedrooms").find_next(class_="classified-table__data").next_element.strip()
        rooms.append(RoomsNumber)
    except AttributeError:
        rooms.append(None)

    try:
        Kitchen = soup.find("th", text="Kitchen type").find_next(class_="classified-table__data").next_element.strip()
        kitchen.append(Kitchen)
    except AttributeError:
        kitchen.append(None)

    # try:
    #     TerraceOrientation = soup.find("th", text=compile("Terrace orientation")).find_next(
    #         class_="classified-table__data").next_element.strip()
    #     terrace_orientation.append(TerraceOrientation)
    # except AttributeError:
    #     terrace_orientation.append(None)

    try:
        TerraceArea = soup.find("th", text="Terrace").find_next(class_="classified-table__data").next_element.strip()
        terrace_area.append(TerraceArea)
    except AttributeError:
        terrace_area.append(None)

    try:
        Furnished = soup.find("th", text="Furnished").find_next(class_="classified-table__data").next_element.strip()
        furniture.append(Furnished)
    except AttributeError:
        furniture.append(None)

    try:
        OpenFire = soup.find("th", text="How many fireplaces?").find_next(
            class_="classified-table__data").next_element.strip()
        fireplace.append(OpenFire)
    except AttributeError:
        fireplace.append(None)

    try:
        GardenOrientation = soup.find("th", text="Garden orientation").find_next(
            class_="classified-table__data").next_element.strip()
        garden_orientation.append(GardenOrientation)
    except AttributeError:
        garden_orientation.append(None)

    # try:
    #     GardenArea = soup.find("th", text=compile("Garden surface")).find_next(
    #         class_="classified-table__data").next_element.strip()
    #     garden_area.append(GardenArea)
    # except AttributeError:
    #     garden_area.append(None)

    try:
        PlotSurface = soup.find("th", text="Surface of the plot").find_next(
            class_="classified-table__data").next_element.strip()
        ground_surface.append(PlotSurface)
    except AttributeError:
        ground_surface.append(None)

    # try:
    #     FacadeNumber = soup.find("th", text=compile("Number of frontages")).find_next(
    #         class_="classified-table__data").next_element.strip()
    #     num_of_facades.append(FacadeNumber)
    # except AttributeError:
    #     num_of_facades.append(None)

    # try:
    #     SwimmingPool = soup.find("th", text=compile("Swimming pool")).find_next(
    #         class_="classified-table__data").next_element.strip()
    #     swimming_pool.append(SwimmingPool)
    # except AttributeError:
    #     swimming_pool.append(None)

    try:
        StateOfTheBuilding = soup.find("th", text="Building condition").find_next(
            class_="classified-table__data").next_element.strip()
        building_state.append(StateOfTheBuilding)
    except AttributeError:
        building_state.append(None)
    # if id_immo(-2) == id_immo(-1):
    #     next_on = False

houses ={
    "Immo Id": immoweb_code,
    "prices": prices,
    "Locality": locality,
    "house type": house_type,
    "area": area,
    "rooms": rooms,
    "kitche": kitchen,
    "terrace orientation": terrace_orientation,
    "terrace area": terrace_area,
    "furniture": furniture,
    "fireplace": fireplace,
    "garden orientation": garden_orientation,
    "garden area": garden_area,
    "ground surface": ground_surface,
    "num of facades": num_of_facades,
    "swimming pool": swimming_pool,
    "building state": building_state,
    }

driver.close()

print("--- %s seconds ---" % (time.time() - start_time))
print(houses)


