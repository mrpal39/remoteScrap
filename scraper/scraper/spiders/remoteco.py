from urllib.parse import quote_plus
import scrapy
from ..items import JobItem, QuotesItem
import re
from datetime import datetime, timedelta

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

class QuotesSpider(scrapy.Spider):

    def __init__(self, author=None, **kwargs):
       
                
        self.author = author
        self.start_urls = [
            f'https://remote.co{author}']
      
        super().__init__(**kwargs)

    name = "remoteco"

    allowed_domains = ['remote.co']
    # start_urls = ['http://books.toscrape.com/']
    base_url = 'https://remote.co'

    def parse(self, response, **kwargs):
        item = JobItem()
        import json
        print(response.url)

        all_div_quotes = response.xpath(
            "/html/body/main/div[2]/div/div[1]/div[5]/div/div[2]/div")
        # print(all_div_quotes)
        for quote in all_div_quotes.css('a::attr(href)'):
            json_object = quote.extract()
            url = quote.extract()
            book_url = self.base_url + url

            print(book_url)
            # title_job = quote.css('span.title::text').extract()
            # title_job_new = quote.css('span::text').extract()
            # if len(url)==2:
            #     urlJob = url[1]
            yield scrapy.Request(book_url, callback=self.parse_book)

    def parse_book(self, response):
        print('#########################################################################')

        JobData = response.xpath('/html/body/main/div/div/div[1]/div[2]/div')
        job_title = JobData.css('h1::text').extract()

        job_post_filter = JobData.css('time::text').extract()

        job_post_Data = JobData.css('time::attr(datetime)').extract()

    #     # Replace with whatever you want
    #     # date = datetime.datetime()
        # if job_post_Data:
                
        #     # # You can even find the current date and time using this expression
        #     tod = datetime.now()


        #     d = timedelta(days=15)
        #     a = tod - d
        #     # now = datetime.now()+timedelta(5)
        #     print(tod)
        #     print(a)

        #     date = datetime.strptime(job_post_Data[0], '%Y-%m-%dT%H:%M:%S%z')
        #     print(job_title)
        #     print(date.date() ,a.date())

        #     if date.date() < a.date():
        #         print('past')
        #     elif date.date() > a.date():
    

        item = JobItem()
        item_tag= QuotesItem()

        job_post_tags = JobData.css(
            'a::attr(href)').extract()  # apply link grap
        companyLogo = response.css("div.listing-logo")        
        url = companyLogo.css('img').xpath('@src').extract()
        post_tag = response.xpath(
            '/html/body/main/div/div/div[1]/div[2]/div/div[1]/div[1]/div[3]/div[2]/span/a[1]/text()').extract()
        Logo_url = response.xpath(
            "/html/body/main/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/img/@data-lazy-src").extract()

        content = response.xpath(
            '/html/body/main/div/div/div[1]/div[2]/div/div[1]/div[3]').getall()
        aurl = response.xpath(
            '/html/body/main/div/div/div[1]/div[2]/div/div[1]/div[4]')
        apply_url = aurl.css('a::attr(href)').extract()#apply link grap
        # print(apply_url)

        # company = response.css("div.company-card")
        # companyCountry = company.css('h3::text').extract()
        company_website = response.xpath(
            '/html/body/main/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/a/@href').extract()
        company_name = response.xpath(
            '/html/body/main/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/strong//text()').extract()
        companyDetail=company_website[0]

        item['job_created_at'] = job_post_Data[0]




        item['job_title'] = job_title[0]
        item['job_description'] = content[0]
        item['company_logo'] = Logo_url[0]
        item['company_website'] = companyDetail
        item['company_name']=company_name[0]
        item['company_email']='admin@remotejobhunt.com'
        item['company_url'] = companyDetail
        item['job_country']=''
        item['job_state']=''
        item['job_city']=''
        item['job_address']=''
        item['category']=post_tag
        item['type']=post_tag
        item['job_zip_code']='145521'
        item['company_country']=''
        item['company_state']=''
        item['company_zip_code']='45458'
        item['company_location']="remote"
        item['wpjobboard_am_data'] = apply_url
        yield item


        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
