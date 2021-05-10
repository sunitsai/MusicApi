from django.urls import path,include
from . views import AudioView

urlpatterns = [
    path("audio", AudioView.as_view()),
    path("audio/<str:audioFileType>", AudioView.as_view()),
    path("audio/<str:audioFileType>/<int:audioFileID>", AudioView.as_view())
]
