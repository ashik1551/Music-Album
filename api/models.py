from django.db import models

from django.db.models import Avg

from django.core.validators import MinValueValidator,MaxValueValidator

from django.contrib.auth.models import User

class Album(models.Model):

    title=models.CharField(max_length=200)

    year=models.IntegerField()

    director=models.CharField(max_length=200)

    language=models.CharField(max_length=200)

    @property
    def track_count(self):

        return Track.objects.filter(album=self).count()
        # return self.track_set.all().count()
    
    @property
    def tracks(self):

        return Track.objects.filter(album=self).order_by('track_num')
    
    @property
    def review_count(self):

        return Review.objects.filter(album=self).count()
    
    @property
    def review_average(self):

        return Review.objects.filter(album=self).values('rating').aggregate(average=Avg('rating'))['average']

    @property
    def reviews(self):

        return Review.objects.filter(album=self)

    def __str__(self):
        return self.title

class Track(models.Model):

    title=models.CharField(max_length=200)

    singers=models.CharField(max_length=300)

    genre=models.CharField(max_length=200)

    duration=models.CharField(max_length=200)

    track_num=models.IntegerField()

    album=models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):

    comment=models.CharField(max_length=300)

    rating=models.FloatField(validators=[
                            MinValueValidator(1),
                            MaxValueValidator(5)
                            ])
    
    album=models.ForeignKey(Album,on_delete=models.CASCADE)

    user=models.ForeignKey(User,on_delete=models.CASCADE)