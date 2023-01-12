from django.urls import include, path
from .views import (
    LoginView,
    RegisterView,
    logout_view,
    MyTicketView,
    MyTickeDetailView,
)

urlpatterns = [
    path("ingresar", LoginView.as_view(), name="login"),
    path("salir", logout_view, name="logout_view"),
    path("registrar", RegisterView.as_view(), name="register"),
    path("mis-compras", MyTicketView.as_view(), name="my_tickets"),
    path(
        "mis-compras/<int:pk>/",
        MyTickeDetailView.as_view(),
        name="my_tickets_detail",
    ),
]
