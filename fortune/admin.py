from django.contrib import admin
from .models import Fortune
# Register your models here.
class FortuneAdmin(admin.ModelAdmin):
	list_display = ('fortune', )
	search_fields = ('fortune', )

admin.site.register(Fortune, FortuneAdmin)