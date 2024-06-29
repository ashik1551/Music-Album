from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView

from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView

from rest_framework import permissions,authentication

from .serializers import TrackSerializers,AlbumSerialzer,ReviewSerializer,UserSerializer

from .permissions import IsOwner,IsAdminOrReadOnly

from .models import Track,Album,Review,User


class UserView(APIView):

    def post(self,request,*args,**kwargs):

        serializer=UserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data)
        
        else:
            
            return Response(data=serializer.errors)


class UserDetailsView(ListAPIView):

    queryset=User.objects.all()

    serializer_class=UserSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]


class AlbumViewSetView(ModelViewSet):

    queryset=Album.objects.all()

    serializer_class=AlbumSerialzer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsAdminOrReadOnly]

    @action(methods=['POST'],detail=True)
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        album_data=Album.objects.get(id=id)

        serializer=TrackSerializers(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_data)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)


class TrackViewSetView(RetrieveUpdateDestroyAPIView):

    queryset=Track.objects.all()

    serializer_class=TrackSerializers

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsAdminOrReadOnly]


class ReviewAddView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        album_data=Album.objects.get(id=id)

        serializer=ReviewSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_data,user=request.user)

            return Response(data=serializer.data)
        
        else:

            return Response(serializer.errors)


class ReviewViewSetView(RetrieveUpdateDestroyAPIView):

    queryset=Review.objects.all()

    serializer_class=ReviewSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsOwner]