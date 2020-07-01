from django.contrib import admin
from Webapp.models import Message

# Register your models here.


# Change Admin Title and Header
admin.site.site_title = "DB"
admin.site.site_header = "Nutrition Platform DataBase"
admin.site.index_title = "DB page-Welcome!"


# Register your models after describing them.
class MessageList(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')

admin.site.register(Message, MessageList)

