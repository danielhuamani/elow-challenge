from django.urls import include, path
from .views import OrderView, OrderThanksView

urlpatterns = [
    path("comprar/", OrderView.as_view(), name="checkout"),
    path("gracias/", OrderThanksView.as_view(), name="thanks"),
]
