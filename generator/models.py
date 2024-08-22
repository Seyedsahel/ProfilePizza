from django.db import models

class Record(models.Model):
    username = models.CharField(max_length=200)
    count = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.username
    
    def inc_count(self):
        self.count = self.count + 1
