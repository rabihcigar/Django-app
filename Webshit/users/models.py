from django.db import models
from django.contrib.auth.models import User

#CASCADE mean if user deleteted, also delete the profile, if the profile delete it wont delete the user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'   
