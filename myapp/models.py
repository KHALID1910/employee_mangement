from django.db import models

# Create your models here.
class User(models.Model):
    uid=models.CharField(max_length=25)
    uname=models.CharField(max_length=50)
    uemail=models.EmailField()
    ucontact=models.CharField(max_length=20)

    class Meta:
        db_table="user"


class URLS(models.Model):
    urlid=models.TextField()
    url=models.TextField()

    class Meta:
        db_table="urls"