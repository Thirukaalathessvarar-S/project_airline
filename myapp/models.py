from django.db import models


class user_data(models.Model):
    user_name=models.CharField(max_length=40)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.user_name