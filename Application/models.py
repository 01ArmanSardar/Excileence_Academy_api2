from django.db import models
from user.models import teacher
from Tution.models import tution
# Create your models here.
class application(models.Model):
    teachers=models.ForeignKey(teacher, on_delete=models.CASCADE)
    tutions=models.ForeignKey(tution, on_delete=models.CASCADE)
    confirm=models.BooleanField(default=False)
    def __str__(self) :
        return f"{self.id} :{self.teachers.user.username}"
    class Meta:
        unique_together =('teachers','tutions')