from django.db import models

# Create your models here.


class Song(models.Model):
    Name = models.CharField(max_length=100)
    SongDuration = models.DurationField()
    UploadTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name


class Podcast(models.Model):
    Name = models.CharField(max_length=100)
    Duration = models.DurationField()
    UploadTime = models.DateTimeField(auto_now_add=True)
    Host = models.CharField(max_length=100)
    Participants = models.CharField(max_length=100)

    
    def __str__(self):
        return self.Name

class AudioBook(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Narrator = models.CharField(max_length=100)
    Duration = models.DurationField()
    UploadTime = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.Title