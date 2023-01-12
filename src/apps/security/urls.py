from django.urls import include, path
from .views import (
    HomeView,
)

urlpatterns = [
    path("home2", HomeView.as_view(), name="home"),
]
