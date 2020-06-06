from django.contrib import admin
from .models import *

# TODO you need to install packages in the requirements.txt file


# TODO you can view this using python manage.py runserver in your terminal
#  make sure you have CD into the memorial directory after you must have
#  installed all the packages in the requirements.txt file
# Register your models here.
admin.site.register(Contact)
admin.site.register(ConDetails)
admin.site.register(Memorial)