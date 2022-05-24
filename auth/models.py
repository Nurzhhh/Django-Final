from django.db import models
from django.contrib.auth.models import User
from asyncio.windows_events import NULL
from datetime import datetime

def user_images(instance, filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_file_name = instance.user.username + "-" + date_time + ".jpg"
    return 'profile/{0}/{1}'.format(instance.user.username, saved_file_name)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to=user_images, default=NULL)
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username