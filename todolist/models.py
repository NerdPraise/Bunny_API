from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.id:
            self.name = self.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class UserTask(models.Model):
    STATES_CHOICES = (
        ('TD', 'TO DO'),
        ('DN', 'DONE')
    )
    description = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATES_CHOICES)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
