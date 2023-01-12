from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import Events

# Create your views here.


class EventsView(ListView):
    model = Events
    queryset = Events.objects.all()
    template_name = "home.html"


class EventDetailView(DetailView):
    model = Events
    queryset = Events.objects.all()
    template_name = "event_detail.html"
    slug_field = "url"
    slug_url_kwarg = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        max_tickets = (
            self.get_object().num_tickets
            if self.get_object().num_tickets < 5
            else 5
        )
        max_tickets = range(1, max_tickets + 1)
        context["max_tickets"] = max_tickets
        return context

    def post(self, request, *args, **kwargs):
        tickets = request.POST.get("tickets")
        request.session["tickets"] = tickets
        request.session["event_id"] = self.get_object().id
        return redirect("orders:checkout")
