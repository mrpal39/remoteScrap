"""djscrapyquotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trade.views import *
from jobs import views as jobsView
from product import views as ProductView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobsView.get_by_tag, name='get_by_tag'),
    path('scrap/', jobsView.page_view, name='scrap'),
    # path('product/', ProductView.get_product, name='get_product'),
    # path('email/', jobsView.get_emal, name='get_emal'),
    # path('trade/', get_trade_data, name='get_emal'),

    # path('aws/', ProductView.get_product, name='get_product_name_modile'),
    # path('aws/', ProductView.get_product_name_modile, name='get_product_name_modile'),

    path('remoteco/', jobsView.remoteCoGetData, name='remoteCoGetData'),


    
    

]
urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        )