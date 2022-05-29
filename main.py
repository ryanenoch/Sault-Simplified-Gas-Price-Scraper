#To run Selenium in Replit IDE
#https://replit.com/talk/ask/Can-I-use-selenium/11566

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import pandas as pd

options = Options()
options.add_argument("--window-size=1920x1080")
options.headless = True #Headless = No GUI

#add these two lines if running from replit IDE!!!!
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://www.sootoday.com/gas-prices")

items = driver.find_element(By.TAG_NAME, "table")
gasdata = items.text
print(gasdata)
print()
gasdata = items.text.replace("\n\n\n",",")

headings = {'Station','Address','City'}
cities = {'Echo Bay','Sault Ste Marie','Bruce Mines','Thessalon','Desbarats'}
stations = {'Heyden Fuels','Esso',"Mac's",'Circle K',"Canadian Tire","Shell",'Petro-Canada','Flying J','Pit Stop'}

for heading in headings:
  gasdata = gasdata.replace(f"{heading}",f",{heading}")
for station in stations:
  gasdata = gasdata.replace(f"{station}",f",{station} ")
for city in cities:
  gasdata = gasdata.replace(f"{city}",f",{city}")

gasdata = gasdata.replace("Thessalon ,Esso","Thessalon Esso")

#print(gasdata)
#print(type(items.text)) #<class 'str'>

#Copies Gas Station Data to CSV (can be used for diagnosis)
text_file = open("ssmgas.csv", "w")
n = text_file.write(gasdata)
text_file.close()

df = pd.read_csv("ssmgas.csv", sep=",")
#print(df)
#print()
df.drop(df.tail(1).index,inplace=True) # drop last row
print(df)
print()
