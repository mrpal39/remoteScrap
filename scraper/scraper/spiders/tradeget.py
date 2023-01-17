from urllib.parse import urljoin, urlparse
import scrapy
from ..items import JobItem, QuotesItem
from bs4 import BeautifulSoup
"""
command: scrapy crawl some-quotes -a author="<author_name>" -L WARN

Example: scrapy crawl some-quotes -a author="Albert Einstein" -L WARN

Those author name should match the name on the site.
"""
import re

# Function to validate URL
# using regular expression

# Driver code


class SpecificAuthorQuotesSpider(scrapy.Spider):
    """Extracts the quotes from specific author"""

    name = "trade"

    # def __init__(self, author=None, **kwargs):
    #     self.author = author
    #     self.start_urls = [
    #         f'https://weworkremotely.com/remote-jobs/search?term={author}&button=']

    #     super().__init__(**kwargs)

    # url = f'https://weworkremotely.com/remote-jobs/search?term=&button='

    start_urls = [
        'https://gocharting.com/terminal?ticker=NSE%3ANIFTY']

    allowed_domains = ['gocharting.com']
    # start_urls = ['http://books.toscrape.com/']
    base_url = 'https://gocharting.com'

    def parse(self, response, **kwargs):
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.find_all(class_='gocharting-tooltip-wrapper'))
        """
        Parses the response page for quotes
        """
        # res = response.css('div.main')
        # all_div_quotes = res.css('.advanced-commentary-container').extract()
        # print(all_div_quotes)
								


        # for quote in response.selector.xpath('//div[@id="main"]').get():
        #    print(quote)

        #      pass           # print(quote)
        # titile=response.xpath('//title/text()').getall()

        # all_div_quotes = response.css('.root').getall()
        # print(titile)
        # print(res)

        # for div in all_div_quotes:
        #    print(div)
    # json_object = quote.extract()
        # # print('demo: %s' % quote) """
    # # print(json.dumps(json_object, indent=3))
    # url = quote.css('a::attr(href)').extract()
    # print(f"/company/audienceplus'{url[0]}")
    # print(f"remote-jobs,{url[1]}")
    # urlJob = url[1]

    # book_url = self.base_url + urlJob
    # spaceUrl = book_url.replace(" ", "")

    # yield scrapy.Request(spaceUrl, callback=self.parse_book)
