from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()

router.register('albums',views.AlbumViewSetView,basename="albums")

urlpatterns=[

    path('token/',ObtainAuthToken.as_view()),

    path('user/',views.UserView.as_view()),

    path('admin/users/',views.UserDetailsView.as_view()),

    path('tracks/<int:pk>/',views.TrackViewSetView.as_view()),

    path('albums/<int:pk>/add_review/',views.ReviewAddView.as_view()),

    path('reviews/<int:pk>/',views.ReviewViewSetView.as_view()),

]+router.urls