from django.contrib import admin
from .models import WishCamp, PersonalInfo
# Register your models here.
class InfoInline(admin.TabularInline):
	model = PersonalInfo

class WishCampAdmin(admin.ModelAdmin):
	inlines = [InfoInline]


admin.site.register(WishCamp, WishCampAdmin)