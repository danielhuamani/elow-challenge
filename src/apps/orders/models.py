from django.db import models


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        "events.Events", related_name="orders", on_delete=models.CASCADE
    )
    num_tickets = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="orders", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order"

    def num_order(self):
        return str(self.id).zfill(5)

    def __str__(self):
        return self.event.name


class OrderUsers(models.Model):
    TYPE_DOCUMENTS_CHOICES = (("DNI", "DNI"), ("CE", "CE"))

    order = models.ForeignKey(
        "Order", related_name="order_users", on_delete=models.CASCADE
    )
    email = models.EmailField("Email")
    first_name = models.CharField("Nombres", max_length=120)
    last_name = models.CharField("Apellidos", max_length=120)
    document = models.CharField("Documento", max_length=255)
    type_document = models.CharField(
        "Tipo de documento", max_length=255, choices=TYPE_DOCUMENTS_CHOICES
    )

    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Info"

    def __str__(self):
        return self.first_name
