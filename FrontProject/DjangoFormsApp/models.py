from django.db import models


class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=12)

    def __str__(self):
        return self.name + "- "+str(self.email)



