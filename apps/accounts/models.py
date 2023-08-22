from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Level(models.Model):
    #firs-year , second-year , third-year , fourth-year , graduated 
    name = models.CharField(max_length=10)
    #frehsman , sophomore , junior , senior ,postgrad
    nickname = models.CharField(max_length=10)

    def __str__(self) -> str:
        return  self.name




class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=False)
    level= models.ForeignKey(Level,on_delete=models.CASCADE,null=False)

    college_id = models.CharField(max_length=11,primary_key=True)
    report_count = models.IntegerField(default=0)
    section_number = models.CharField(max_length=3,null=True,blank=True)
    is_grad = models.BooleanField(blank=True , null=True)
    #is ,cs ,sc ,sys ,general
    major = models.CharField(max_length=10)
    verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.user.username)




