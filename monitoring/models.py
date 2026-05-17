from django.db import models

class StatusEntry(models.Model):
    name = models.CharField(max_length=180)
    status = models.CharField(max_length=128)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.status}"
