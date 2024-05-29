from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register((StudentProfile,Course,CourseSchedule,StudentRegistration,Notification))