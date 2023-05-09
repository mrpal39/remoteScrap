from urllib.parse import urljoin, urlparse
import scrapy
from ..items import JobItem, QuotesItem

"""
command: scrapy crawl some-quotes -a author="<author_name>" -L WARN

Example: scrapy crawl some-quotes -a author="Albert Einstein" -L WARN

Those author name should match the name on the site.
"""
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

class SpecificAuthorQuotesSpider(scrapy.Spider):
    """Extracts the quotes from specific author"""

    name = "jobtag"

    def __init__(self, author=None, **kwargs):
        self.author = author
        self.start_urls = [
            f'https://weworkremotely.com/remote-jobs/search?term={author}&button=']

        super().__init__(**kwargs)

    # url = f'https://weworkremotely.com/remote-jobs/search?term=&button='
    # start_urls = [url]

    allowed_domains = ['weworkremotely.com']
    # start_urls = ['http://books.toscrape.com/']
    base_url = 'https: // weworkremotely.com'

    def parse(self, response, **kwargs):

        item = JobItem()
        import json

        all_div_quotes = response.css('section.jobs')
        for quote in all_div_quotes.css('li.feature'):
            json_object = quote.extract()
            # print(json.dumps(json_object, indent=3))
            url = quote.css('a::attr(href)').extract()
            # print(f"/company/audienceplus'{url[0]}")
            # print(f"remote-jobs,{url[1]}")
            urlJob = url[1]

            book_url = self.base_url + urlJob
            spaceUrl = book_url.replace(" ", "")

            yield scrapy.Request(spaceUrl, callback=self.parse_book)

    def parse_book(self, response):
        # print(response)
        item = JobItem()
        item_tag = QuotesItem()


        #header work post
        JobData = response.css('div.listing-header-container')
        job_title = JobData.css('h1::text').extract()
        job_post_Data= JobData.css('time::text').extract()      
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
            print("Yes")
        else:
            companyUrl =''

            print("No")
        for t in job_post_tags:
            x = re.findall("company",  t)

        if (x):
            print(x)

            print("Yes, there is at least one match!")
        else:
            print(t)
            item_tag['text']=t
            yield item_tag

            print("No match")

        # companyUrl = self.base_url + company_website[1]
        c = len(apply_url[0])

        l_apply_url = 'a:1:{s:3:"url";s:' + str(c) + ':"' + apply_url[0] + '";}'


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
        item['category']=self.author
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
