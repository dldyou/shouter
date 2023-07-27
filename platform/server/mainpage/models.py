from django.db import models
from .utils import renameToKey

# Create your models here.
class UploadedFile(models.Model):
    title = models.TextField(max_length=40, null=True)
    file = models.FileField(upload_to=renameToKey)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def key(self):
        return self.file.name.split('.')[0]