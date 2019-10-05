from selenium import webdriver
import shutil
import time 
import xlrd
import csv


"""def csv_from_excel():

    wb = xlrd.open_workbook('xxxx.xls')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('your_csv_file.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()"""

driver = webdriver.Chrome('ChromeLocation')
URL = "URLYouNeed"

#This helps to login as Ursula on the /uumontclair site and then download a spreadsheet containing items
def download_item():
    driver.get(URL)
    driver.find_element_by_name("phone").send_keys("xxxxxxxx")
    driver.find_element_by_name("pin").send_keys("xxxxxx")
    driver.find_element_by_xpath("//input[@value='Login']").click()
    driver.find_element_by_link_text('Reports').click()
    driver.find_element_by_link_text('Item Spreadsheet').click()
    
#This helps to login as Ursula on the /uumontclair site and then upload the winners
def sales_winning():
    driver.get(URL)
    driver.find_element_by_name("phone").send_keys("xxxxxxxx")
    driver.find_element_by_name("pin").send_keys("xxxxxx")
    driver.find_element_by_xpath("//input[@value='Login']").click()
    driver.find_element_by_link_text('Sales').click()
    driver.find_element_by_name('itemNumber').send_keys('D5')
    driver.find_element_by_xpath("//input[@name='paddle']").send_keys('4')
    driver.find_element_by_xpath("//input[@name='qty']").send_keys('0')
    driver.find_element_by_xpath("//input[@name='price']").send_keys('0')

download_item()
