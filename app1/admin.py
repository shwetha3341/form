from django.contrib import admin

from app1.models import Access_Records, Webpage
from app1.models import *
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Access_Records)
