from urllib.parse import quote_plus
import scrapy
from ..items import JobItem, QuotesItem

import urllib.parse
from urllib.parse import urljoin, urlparse

# Python3 program to check
# URL is valid or not
# using regular expression
import re
import time
import os
import requests
import csv
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
# # Function to validate URL
# # using regular expression
# def isValidURL(str):

# 	# Regex to check valid URL
# 	regex = ("((http|https)://)(www.)?" +
# 			"[a-zA-Z0-9@:%._\\+~#?&//=]" +
# 			"{2,256}\\.[a-z]" +
# 			"{2,6}\\b([-a-zA-Z0-9@:%" +
# 			"._\\+~#?&//=]*)")
	
# 	# Compile the ReGex
# 	p = re.compile(regex)

# 	# If the string is empty
# 	# return false
# 	if (str == None):
# 		return False

# 	# Return if the string
# 	# matched the ReGex
# 	if(re.search(p, str)):
# 		return True
# 	else:
# 		return False

    # Driver code

   

# This code is contributed by avanitrachhadiya2155



class QuotesSpider(scrapy.Spider):

    start_urls = [
        'https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=software&locationstring=&sort=M']

    name = "email_job"

    allowed_domains = ['jobbank.gc.ca']
    # start_urls = ['http://books.toscrape.com/']
    base_url = 'https://www.jobbank.gc.ca'

    def parse(self, response, **kwargs):
        item = JobItem()
        import json

        all_div_quotes = response.css('.results-jobs')

        for quote in all_div_quotes.css('article'):
            json_object = quote.extract()
            url = quote.css('a::attr(href)').extract()
            urlJob = url[0]

            book_url = self.base_url + urlJob

            yield scrapy.Request(book_url, callback=self.parse_book)

    def parse_book(self, response):
        # item = JobItem()

        # #header work post
        # driver.get(response.url)
        # driver.implicitly_wait(20)
        # job_search_botton = driver.find_elements(by=By.ID, value=("applynowbutton"))
        # job_search_botton[-1].click()
        # driver.implicitly_wait(70)

        # JobData = response.css('.howtoapply')
        # jh1=response.css('h3::text').extract()


        # job_title = JobData.css('.howtoapply')
        # apply_url = job_title.css('a::attr(href)').extract()#apply link grap
        # print(jh1)
        # job_post_Data= JobData.css('time::text').extract()      

        # companyLogo = response.css("div.listing-logo")        
        # url = companyLogo.css('img').xpath('@src').extract()
        # post_tag=response.css('span.listing-tag::text').extract()
        # Logo_url=urljoin(url[0], urlparse(url[0]).path)  # 'http://example.com/'
       

        # content = response.css('div.listing-container').extract()
        # aurl = response.css('div.apply_tooltip')

        # company = response.css("div.company-card")
        # companyCountry = company.css('h3::text').extract()
        # company_website = company.css('a::attr(href)').extract()
        # company_name = company.css('a::text').extract()
        # companyDetail=company_website[2]

        # if(isValidURL(companyDetail) == True):
        #     companyUrl = companyDetail
        #     print("Yes")
        # else:
        #     companyUrl =''

        #     print("No")
        
        # # companyUrl = self.base_url + company_website[1]
        # c = len(apply_url[0])

        # l_apply_url = 'a:1:{s:3:"url";s:' + str(c) + ':"' + apply_url[0] + '";}'


        # item['job_title'] = job_title[0]
        # item['job_description'] = content[0]
        # item['company_logo'] = Logo_url
        # item['company_website'] = companyUrl
        # item['company_name']=company_name[0]
        # item['company_email']='admin@remotejobhunt.com'
        # item['company_url']=companyUrl
        # item['job_country']=companyCountry[-1]
        # item['job_state']=companyCountry[-1]
        # item['job_city']=companyCountry[-1]
        # item['job_address']=companyCountry[-1]
        # item['category']=post_tag[1]
        # item['type']=post_tag[0]
        # item['job_zip_code']='145521'
        # item['company_country']=companyCountry[-1]
        # item['company_state']=companyCountry[-1]
        # item['company_zip_code']='45458'
        # item['company_location']=companyCountry[-1]  
        # item['wpjobboard_am_data'] =l_apply_url
        # yield item


        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
