## About The Project:

The project was done with the aim:

Scrape Belgian real-estate website - Immoweb.be
Extract data from it
Create a data set
Write the data set into a csv file

## Team:

Samuel Dodet
Sergiy Polovynko

## Project requires:

[Selenium](https://selenium-python.readthedocs.io/)

[Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[Pandas](https://pandas.pydata.org/)

file_reader module provided with the repository

## How it works:

import selenium, beautifulsoup and pandas libraries
selenium - to navigate dynmicaly through website pages
bs4 - scraps the content
pandas - writes the libraries

provide the list of immoweb searches (based on pricing criteria)

create a dictionary of lists. Lists will stock values of searched criterias.

Launch a loop that will:

Take the url from the list(url will contain customized search based on a price)
CLick automatically on the "Accept Conditions" button
Click on the first search appearing on the page
Read through the page
Scraped values are appended recursively to the dictionary of lists created previously
Website proceeds to the next page, by using 'next' link present on the page

Scraping loop comprehend multiple error handeling:
In case if the next link is not present on the page the page go back one step in order to relaunch it's sequence
In case if the next link button is unclickable, the loop breaks and next price set of properties is launched

Once all the values are gatheres in the object of lists - the object is treated by pandas library and transformed into a data frame
The data frame on it's turn is written into a csv file.

 



