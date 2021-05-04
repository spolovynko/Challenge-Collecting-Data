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
