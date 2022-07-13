from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Users",blank=True,null=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE, related_name="Groups",blank=True,null=True)

    def __str__(self):
        return str(self.user.first_name)


class Book(models.Model):
    book_name = models.CharField(max_length=100,blank=True,null=True)
    status = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.book_name)