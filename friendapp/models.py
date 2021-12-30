from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Friend(models.Model):
    friend = 1
    A_Request_B = 2
    B_Request_A = 3

    friend_A = models.ForeignKey(User, related_name='friend_A',on_delete=models.CASCADE)
    friend_B = models.ForeignKey(User, related_name='friend_B',on_delete=models.CASCADE)
    friend_status = models.IntegerField()

    def __str__(self):
        return '%s and %s friendship'%(self.friend_A,self.friend_B)

    class Meta:
        unique_together = ['friend_A', 'friend_B']