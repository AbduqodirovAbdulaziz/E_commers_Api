from django.db import models


class Yangilik(models.Model):
    sarlavha = models.CharField(max_length=255)
    batafsil = models.TextField()
    rasm = models.ImageField(upload_to='yangiliklar/')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.sarlavha
