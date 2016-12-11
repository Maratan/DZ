from django.contrib import admin

# Register your models here.
from .models import Tovar

# Register your models here.
class TovarAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'cout')
    list_filter = ('user',)

admin.site.register(Tovar, TovarAdmin)
