

from django.db import models

class Task(models.Model):
    PRIORITY =(
        (1,'High'),
        (2,'Middle'),
        (3,'Low')
    )
    todo = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    priority = models.SmallIntegerField(choices=PRIORITY, default=3)
    is_done =models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo



