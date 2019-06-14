import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import codecs
import mysql.connector
from openpyxl import load_workbook
st = 1
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "test"
	)
sql = "INSERT INTO test.rank (rank, club, country, now_pts, diff, before_pts) VALUES (%s, %s, %s, %s, %s, %s)"
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
mycursor = mydb.cursor()
options = webdriver.ChromeOptions ()
options.add_argument ('window-size=1920x1080')
options.add_argument('--log-level=3')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
for i in range(50):
	print("https://footballdatabase.com/ranking/world/"+str(i+1))

	driver.get("https://footballdatabase.com/ranking/world/"+str(i+1))
	for j in range(51):
		try:
			rank = driver.find_element_by_xpath('//div/table/tbody/tr['+str(j+1)+']/td[@class="rank"][1]')
			r = int(rank.text)
			club = driver.find_element_by_xpath('//div/table/tbody/tr['+str(j+1)+']/td/a/div[@class="limittext"]')
			c = club.text.encode()	
			country = driver.find_element_by_xpath('//div/table/tbody/tr['+str(j+1)+']/td/a[@class="sm_logo-name"]')
			count = country.text.encode()
			now_pts = driver.find_element_by_xpath('//div/table/tbody/tr['+str(j+1)+']/td[@class="rank"][2]')
			now_pts_int = int(now_pts.text)
			before_pts = driver.find_element_by_xpath('//div/table/tbody/tr['+str(j+1)+']/td/div[@style="font-size: small;"]')
			x = int(now_pts.text)
			y = int(before_pts.text)
			diff = x-y			
			val = (r, c, count, x, diff, y)
			mycursor.execute(sql, val)
			mydb.commit()
			print(mycursor.rowcount, "record inserted.")
		except:
			k=1
		
	time.sleep(st)
mycursor.close()
mydb.close()