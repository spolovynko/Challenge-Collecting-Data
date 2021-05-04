from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup
start_time = time.time()


span = list()
url='https://www.immoweb.be/fr/recherche/maison/a-vendre?countries=BE&maxPrice=100000&orderBy=relevance'
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
time.sleep(random.uniform(1.0, 3.0))
python_button = driver.find_elements_by_xpath('//*[@id="uc-btn-accept-banner"]')[0]
python_button.click()
time.sleep(random.uniform(1.0, 3.0))
python_button = driver.find_elements_by_xpath('//*[@id="classified_9305962"]')[0]
python_button.click()
soup = BeautifulSoup(driver.page_source)
time.sleep(random.uniform(1.0, 3.0))
price = []
next_on = True
#TODO ADD all list
price.append(soup.find("p", class_="classified__price").find("span", class_="sr-only").text)
#while next_on:
for i in range(5):
    try:
        python_button = driver.find_elements_by_xpath('//*[@id="classifiedNavigation"]/ul/li[2]/a')[0]
        python_button.click()
        time.sleep(random.uniform(1.0, 3.0))
        soup = BeautifulSoup(driver.page_source)
        price.append(soup.find("p", class_="classified__price").find("span", class_="sr-only").text)
    except:
        next_on = False
        print("no more pages")
#TODO Add loop to iterate in all houses
#soup = BeautifulSoup(driver.page_source)
#span.append({"Price": soup.find("p", class_="classified__price").find("span", class_="sr-only").text})

driver.close()
# And then it's like Beautiful
print(price)

print("--- %s seconds ---" % (time.time() - start_time))
