from django.db import models

# Create your models here.

CLASSES=[
    ('FIVE','FIVE'),
    ('SIX','SIX'),
    ('SEVEN','SEVEN'),
    ('EIGHT','EIGHT'),

]

DAYS=[
    ('2 days',2),
    ('5 days',5),
    ('6 days',6),

]

class tution(models.Model):
    claSS=models.CharField(choices=CLASSES,max_length=12)
    claSS_slug=models.SlugField(max_length=12)
    salary=models.IntegerField()
    day_perweek=models.CharField(choices=DAYS,max_length=13)
    avilable=models.BooleanField(default=True)
    subject=models.CharField(max_length=100,null=True)
    tution_duration=models.CharField(max_length=40,null=True)
    no_of_student=models.IntegerField(null=True)

    def __str__(self):
        return f'{self.id}'
    class Meta:
        ordering=['-id']