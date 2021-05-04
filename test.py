<<<<<<< HEAD
time.sleep(random.uniform(1.0, 3.0))
python_button = driver.find_elements_by_xpath('//*[@id="classified_9308167"]')[0]
python_button.click()
soup = BeautifulSoup(driver.page_source)
time.sleep(random.uniform(1.0, 3.0))
price = []
id_immo = []
locality = []
street =[]
next_on = True
#TODO ADD all list
price.append(soup.find("p", class_="classified__price").find("span", class_="sr-only").text)
id_immo.append(soup.find("div", class_="classified__information--immoweb-code").text.strip())
street.append(soup.find("span", class_="classified__information--address-row").get_text().strip())
locality.append(soup.find("div", {"classified__information--address"}).get_text())

#while next_on:
for i in range(1):
#try:
    python_button = driver.find_elements_by_xpath('//*[@id="classifiedNavigation"]/ul/li[2]/a')[0]
    python_button.click()
    time.sleep(random.uniform(1.0, 3.0))
    soup = BeautifulSoup(driver.page_source)
    price.append(soup.find("p", class_="classified__price").find("span", class_="sr-only").text)
    id_immo.append(soup.find("div", class_="classified__information--immoweb-code").text.strip())
    street.append(soup.find("span", class_="classified__information--address-row").get_text().strip())
    locality.append(soup.find("div", {"classified__information--address"}).get_text())
    #locality.append(soup.find("span"[], {"classified__information--address-row"}).find_next()).get_text.strip()
#except:
    #next_on = False
    #print("no more pages"
#TODO Add loop to iterate in all houses
#soup = BeautifulSoup(driver.page_source)get
#span.append({"Price": soup.find("p", class_="classified__price").find("span", class_="sr-only").text})

driver.close()
# And then it's like Beautiful
print(price)
print(id_immo)
print(street)
print(locality)

print("--- %s seconds ---" % (time.time() - start_time))
=======
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


#options = Options()
#options.add_argument("window-size=1400,600")
#from fake_useragent import UserAgent
#ua = UserAgent()
#a = ua.random
#user_agent = ua.random
#print(user_agent)
#options.add_argument(f'user-agent={user_agent}')


driver = webdriver.Chrome()

driver.get('https://www.immoweb.be/fr/recherche/immeuble-de-rapport/a-vendre')

import time
time.sleep(10)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

results = soup.find_all("div", {"class":"result-xl"})
title=[]
address=[]
price=[]
surface=[]
desc=[]
for result in results:
   title.append(result.find("div", {"class":"title-bar-left"}).get_text().strip())
   address.append(result.find("span", {"result-adress"}).get_text().strip())
   price.append(result.find("div", {"class":"xl-price rangePrice"}).get_text().strip())
   surface.append(result.find("div", {"class":"xl-surface-ch"}).get_text().strip())
   desc.append(result.find("div", {"class":"xl-desc"}).get_text().strip())


df = pd.DataFrame({"Title":title,"Address":address,"Price:":price,"Surface" : surface,"Description":desc})
df.to_csv("output.csv")
>>>>>>> a137d3aed1b02a10d38e8d265eed9bac7d405d60
