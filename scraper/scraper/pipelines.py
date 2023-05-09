# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from quotes.models import Quotes
from jobs.models import Jobs

import logging
import coloredlogs
logger = logging.getLogger(__name__)
coloredlogs.install(level="WARN", logger=logger)


class ScraperPipeline:

    def process_item(self, item_tag, spider):
        print(item_tag)
        try:
            Quotes.objects.create(text=item_tag['text'])
            print("\n")
            logger.warn("Loaded quote {}".format(item_tag['text']))
            print(item_tag)
        except Exception as e:
            print("\n")
            logger.error(
                "\nFailed to load quote, Reason For Failure:{}".format(e))
            print(item_tag)
        return item_tag


class ScraperJobPipeline:

    def process_item(self, item, spider):
        # print(item)
        try:
            Jobs.objects.create(
             
                job_title=item['job_title'],
                job_description=item['job_description'],
                company_logo=item['company_logo'],
                company_website=item['company_website'],
                company_name=item['company_name'],
                company_email=item['company_email'],
                company_url=item['company_url'],
                job_country=item['job_country'],
                job_state=item['job_state'],
                job_zip_code=item['job_zip_code'],
                job_city=item['job_city'],
                job_address=item['job_address'],
                category=item['category'],
                type=item['type'],
                wpjobboard_am_data=item['wpjobboard_am_data'],
                company_country=item['company_country'],
                company_state=item['company_state'],
                company_zip_code=item['company_zip_code'],
                company_location=item['company_location'],

                )



                
            print("\n")
            logger.warn("Loaded quote {}".format(item['text']))
            print(item)
        except Exception as e:
            print("\n")
            logger.error(
                "\nFailed to load quote, Reason For Failure:{}".format(e))
            print(item)
        return item
