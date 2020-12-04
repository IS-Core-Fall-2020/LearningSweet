from django.db import models
from datetime import datetime, timedelta

from django.contrib.auth.models import User

# Create your models here.


class UserPic(models.Model) :
    photo_main = models.ImageField(upload_to='photos')
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Group(models.Model) :

    group_name = models.CharField(max_length=30)
    group_description = models.CharField(max_length=100)
    user = models.ManyToManyField(User)
    

    def __str__(self) :
        return (self.group_name)

    class Meta :
        db_table = 'groups'


class Assignment(models.Model) :

    assign_name = models.CharField(max_length=30)
    assign_description = models.CharField(max_length=250)
    assign_completion = models.BooleanField()
    assign_duedate = models.DateField(default=datetime.today, blank=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return(self.assign_name)

    class Meta :
        db_table = 'assignments'
