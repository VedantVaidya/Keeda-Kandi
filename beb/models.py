from django.db import models


class MyJSON(models.Model):
    data=models.JSONField()

    class Meta:
        db_table="MyJSON"
    