from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView
from apps.events.models import Events
from django.forms.models import inlineformset_factory
from .models import Order, OrderUsers
from .forms import OrderForm

# Create your views here.


class OrderView(TemplateView):
    template_name = "checkout.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not Events.objects.filter(
            id=request.session.get("event_id"),
            is_delete=False,
            is_published=True,
        ).exists():
            return redirect("events:events")
        event = get_object_or_404(Events, id=request.session.get("event_id"))
        tickets = request.session.get("tickets")
        if not (event.total_tickets() > tickets):
            messages.success(
                self.request,
                "En estos momentos no contamos con los tickets que solicita",
            )
            return redirect("events:events")
        OrderUsersInlineForm = inlineformset_factory(
            Order,
            OrderUsers,
            fields=[
                "email",
                "first_name",
                "last_name",
                "type_document",
                "document",
            ],
            can_delete=False,
            min_num=int(tickets),
            extra=0,
        )
        context["form"] = OrderForm(instance=Order())
        context["orderUsersInlineForm"] = OrderUsersInlineForm(
            instance=Order()
        )
        context["event"] = event
        context["tickets"] = tickets
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        event = get_object_or_404(Events, id=request.session.get("event_id"))
        tickets = request.session.get("tickets")
        form = OrderForm(
            {
                "event": event,
                "num_tickets": int(tickets),
                "user": request.user,
            },
            instance=Order(),
        )
        OrderUsersInlineForm = inlineformset_factory(
            Order,
            OrderUsers,
            fields=[
                "email",
                "first_name",
                "last_name",
                "type_document",
                "document",
            ],
            can_delete=False,
            min_num=int(tickets),
            extra=0,
        )
        orderInlineForm = OrderUsersInlineForm(request.POST, instance=Order())
        if not (event.total_tickets() > tickets):
            messages.success(
                self.request,
                "En estos momentos no contamos con los tickets que solicita",
            )
            return redirect("events:events")
        if orderInlineForm.is_valid() and form.is_valid():
            instance = form.save()
            orderInlineForm.instance = instance
            orderInlineForm.save()
            request.session["order_id"] = instance.id
            return redirect(reverse("order:thanks"))
        else:
            context["event"] = event
            context["tickets"] = tickets
            context["form"] = form
            context["orderUsersInlineForm"] = orderInlineForm
            return self.render_to_response(context)


class OrderThanksView(TemplateView):
    template_name = "thanks.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not Order.objects.filter(
            id=request.session.get("order_id")
        ).exists():
            return redirect(reverse("events:events"))
        order = get_object_or_404(Order, id=request.session.get("order_id"))
        context["order"] = order
        del request.session["order_id"]
        del request.session["tickets"]
        del request.session["event_id"]
        return self.render_to_response(context)
