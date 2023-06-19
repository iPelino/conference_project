from django.urls import path, re_path
from .views import (
    speakerList,
    createSpeakers,
    viewSpeaker,
    speakerUpdate,
    speakerDelete,
)

urlpatterns = [
    path("", speakerList),
    path("create/", createSpeakers),
    path("create/", createSpeakers),
    path("<int:id>/", viewSpeaker),
    path("<int:id>/update/", speakerUpdate),
    path("<int:id>/delete/", speakerDelete),
]
