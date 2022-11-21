from django.db import models


class Verification(models.Model):
    email = models.CharField(max_length=100)
    hash_key = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        if self.status:
            return f"{self.email} Verified"
        else:
            return f"{self.email} NOT VERIFIED"


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

