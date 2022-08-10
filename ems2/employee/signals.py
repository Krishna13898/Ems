from django.db.models.signals import post_save
from django.contrib.auth.models import User

from . models import Manager

def createManager(sender,instance,created,**kwargs):
    
    if created:
        user = instance
        manager = Manager.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=instance.first_name,
            last_name = instance.last_name,
        )


post_save.connect(createManager,sender=User)