from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    FormView,
    CreateView,
    ListView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from apps.orders.models import Order

# Create your views here.
class LoginView(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("events:events")

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password"),
        )
        if user is not None:
            login(self.request, user)
        next_page = self.request.GET.get("next")
        if next_page:
            return redirect(next_page)
        return redirect(reverse_lazy("security:home"))


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:login")
    success_message = "se ha registrado exitosamente"


def logout_view(request):
    logout(request)
    return redirect("events:events")


class MyTicketView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "my-tickets.html"
    login_url = reverse_lazy("events:events")

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .select_related("event")
            .order_by("-created_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_order"] = self.get_queryset().count()
        return context


class MyTickeDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "my-tickets-detail.html"
    login_url = reverse_lazy("events:events")

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_order"] = self.get_queryset().count()
        context["details"] = self.get_object().order_users.all()
        return context
