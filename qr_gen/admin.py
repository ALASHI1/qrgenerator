from django.contrib import admin
from .models import *
# Register your models here.
 
 
admin.site.register(Qrcode)
@admin.register(Qrfilecode)
class QrfilecodeAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug') 

@admin.register(Qraudiocode)
class QraudiocodeAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug') 

@admin.register(Qrpdfcode)
class QrpdfcodeAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug') 