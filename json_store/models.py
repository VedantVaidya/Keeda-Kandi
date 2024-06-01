from django.db import models

class WifiJson(models.Model):
    name=models.CharField(max_length=100)
    data=models.TextField()

    class Meta:
        db_table="WifiJson"
    
    def __str__(self):
        return self.name
    
class WAXpathJson(models.Model):
    username = models.CharField(max_length=100)
    xpaths = models.TextField()

    class Meta:
        db_table="WAXpathJson"
    
    def __str__(self):
        return self.username
    

class WAScriptJson(models.Model):
    username = models.CharField(max_length=100)
    script = models.TextField()

    class Meta:
        db_table="WAScriptJson"
    
    def __str__(self):
        return self.username