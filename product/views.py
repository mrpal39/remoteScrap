from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
from django.core.management import call_command


def get_product_name_modile(request):
    
    if request.method == 'GET':
        # data=request.POST['search']
        # c = RequestContext(request.POST, {
        response=call_command('amzone_product')

        print(response)


    return render(request, 'homepage.html')



def get_product(request):
    
    if request.method == 'GET':
        # data=request.POST['search']
        # c = RequestContext(request.POST, {
        response=call_command('product_single_job')

        print(response)


    return render(request, 'homepage.html')