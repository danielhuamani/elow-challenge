from django.contrib import admin
from .models import Order, OrderUsers

# Register your models here.


class OrderUsersInline(admin.StackedInline):
    model = OrderUsers
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["get_num_order", "event", "user", "num_tickets"]
    search_fields = [
        "event__name",
        "event__description",
        "user__first_name",
        "user__last_name",
    ]
    inlines = [OrderUsersInline]

    @admin.display(description="Codigo")
    def get_num_order(self, obj):
        return obj.num_order()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("event", "user")


admin.site.register(Order, OrderAdmin)
