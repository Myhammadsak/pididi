from django.db import models

class Feedback(models.Model):

    user = models.CharField(max_length=32)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.message}'