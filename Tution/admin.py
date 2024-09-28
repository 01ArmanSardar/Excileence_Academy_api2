from django.contrib import admin
from .models import tution
# Register your models here.

class tutionAdmin(admin.ModelAdmin):
    list_display=['claSS','salary','day_perweek',]
    prepopulated_fields={'claSS_slug':('claSS',),}

admin.site.register(tution,tutionAdmin)

