import json
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromiumService
from urllib.parse import urlparse
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import csv
import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import quote_plus
import scrapy
from ..items import JobItem, QuotesItem

import urllib.parse
from urllib.parse import urljoin, urlparse

# Python3 program to check
# URL is valid or not
# using regular expression
import re

# Function to validate URL
# using regular expression


def isValidURL(str):

    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if (re.search(p, str)):
        return True
    else:
        return False

    # Driver code


# This code is contributed by avanitrachhadiya2155
# import pandas as pd

os.environ['PATH'] += r"/home/rahul/dev"

service = Service(executable_path='/snap/bin/chromium.chromedriver')
driver = webdriver.Chrome(service=service)
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# driver.get("https://www.amazon.com/")
# driver.implicitly_wait(30)

# what = driver.find_element(by=By.ID, value="twotabsearchtextbox")

# # InputFile = 'Redmi'

# what.send_keys(InputFile)

# driver.implicitly_wait(30)

# search_button = driver.find_element(
#     by=By.ID, value='nav-search-submit-button').click()
# driver.implicitly_wait(30)

# l_list = []
# job_search = driver.find_elements(by=By.CLASS_NAME, value=("sg-col-inner"))
# print(len(job_search))
# ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)


class QuotesSpider(scrapy.Spider):

    name = "aws"
    # driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.get("https://www.amazon.com/")
    driver.implicitly_wait(30)

    what = driver.find_element(by=By.ID, value="twotabsearchtextbox")

    InputFile = 'samsung phone'

    what.send_keys(InputFile)

    driver.implicitly_wait(30)

    search_button = driver.find_element(
        by=By.ID, value='nav-search-submit-button').click()
    driver.implicitly_wait(30)

    # l_list = []
    # job_search = driver.find_elements(by=By.CLASS_NAME, value=("sg-col-inner"))
    # # print(len(job_search))
    # print
    # ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    allowed_domains = ['amazon.com']
    # start_urls = ['http://books.toscrape.com/']
    base_url = 'https://amazon.com'

    start_urls = [
        driver.current_url]

    def parse(self, response, **kwargs):
        item = JobItem()
        import json
        all_div_quotes = response.css('div.s-matching-dir')
        # print(response)
        for quote in all_div_quotes.css('.rush-component'):
            # print(quote)

        #     print(quote)
        # #     json_object = quote.extract()
            url = quote.css('a::attr(href)').extract_first()
            if url is not None:
                demo=isValidURL(url)
                if demo is False:
                    book_url =self.base_url + url
                    # print(book_url) 
                    yield scrapy.Request(book_url, callback=self.parse_book)
        # #     # pass

    def parse_book(self, response):
        # print(response)

        JobData = response.css('.centerColAlign')
        # print(JobData)
        dumpTitle = JobData.css('#productTitle::text').extract()
        if len(dumpTitle):
            # print()
            productName=dumpTitle[0]
            str1 = productName.replace(' ','')
            fileName=str1[:20]            
            name=f"{fileName}.json"
    
            #     # pass
            #     print(response.url)
    #########################################productOverview_feature_div
            desc = JobData.css('#productOverview_feature_div')        
            tb=desc.css("table")
            divs = tb.css('tr')
            # print(divs)
            lDetail=[]

            for div in divs:
                Detail = dict()

                productAbout=div.css("span::text").extract()
                Detail={
                    productAbout[0]:productAbout[1]
                }
                lDetail.append(Detail)
                # print(div.css("span::text").extract())

            ###############################productOverview_feature_div##########################################
            featurebullets = JobData.css('#feature-bullets')     
            fH=featurebullets.css("h1::text").extract()
            # print(fH)   
            uls=featurebullets.css("ul")
            lAbout=[]
            
            for fHdiv in uls:
                f= fHdiv.css("li")
                lspan=f.css("span::text").extract()
                lAbout.append(lspan)
                # print(f.css("span::text").extract())
##################################################productDescription##################################################
            productDescription = response.css('#productDescription_feature_div')
            ph1=pDescription =productDescription.css("h2::text").extract()
            # print(ph1[0])

            pDescription =productDescription.css("span::text").extract()
            # print(pDescription)


            dictionary={

                'url':response.url,
                'product Name':productName,
                'productDetail':lDetail,
                'about':lAbout,
                 ph1[0]:pDescription[0],

            }
            # # print(dictionary)
            # with open(os.path.join('../../../dump/',name), "w") as outfile:   
            #     json.dump(dictionary, outfile,ensure_ascii=False, indent=4)


            directory = f'./dump/'
            file_path = os.path.join(directory, name)
            if not os.path.isdir(directory):
                os.mkdir(directory)

            file = open(file_path, "w")
            json.dump(dictionary, file,ensure_ascii=False, indent=4)

    # #     job_post_Data= JobData.css('span.productTitle::text').extract()

    # #     companyLogo = response.css("div.listing-logo")
    # #     url = companyLogo.css('img').xpath('@src').extract()
    # #     post_tag=response.css('span.listing-tag::text').extract()
    # #     Logo_url=urljoin(url[0], urlparse(url[0]).path)  # 'http://example.com/'

    # #     content = response.css('div.listing-container').extract()
    # #     aurl = response.css('div.apply_tooltip')
    # #     apply_url = aurl.css('a::attr(href)').extract()#apply link grap

    # #     company = response.css("div.company-card")
    # #     companyCountry = company.css('h3::text').extract()
    # #     company_website = company.css('a::attr(href)').extract()
    # #     company_name = company.css('a::text').extract()
    # #     companyDetail=company_website[2]

    # #     if(isValidURL(companyDetail) == True):
    # #         companyUrl = companyDetail
    # #         print("Yes")
    # #     else:
    # #         companyUrl =''

    # #         print("No")

    # #     # companyUrl = self.base_url + company_website[1]
    # #     c = len(apply_url[0])

    # #     l_apply_url = 'a:1:{s:3:"url";s:' + str(c) + ':"' + apply_url[0] + '";}'

    # #     item['job_title'] = job_title[0]
    # #     item['job_description'] = content[0]
    # #     item['company_logo'] = Logo_url
    # #     item['company_website'] = companyUrl
    # #     item['company_name']=company_name[0]
    # #     item['company_email']='admin@remotejobhunt.com'
    # #     item['company_url']=companyUrl
    # #     item['job_country']=companyCountry[-1]
    # #     item['job_state']=companyCountry[-1]
    # #     item['job_city']=companyCountry[-1]
    # #     item['job_address']=companyCountry[-1]
    # #     item['category']=post_tag[1]
    # #     item['type']=post_tag[0]
    # #     item['job_zip_code']='145521'
    # #     item['company_country']=companyCountry[-1]
    # #     item['company_state']=companyCountry[-1]
    # #     item['company_zip_code']='45458'
    # #     item['company_location']=companyCountry[-1]
    # #     item['wpjobboard_am_data'] =l_apply_url
    # #     yield ite

        next=response.css(".s-pagination-strip")
        apply_url = next.css('a::attr(href)').extract()#apply link grap
        # if len(apply_url):

        #     print(apply_url)

            

        # next_page = next.css('span.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
