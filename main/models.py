from django.db import models



class Films(models.Model):
    class Meta:
        verbose_name = "фильм"
    title = models.CharField(max_length=50, verbose_name='названия')
    image = models.ImageField(upload_to='')
    director = models.CharField(max_length=50, verbose_name='режиссер')
    rating = models.FloatField(default=0, verbose_name='рейтинг')
    duration = models.FloatField(null=True, verbose_name='длительность')


    def __str__(self):
        return self.title


class Review(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE,related_name='review')
    text = models.TextField()

    def __str__(self):
        return self.text