from csk.views import *
from django.urls import path
app_name='something'
#urls
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('mahindra/',mahindra,name='mahindra'),
    path('mahi/',mahi,name='mahi'),
    path('deva/',deva,name='deva')
]