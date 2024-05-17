from django.db import models
from  django.utils import timezone
# Create your models here.



class Job(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    company =models.CharField(max_length=1000)
    requirements = models.CharField(max_length=255, blank=True)
    salary = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    job_type = models.CharField(max_length=1000)
    status = models.BooleanField(default=True)
    banner = models.ImageField(upload_to='jobs/', blank=True)

    def __str__(self):
        return self.title


