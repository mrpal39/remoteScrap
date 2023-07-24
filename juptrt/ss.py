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

# os.environ['PATH'] += r"D:/Bhawana/Scrapping Data/IndeedData"
# driver = webdriver.Chrome()
# driver.get("https://weworkremotely.com/remote-jobs/search?term=&button=")
# driver.implicitly_wait(30)

# what = driver.find_element_by_id("search--input")
# what.send_keys('marketing')
# driver.implicitly_wait(30)

# search_button = driver.find_element_by_id('post-job-cta').click()
# driver.implicitly_wait(30)

# l_list = []
# job_search = driver.find_elements_by_class_name("title")
# ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
# for i in range(0, len(job_search)):
#     try:
#         if job_search[i].is_displayed():
#             job_search[i].click()
#             l_list.append(driver.current_url)
#             driver.back()
#             # print(driver.current_url)
#     except exceptions.StaleElementReferenceException as e:
#         # print(e)
#         job_search = driver.find_elements_by_class_name("title")
#         job_search[i].click()
#         # print(driver.current_url)
#         l_list.append(driver.current_url)
#         driver.back()
#         pass  
# print(l_list)
# print(len(l_list))
# #==================================================================================================================
# for i in l_list:
#     source = requests.get(i).text
#     soup = BeautifulSoup(source, 'lxml')

#     # file = open('data.csv', 'w', encoding='UTF8')
#     # writer = csv.writer(file)
#     # writer.writerow(['Title', 'Description', 'Job Type', 'Company Name', 'Logo', 'Country', 'External URL'])

#     job = soup.find('div', class_='content')
#     job_title = job.h1.text
#     job_description = soup.find('div', class_='listing-container')
#     job_type = soup.find('span', class_="listing-tag").text
#     company_name = job.h2.a.text.replace(' ','')
#     external_url = soup.find("a",{"id":"job-cta-alt"}).get("href")
#     c =len(external_url)
#     l_apply_url = 'a:1:{s:3:"url";s:' + str(c) + ':"' + external_url + '";}'

#     try: 
#         logo = soup.find('div', class_='listing-logo').img.get('src')
#         parse = urlparse(logo)
#         url = parse[0] + "://" + parse[1] + parse[2] + parse[3]
#     except:
#         print('No element with this class name found...')
#     country = soup.find('div', class_='company-card').h3.text
#     # count = soup.find('div', class_='company-card')
#     # com = count.find_all('h3')
#     # for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
#     #     print(link.get('href'))  

#     data = soup.find_all('div',attrs={'class':'company-card'})
#     for div in data:
#         temp = []
#         links = div.find_all('a', attrs={'href': re.compile("^https://")})
#         for a in links:
#             l = a['href']
#             l1 = list(l.split(","))
#             temp.append(l1)
#         company_url = temp[0][0]
#         # l2 = l1[0]
#         # parse = urlparse(l2)
#         # # url = parse[0] + "://" + parse[1] + parse[2] + parse[3]
#         # print(parse[0] + "://" + parse[1])
    

#     # # l = com[2]
#     # print(int(com['href']))
#     # count = soup.select("div ~ h3 ~ a")
#     # componay_url = com.h3.a.get("href")
#     # for item in soup.find_all(["h3"]):
#     #     i =list(item)
#     #     print(i[4])
#     # our_text = soup.select_one('div h3 a')
#     # print(our_text)

#     # special_divs = soup.find_all('div',{'class':'company-card'})
#     # for text in special_divs:
#     #     download = text.find_all('a', href = re.compile('\.mp3$'))
#     #     for text in download:
#     #         hrefText = (text['href'])
#     #         print(hrefText)

#     # print(f'''
#     # Title: {job_title}
#     # Description: {job_description}
#     # Job Type: {job_type}
#     # Company Name: {company_name}
#     # Logo: {url}
#     # Country: {country}
#     # ''')
#     # heading = count.find_all("h3")
#     # n=len(heading)
#     # for x in range(n): 
#     #     # print(str.strip(heading[x].text))
#     #     print(heading[x].get('href'))



#     with open('data.csv', 'a+', encoding='UTF8', newline='') as f:
#         csv_writer = csv.writer(f)
#         # csv_writer.writerow(['Title', '         after company_name , company_url
#         csv_writer.writerow([url, job_title, company_name, company_url, country, job_type, job_description, l_apply_url, company_name, company_url, company_url]) #,  company_url, company_url
        
#     # writer.writerow([job_title, job_description, job_type, company_name, logo, country, external_url])
#     # file.close()

#     # dictionary = {'Title' : 'job_title', 'Description' : 'job_description', 'Job Type' : 'job_type', 'Company Name' : 'company_name', 'Logo' : 'logo', 'Country' : 'country', 'External URL' : 'external_url'}
#     # df = pd.DataFrame(dictionary, index=[i])
#     # to_csv = df.to_csv('data.csv')

