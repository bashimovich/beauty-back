from django.contrib import admin
from .models import *
from django.utils.html import format_html, mark_safe, format_html_join
from django.contrib import admin
from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline








class WebImageInline(GenericStackedInline):
    model = WebImage

class MobileImageInline(GenericStackedInline):
    model = MobileImage

class CompanyAdmin(admin.ModelAdmin):
    list_display = ( "get_images", "name", )
    inlines = (WebImageInline, MobileImageInline, )
    def get_images(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.web_images.all()))
   
class WorkersAdmin(admin.ModelAdmin):
    list_display = ("get_images", "name", )
    inlines = (WebImageInline, MobileImageInline, )
    def get_images(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.web_images.all()))

class ServicesAdmin(admin.ModelAdmin):
    list_display = ("get_images", "name", )
    inlines = (WebImageInline, MobileImageInline, )
    def get_images(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.web_images.all()))

class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "company","service", 'time')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Workers, WorkersAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Order, OrderAdmin)