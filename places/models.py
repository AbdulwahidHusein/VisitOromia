from django.db import models

class VisitablePlace(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    region = models.CharField(max_length=255)
    zone = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=255)


    def __str__(self):
        return self.name

#a post made for a particular place
 
class PlacePosts(models.model):
    place = models.ForeignKey(VisitablePlace, on_delete=models.CASCADE)
    text = models.TextField()
    photo = models.ImageField(upload_to=f'places/posts/photos', null=True, blank=True)
    video = models.FileField(upload_to='places/posts/videos', null=True, blank=True)
    