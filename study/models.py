from django.db import models

class study1(models.Model):
    study_name = models.CharField(max_length=100)
    study_phase = models.CharField(max_length=100)
    sponsor_name = models.CharField(max_length=100)
    study_description = models.TextField()
    
    def __str__(self):
        return self.study_name
