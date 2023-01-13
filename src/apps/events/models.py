from django.db import models
from django.db.models import Sum
from django.utils.text import slugify

# Create your models here.
class Events(models.Model):
    name = models.CharField("Nombre", max_length=255)
    description = models.TextField("Description", blank=True)
    is_published = models.BooleanField("Esta publicado?", default=False)
    date_start = models.DateTimeField("Fecha de Inicio")
    address = models.CharField("Dirección", max_length=255)
    num_tickets = models.IntegerField("Numero de entradas")
    is_delete = models.BooleanField(default=False)
    banner = models.ImageField("Banner", upload_to="banner/")
    cover = models.ImageField(
        "Imagen Representativa", upload_to="cover/", help_text="360x220"
    )
    url = models.SlugField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super().save(*args, **kwargs)

    def total_tickets(self):
        tickets_by_orders = self.orders.all().aggregate(
            total_tickets=Sum("num_tickets")
        )
        total_tickets = 0
        if tickets_by_orders:
            total_tickets = tickets_by_orders.get("total_tickets")
        return int(total_tickets)

    def __str__(self):
        return self.name
