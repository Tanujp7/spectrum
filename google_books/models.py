from django.db import models

class SecretKey(models.Model):
    email = models.EmailField(max_length=256, null=True, blank=True)
    secret_key = models.CharField(max_length=256)

    def __str__(self):
        return (self.secret_key)
