from django.db import models

# Create your models here.
class Cusslist(models.Model):
    id = models.AutoField(primary_key=True)
    cussword = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['cussword']

    def __str__(self):
        return "Cusslist"

    