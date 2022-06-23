from django.urls import path
from .views import Home, Main, Song

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('main', Main.as_view(), name="Main"),
    path('main/song/', Song.as_view(), name="Song"),
    path('main/<str:query>', Main.as_view(), name="Main wirh Query")
]