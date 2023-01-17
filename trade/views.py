from django.shortcuts import render
from django.core.management import BaseCommand
from scrapy import cmdline
from http.client import HTTPResponse

# Create your views here.
from django.core.management import call_command
from pathlib import Path

# Create your views here.

def get_trade_data(request):

    if request.method == 'GET':
        # c = RequestContext(request.POST, {
        call_command('scrape_all_trade')
    return render(request, 'homepage.html')

