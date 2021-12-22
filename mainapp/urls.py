from django.urls import path

from mainapp.views import mainpage

app_name = 'mainapp'

urlpatterns =[
    path('main/',mainpage,name='mainpage')
]