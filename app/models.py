from django.db import models

# Create your models here.


class Imagekit(models.Model):
    file_url = models.URLField(verbose_name="File URL")

    def __str__(self):
        return str(self.id)
