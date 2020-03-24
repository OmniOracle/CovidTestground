# import urllib.request, urllib.parse, urllib.error
# import ssl
# import numpy as np
# import pandas as pd
# import matplotlib as plt
import bs4 as soup
import requests as requests
import csv

# Get link
res = requests.get(
    'https://www.rivm.nl/en/news/current-information-about-novel-coronavirus-covid-19')

# Feed page into bs4
data = soup.BeautifulSoup(res.content, 'lxml')

# Use css selector to extract relevant data
patients = data.select('table')
page = data.select('p')
date = page[3].getText(strip=True)

current_date = date.find('date')
date_time = (date[current_date+5:])
# Convert data to string object
sPatients = patients[0].getText(strip=True)
print(patients)
# Test string object for digits
covid_numbers = ''.join(filter(lambda i: i.isdigit(), sPatients))
# write relevant data to CSV file
with open('covidNL.csv', 'a', newline='') as csvfile:
    datafile = csv.writer(csvfile, lineterminator='\n')
    datafile.writerow([covid_numbers])
# datafile.writerow(['Date','Patients'])
# datafile.writerow([date_time])

print(covid_numbers)
