from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    names = models.CharField(max_length=50)
    lastnames = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        return super().save(*args, **kwargs)

    def check_user_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
