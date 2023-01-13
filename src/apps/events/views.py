from django.db.models import Sum
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import Events

# Create your views here.


class EventsView(ListView):
    model = Events
    queryset = Events.objects.filter(is_published=True, is_delete=False)
    template_name = "home.html"


class EventDetailView(DetailView):
    model = Events
    queryset = Events.objects.filter(is_published=True, is_delete=False)
    template_name = "event_detail.html"
    slug_field = "url"
    slug_url_kwarg = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        allowed_tickets = (
            self.get_object().num_tickets - self.get_object().total_tickets()
        )
        max_tickets = allowed_tickets if allowed_tickets < 5 else 5
        context["total_tickets"] = max_tickets
        max_tickets = range(1, max_tickets + 1)
        context["max_tickets"] = max_tickets
        return context

    def post(self, request, *args, **kwargs):
        tickets = request.POST.get("tickets")
        request.session["tickets"] = tickets
        request.session["event_id"] = self.get_object().id
        return redirect("orders:checkout")
