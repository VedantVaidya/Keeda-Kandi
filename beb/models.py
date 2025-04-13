from django.db import models


class MyJSON(models.Model):
    data=models.JSONField()
    key=models.CharField(max_length=20, null=True, blank=True, default=None)

    class Meta:
        db_table="MyJSON"
    