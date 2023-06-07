from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
from django.core.management import call_command
from .models import Jobs
from quotes.models import Quotes
def page_view(request):
    ra = Quotes.objects.all()

    if request.method == 'POST':
        for a in ra:
             
        # a = 'categories/remote-devops-sysadmin-jobs'

            response = call_command('scrape_all_job', a)

        # print(response)
            pass

         
       
    return render(request, 'homepage.html')




def get_by_tag(request):

    
    if request.method == 'POST':
        data=request.POST['search']
        # c = RequestContext(request.POST, {
        response=call_command('scrape_job_from_tags',data)
        return render(request, 'homepage.html', )

        
    else:


        context = {'name': 'John', 'age': 30}
        return render(request, 'homepage.html', context=context)



def get_emal(request):
    
    if request.method == 'GET':
        response=call_command('scrape_email_job')



    return render(request, 'homepage.html')