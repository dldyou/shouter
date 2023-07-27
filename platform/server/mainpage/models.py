from django.db import models

# Create your models here.
class UploadedFile(models.Model):
    title = models.TextField(max_length=40, null=True)
    file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title