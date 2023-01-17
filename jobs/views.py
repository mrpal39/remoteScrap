from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
from django.core.management import call_command
from .models import Jobs

def page_view(request):

    if request.method == 'POST':
        # c = RequestContext(request.POST, {
        response=call_command('scrape_all_job')

        print(response)


    return render(request, 'homepage.html')




def get_by_tag(request):
    
    if request.method == 'POST':
        data=request.POST['search']
        # c = RequestContext(request.POST, {
        response=call_command('scrape_job_from_tags',data)

        print(response)


    return render(request, 'homepage.html')





def get_emal(request):
    
    if request.method == 'GET':
        response=call_command('scrape_email_job')

        print(response)


    return render(request, 'homepage.html')