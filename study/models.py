from django.db import models

# Create your models here.
class Study(models.Model):
    study_name = models.CharField(max_length=255)
    STUDY_PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ]
    study_phase = models.CharField(max_length=50, choices=STUDY_PHASE_CHOICES)
    sponsor_name = models.CharField(max_length=255)
    study_description = models.TextField()

    def __str__(self):
        return f'Study: {self.study_name} ({self.study_phase})'