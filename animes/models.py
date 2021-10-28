from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=200)
    img = models.TextField(null=True)
    mal_id = models.CharField(max_length=50)


    def __str__(self):
        #ID. TITULO
        return f'{self.id}. {self.title}'
