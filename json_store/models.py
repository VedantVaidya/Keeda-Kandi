from django.db import models

class WifiJson(models.Model):
    name=models.CharField(max_length=100)
    data=models.TextField()

    class Meta:
        db_table="WifiJson"