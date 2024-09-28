from django.contrib import admin
from .models import teacher
# Register your models here.

class teacherAdmin(admin.ModelAdmin):
    list_display=['username','mobile_no','eduction',]

    def username(self,obj):
        return f'{obj.user.username}'
admin.site.register(teacher,teacherAdmin)