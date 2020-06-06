from django.urls import path
from .views import *

# The site urls
urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name="contact"),
    path('plans', plan, name="plan"),
    path('how_it_works', how, name="how"),
    path('browse-memorial', memorial, name="memorial"),
    path('signup', SignUp.as_view(), name='signup'),
    path('Create_a_memorial_for_your_loved_one', create_memorial, name='create'),



    # 404 handling urls
    path("<anything>/", page404, name='404'),
    path("<anything>/<whatever>", page404_1),
    path("<anything>/<whatever>/<seriously>", page404_2),
    path("<anything>/<whatever>/<seriously>/<i_give_up>", page404_3)
]