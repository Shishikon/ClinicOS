from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('book-app', book_app, name='book_app'),

]
