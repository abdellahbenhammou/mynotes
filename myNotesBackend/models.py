from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    note = models.TextField()
    tags = models.TextField()
    date = models.DateTimeField('date published')
    user = models.ForeignKey(User,null=True, blank=True)



# Create your models here.
