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
