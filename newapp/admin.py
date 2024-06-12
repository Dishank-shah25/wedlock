from django.contrib import admin
from .views import submit
# Register your models here.
class showsubmit(admin.ModelAdmin):
    list_display = ['email','password','repassword','person_select','firstname','lastname','gender','fgender','religion','language']
admin.site.register(submit,showsubmit)