from django.db import models


# Upload file API
class FileModel(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='upload')    # store the file at /upload/ folder





