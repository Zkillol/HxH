from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pic/')
    description = models.TextField()


    def __str__(self):
        return self.title
