from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Friend(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    friends = models.ManyToManyField(User,blank=True,related_name='friends')


class Friend_request(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_user')
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')




