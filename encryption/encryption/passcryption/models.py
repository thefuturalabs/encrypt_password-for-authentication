from django.db import models

class user_login(models.Model):
  name = models.CharField(max_length=255,unique=True)
  email = models.EmailField()
  password = models.CharField(max_length=2500)
  status=models.BooleanField(default=False)


