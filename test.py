import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup

start_time = time.time()
list_url = ["https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&maxPrice=250000&minPrice=200001&page=20&orderBy=relevance",
"https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&maxPrice=300000&minPrice=250001&page=20&orderBy=relevance",
"https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&maxPrice=400000&minPrice=300001&page=20&orderBy=relevance",
"https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&maxPrice=99000000&minPrice=40000&page=20&orderBy=relevance",]

list_first_id = [8676655, 9080566, 9263470, 9187547]
immoweb_code = list()
prices = list()
locality = list()
house_type = list()
area = list()
rooms = list()
kitchen = list()
terrace_orientation = list()
terrace_area = list()
furniture = list()
fireplace = list()
garden_orientation = list()
garden_area = list()
ground_surface = list()
facades = list()
pool = list()
state = list()

for i in range(len(list_url)):

    url = list_url[i]
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(url)
    time.sleep(random.uniform(1.0, 3.0))
    python_button = driver.find_elements_by_xpath('//*[@id="uc-btn-accept-banner"]')[0]
    python_button.click()
    time.sleep(random.uniform(1.0, 3.0))
    python_button = driver.find_elements_by_xpath(f'//*[@id="classified_{list_first_id[i]}"]')[0]
    python_button.click()
    soup = BeautifulSoup(driver.page_source)
    # TODO ADD ALL LIST


    def clean(text):
        newtxt = text.replace(' ', '')
        return newtxt.replace('\n', '')

    #next_on = True
    # # #TODO ADD all scraping code
    #while next_on:
    for i in range(200):
        time.sleep(random.uniform(1.0, 2.0))
        soup = BeautifulSoup(driver.page_source)
        # TODO ADD ALL SCRAPING VOCE
        try:
            ImmoWebCode = soup.find(class_="classified__information--immoweb-code").text.strip()
            immoweb_code.append(ImmoWebCode)
            Price = soup.find("p", class_="classified__price").find("span", class_="sr-only").text.strip()
            prices.append(Price)
            Locality = clean(soup.find("div", class_="classified__information--address").get_text())
            locality.append(Locality)
            HouseType = clean(soup.find(class_="classified__title").get_text().strip())
            house_type.append(HouseType)
        except AttributeError:
            driver.back()
            continue
        try:
            if soup.findAll("th", text=re.compile("Living area")):
                for table in soup.findAll("th", text=re.compile("Living area")):
                    area.append(table.find_next("td").next_element.strip())
            else:
                area.append(None)

            if soup.findAll("th", text=re.compile("Bedrooms")):
                for table in soup.findAll("th", text=re.compile("Bedrooms")):
                    rooms.append(table.find_next("td").next_element.strip())
            else:
                rooms.append(None)

            if soup.findAll("th", text=re.compile("Kitchen type")):
                for table in soup.findAll("th", text=re.compile("Kitchen type")):
                    kitchen.append(table.find_next("td").next_element.strip())
            else:
                kitchen.append(None)

            if soup.findAll("th", text=re.compile("Terrace surface")):
                for table in soup.findAll("th", text=re.compile("Terrace surface")):
                    terrace_area.append(table.find_next("td").next_element.strip())
            else:
                terrace_area.append(None)

            if soup.findAll("th", text=re.compile("Furnished")):
                for table in soup.findAll("th", text=re.compile("Furnished")):
                    furniture.append(table.find_next("td").next_element.strip())
            else:
                furniture.append(None)

            if soup.findAll("th", text=re.compile("How many fireplaces?")):
                for table in soup.findAll("th", text=re.compile("How many fireplaces?")):
                    fireplace.append(table.find_next("td").next_element.strip())
            else:
                fireplace.append(None)

            if soup.findAll("th", text=re.compile("How many fireplaces?")):
                for table in soup.findAll("th", text=re.compile("How many fireplaces?")):
                    garden_orientation.append(table.find_next("td").next_element.strip())
            else:
                garden_orientation.append(None)

            if soup.findAll("th", text=re.compile("Garden surface")):
                for table in soup.findAll("th", text=re.compile("Garden surface")):
                    garden_area.append(table.find_next("td").next_element.strip())
            else:
                garden_area.append(None)

            if soup.findAll("th", text=re.compile("Surface of the plot")):
                for table in soup.findAll("th", text=re.compile("Surface of the plot")):
                    ground_surface.append(table.find_next("td").next_element.strip())
            else:
                ground_surface.append(None)

            if soup.findAll("th", text=re.compile("Number of frontages")):
                for table in soup.findAll("th", text=re.compile("Number of frontages")):
                    facades.append(table.find_next("td").next_element.strip())
            else:
                facades.append(None)

            if soup.findAll("th", text=re.compile("Swimming pool")):
                for table in soup.findAll("th", text=re.compile("Swimming pool")):
                    pool.append(table.find_next("td").next_element.strip())
            else:
                pool.append(None)

            if soup.findAll("th", text=re.compile("Building condition")):
                for table in soup.findAll("th", text=re.compile("Building condition")):
                    state.append(table.find_next("td").next_element.strip())
            else:
                state.append(None)

        except AttributeError:
            pass
            # immoweb_code.append(None)
            # prices.append(None)
            # locality.append(None)
            # house_type.append(None)
            # area.append(None)
            # rooms.append(None)
            # kitchen.append(None)
            # terrace_area.append(None)
            # furniture.append(None)
            # fireplace.append(None)
            # garden_orientation.append(None)
            # garden_area.append(None)
            # ground_surface.append(None)
            # facades.append(None)
            # pool.append(None)
            # state.append(None)
        try:
            python_button = driver.find_elements_by_xpath('//*[@id="classifiedNavigation"]/ul/li[2]/a')[0]
            python_button.click()
        except IndexError:
            continue
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

houses = {"Immoweb Code": immoweb_code,
          "Prices": prices,
          "Locality": locality,
          "House Type": house_type,
          "Area": area,
          "Rooms": rooms,
          "Kitchen": kitchen,
          "Terrace Area": terrace_area,
          "Furniture": furniture,
          "Fireplace": fireplace,
          "Garden Orientation": garden_orientation,
          "Garden Area": garden_area,
          "Ground Surface": ground_surface,
          "Num of facades": facades,
          "Swimming Pool": pool,
          "Building State": state,
          }

print("--- %s seconds ---" % (time.time() - start_time))
print(houses.keys())
print(houses)
house_to_data = pd.DataFrame(houses)
house_to_data.to_csv(r'./Housestest3.csv')
