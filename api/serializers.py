from rest_framework import serializers

from .models import Album,Track,Review,User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:

        model=User

        fields=['id','username','email','password']

        read_only_fields=['id']

    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)

class TrackSerializers(serializers.ModelSerializer):

    album=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Track

        fields="__all__"

        read_only_fields=['id','album']

class ReviewSerializer(serializers.ModelSerializer):

    album=serializers.StringRelatedField(read_only=True)

    user=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Review

        fields="__all__"

        read_only_fields=['id','user']

class AlbumSerialzer(serializers.ModelSerializer):

    track_count=serializers.IntegerField(read_only=True)

    tracks=TrackSerializers(many=True,read_only=True)

    review_count=serializers.IntegerField(read_only=True)

    review_average=serializers.FloatField(read_only=True)

    reviews=ReviewSerializer(many=True,read_only=True)

    class Meta:

        model=Album

        fields="__all__"

        read_only_fields=['id']
