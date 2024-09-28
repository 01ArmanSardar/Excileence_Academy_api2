from django.db import models
from django.contrib.auth.models import User
# Create your models here.

EDUCATION_TYPE=[
    ('SSC','SSC'),
    ('HSC','HSC'),
    ('HONOURS','HONOURS'),
    ('MASTERS','MASTERS'),

]

class teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date=models.DateField(null=True)
    mobile_no=models.CharField(max_length=12,null=True)
    eduction=models.CharField(choices=EDUCATION_TYPE,null=True,max_length=12)

    def __str__(self):
        return f"{self.user.username}"
