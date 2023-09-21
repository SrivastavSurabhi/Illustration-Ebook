from django.contrib import admin
from .models import Response, FormData
# Register your models here.

class ResponseAdmin(admin.ModelAdmin):
    list_display=('unique_id','response_id','genated_content','genated_content','story_text','datetime')

class FormDataAdmin(admin.ModelAdmin):
    list_display=('unique_id','response_id','readers_name','story_format','genre','writing_style','charcter_type','charachter_name','charachter_age','charachter_ethinicity','animal_type','readers_age_group','location','moral','audio_name','datetime')

admin.site.register(Response,ResponseAdmin)
admin.site.register(FormData,FormDataAdmin)