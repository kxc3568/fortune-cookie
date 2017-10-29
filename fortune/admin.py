from django.contrib import admin
from .models import Fortune
# Register your models here.
class FortuneAdmin(admin.ModelAdmin):
	list_display = ('message', 'emotions')
	search_fields = ('message', )

admin.site.register(Fortune, FortuneAdmin)