from django.urls import include, path
from .views import EventsView, EventDetailView

urlpatterns = [
    path("", EventsView.as_view(), name="events"),
    path(
        "eventos/<slug:url>/'", EventDetailView.as_view(), name="event_detail"
    ),
]
