from urllib.parse import quote_plus
import scrapy
from ..items import JobItem, QuotesItem
import re

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
	if(re.search(p, str)):
		return True
	else:
		return False

    # Driver code

   

# This code is contributed by avanitrachhadiya2155



class QuotesSpider(scrapy.Spider):

    def __init__(self, author=None, **kwargs):
        self.author = author
        self.start_urls = [
            f'https://weworkremotely.com/{author}']

        super().__init__(**kwargs)


    name = "quotes"

    allowed_domains = ['weworkremotely.com']
    # start_urls = ['http://books.toscrape.com/']
    base_url = 'https://weworkremotely.com'

    def parse(self, response, **kwargs):
        item = JobItem()
        import json
        # print(response.url)

        all_div_quotes = response.css('section.jobs')
        for quote in all_div_quotes.css('li'):
            json_object = quote.extract()
            url = quote.css('a::attr(href)').extract()
            title_job = quote.css('span.title::text').extract()
            title_job_new = quote.css('span::text').extract()
            if len(url)==2:
                    
                urlJob = url[1]
                print(url[1], len(url))

                book_url = self.base_url + urlJob
                print(book_url)
                yield scrapy.Request(book_url, callback=self.parse_book)

    def parse_book(self, response):
        print('#########################################################################response.url')

        # print(response.url)
        # print('#########################################################################response.url')


        item = JobItem()
        item_tag= QuotesItem()

        #header work post
        JobData = response.css('div.listing-header-container')
        job_title = JobData.css('h1::text').extract()

        job_post_filter = JobData.css('time::text').extract()

        job_post_Data = JobData.css('time::attr(datetime)').extract()
        job_post_tags = JobData.css(
            'a::attr(href)').extract()  # apply link grap
        companyLogo = response.css("div.listing-logo")        
        url = companyLogo.css('img').xpath('@src').extract()
        post_tag=response.css('span.listing-tag::text').extract()
        Logo_url=urljoin(url[0], urlparse(url[0]).path)  # 'http://example.com/'
       

        content = response.css('div.listing-container').extract()
        aurl = response.css('div.apply_tooltip')
        apply_url = aurl.css('a::attr(href)').extract()#apply link grap

        company = response.css("div.company-card")
        companyCountry = company.css('h3::text').extract()
        company_website = company.css('a::attr(href)').extract()
        company_name = company.css('a::text').extract()
        companyDetail=company_website[2]

        if(isValidURL(companyDetail) == True):
            companyUrl = companyDetail
        else:
            companyUrl =''
        for t in job_post_tags:
            x = re.findall("company",  t)

            if (x):
                # print(x)
# 
                print("Yes, there is at least one match!")
            else:
                # print(t)
                item_tag['text']=t
                yield item_tag

                # print("No match")


             
        
        companyUrl = self.base_url + company_website[1]
        c = len(apply_url[0])

        l_apply_url = 'a:1:{s:3:"url";s:' + str(c) + ':"' + apply_url[0] + '";}'
        item['job_created_at'] = job_post_Data[0]


        item['job_title'] = job_title[0]
        item['job_description'] = content[0]
        item['company_logo'] = Logo_url
        item['company_website'] = companyUrl
        item['company_name']=company_name[0]
        item['company_email']='admin@remotejobhunt.com'
        item['company_url']=companyUrl
        item['job_country']=companyCountry[-1]
        item['job_state']=companyCountry[-1]
        item['job_city']=companyCountry[-1]
        item['job_address']=companyCountry[-1]
        item['category']=post_tag[1]
        item['type']=post_tag[0]
        item['job_zip_code']='145521'
        item['company_country']=companyCountry[-1]
        item['company_state']=companyCountry[-1]
        item['company_zip_code']='45458'
        item['company_location']=companyCountry[-1]  
        item['wpjobboard_am_data'] =l_apply_url
        yield item


        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
