from django.db import models

# Create your models here.
class Artiste(models.Model):
    '''Creates the Artiste table'''
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Song(models.Model):
    '''Initializes the Song table'''
    title = models.CharField(max_length=128)
    date_released = models.DateField()
    likes = models.IntegerField()     
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class Lyric(models.Model):
    '''Initializes the lyric table'''
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.content) > 50:
            return f"{self.content[0:50]}..."
        else:
            return f"{self.content}" 