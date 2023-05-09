from django.core.management import BaseCommand
from scrapy import cmdline

import os
from pathlib import Path

class Command(BaseCommand):

    help = "Scrape the tags from specific author"

    def add_arguments(self, parser):
           parser.add_argument('author_name',
                                type=str, help="Name of the author, parts of name separated by '-'")

    # def add_arguments(self, parser):
    #     parser.add_argument('total', type=int,
    #                         help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        django_path = Path(__file__).resolve().parent.parent.parent.parent
        os.chdir(str(django_path)+"/scraper/")
        os.system(
            "scrapy crawl quotes -a author='{}' -L WARN".format(kwargs['author_name']))
