from django.db import models

# Create your models here.

class Link(models.Model):
    # wikipedia, discogs, streaming services (Spotify, Tidal, Apple ...)
    class Type(models.TextChoices):
        WIKIPEDIA = 'wikipedia', 'Wikipedia'
        SPOTIFY = 'spotify', 'Spotify'
        # FIXME!

    label = models.CharField(max_length=200, choices=Type.choices)
    url = models.URLField()

    class Meta:
        abstract = True
    

class Artist(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class ArtistLink(Link):
    artist = models.ForeignKey(Artist, related_name="links", on_delete=models.CASCADE)


class Record(models.Model):
    artist = models.ManyToManyField(Artist, related_name="records")
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class RecordLink(Link):
    record = models.ForeignKey(Record, related_name="links", on_delete=models.CASCADE)