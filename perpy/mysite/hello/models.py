from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=50)
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.text[:20]}"
