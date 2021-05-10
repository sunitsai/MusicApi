from music.viewsets import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register('song',SongViewset)
router.register('podcast',PodcastViewset)
router.register('audiobook',AudioBookViewset)



