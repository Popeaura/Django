from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=50)
    text = models.TextField()

    sent_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"(slef.sender): {self.text[:30]}"