from django.db import models

# Create your models here.
class Song(models.Model):
    Name = models.CharField(max_length=100, null=False)
    SongDuration = models.DurationField(null=False)
    UploadTime = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.Name


class Podcast(models.Model):
    Name = models.CharField(max_length=100, null=False)
    Duration = models.DurationField(null=False)
    UploadTime = models.DateTimeField(auto_now_add=True, null=False)
    Host = models.CharField(max_length=100, null=False)
    Participants = models.CharField(max_length=100)

    
    def __str__(self):
        return self.Name

class AudioBook(models.Model):
    Title = models.CharField(max_length=100, null=False)
    Author = models.CharField(max_length=100, null=False)
    Narrator = models.CharField(max_length=100, null=False)
    Duration = models.DurationField(null=False)
    UploadTime = models.DateTimeField(auto_now_add=True, null=False)

    
    def __str__(self):
        return self.Title