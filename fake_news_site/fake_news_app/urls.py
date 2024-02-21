from django.urls import path
from .views import *


urlpatterns = [
    path('news/', retriever_function, name='retriever_function'),
    path('news/<str:id>', detail_function, name='detail_function')
]