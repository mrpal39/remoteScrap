# import time
# import os
# import pandas as pd
# from bs4 import BeautifulSoup
# import requests
# import csv
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.common import exceptions
# from urllib.parse import urlparse
# import re
# from selenium.webdriver.chrome.service import Service as ChromiumService
# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver


# os.environ['PATH'] += r"/home/rahul/dev"

# service = Service(executable_path='/snap/bin/chromium.chromedriver')
# driver = webdriver.Chrome(service=service)
# # driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# driver.get("https://weworkremotely.com/remote-jobs/search?term=&button=")
# driver.implicitly_wait(30)

# what = driver.find_element(by=By.ID, value="search--input")

# InputFile='programming'

# what.send_keys(InputFile)

# driver.implicitly_wait(30)

# search_button = driver.find_element(by=By.ID, value='post-job-cta').click()
# driver.implicitly_wait(30)

# l_list = []
# job_search = driver.find_elements(by=By.CLASS_NAME, value=("title"))
# # print(job_search)
# ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
# for i in range(0, 20):
#     try:
#         if job_search[i].is_displayed():
#             job_search[i].click()
#             l_list.append(driver.current_url)
#             driver.back()
#             # print(driver.current_url)
#     except exceptions.StaleElementReferenceException as e:
#         # print(e)
#         job_search = driver.find_elements(by=By.CLASS_NAME, value=("title"))
#         job_search[i].click()
#         # print(driver.current_url)
#         l_list.append(driver.current_url)
#         driver.back()
#         pass


# for i in l_list:
#     DataColoums=[]    

#     source = requests.get(i).text
#     soup = BeautifulSoup(source, 'lxml')
#     job = soup.find('div', class_='content')
#     job_title = job.h1.text
#     job_description = soup.find('div', class_='listing-container')
#     job_type = soup.find('span', class_="listing-tag").text
#     company_name = job.h2.a.text.replace(' ', '')
#     external_url = soup.find("a", {"id": "job-cta-alt"}).get("href")
#     c = len(external_url)
#     l_apply_url = 'a:1:{s:3:"url";s:' + str(c) + ':"' + external_url + '";}'
#     try:
#         logo = soup.find('div', class_='listing-logo').img.get('src')
#         parse = urlparse(logo)
#         url = parse[0] + "://" + parse[1] + parse[2] + parse[3]
#     except:
#         print('No element with this class name found...')
#     country = soup.find('div', class_='company-card').h3.text

#     data = soup.find_all('div', attrs={'class': 'company-card'})
#     for div in data:
#         temp = []
#         links = div.find_all('a', attrs={'href': re.compile("^https://")})
#         for a in links:
#             l = a['href']
#             l1 = list(l.split(","))
#             temp.append(l1)
#         company_url = temp[0][0]

#         # csv_writer.writerow([url, job_title, company_name, company_url, country, job_type, job_description,
#         #     
#         #                 l_apply_url, company_name, company_url, company_url])  # ,  company_url, company_url


#         # import datetime
#         # from datetime import date
#         # from datetime import datetime, date, timedelta


#         # Created =data.today()   
#         # result_1 = today + timedelta(days=3)
#     DataColoums += [
#         {

#             "job.company_logo":url,
#             "job.job_title":job_title,
#             "job.company_name":company_name,
#             "job.company_email":company_url,
#             "job.is_approved":1,
#             "job.is_active":1,
#             "job.is_filled":1,
#             "job.is_featured":1,
#             "job.company_url":company_url,
#             "job.job_country":country,
#             "job.job_state":country,
#             "job.job_zip_code":'12455',
#             "job.job_city":country,
#             "job.job_address":country,
#             "job.category":"demo",
#             "job.type":job_type,
#             "job.payment_method":"cash",
#             "job.job_created_at":"2020-09-22",
#             "job.job_expires_at":"2020-09-22",
#             "job.job_description":job_description,
#             "job.wpjobboard_am_data":l_apply_url,
#             "job.companyid":'45',
#             "job.companycompany_name":company_name,
#             "job.companyuser_email":'demoa@gmail.com    ',
#             "job.companycompany_website":company_url,
#             "job.company_url":company_url,
#         }


#     ]



#     if len(DataColoums):
            
#         filename =f"{InputFile}.csv"

#         with open(filename, 'a+', encoding='UTF8', newline='') as f:


#             new_column_names = [
#                 "job.company_logo",
#                 "job.job_title",
#                 "job.company_name",
#                 "job.company_email",
#                 "job.is_approved",
#                 "job.is_active",
#                 "job.is_filled",
#                 "job.is_featured",
#                 "job.company_url",
#                 "job.job_country",
#                 "job.job_state",
#                 "job.job_zip_code",
#                 "job.job_city",
#                 "job.job_address",
#                 "job.category",
#                 "job.type",
#                 "job.payment_method",
#                 "job.job_created_at",
#                 "job.job_expires_at",
#                 "job.job_description",
#                 "job.wpjobboard_am_data",
#                 "job.companyid",
#                 "job.companycompany_name",
#                 "job.companyuser_email",
#                 "job.companycompany_website",

#                 "job.company_url",

#             ]

#             # csv_writer = csv.writer(f)
#             writer = csv.DictWriter(f, fieldnames=new_column_names)

#         # writing headers (field names)
#             writer.writeheader()

#             # writing data rows
#             writer.writerows(DataColoums)
#                 # csv_writer.writerow(new_column_names)
#                 # csv_writer.writerow([url, job_title, company_name, company_url, country, job_type, job_description,
#             #                     l_apply_url, company_name, company_url, company_url])  # ,  company_url, company_url
