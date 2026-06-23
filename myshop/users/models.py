from __future__ import annotations

from django.conf import settings
from django.db import models, transaction


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="addresses",
    )
    label = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=120, default="Ukraine")
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_default", "label", "-created_at"]

    def __str__(self) -> str:
        return f"{self.label} for {self.user}"

    def save(self, *args, **kwargs) -> None:
        with transaction.atomic():
            if not self.pk and not self.user.addresses.exists():
                self.is_default = True
            super().save(*args, **kwargs)
            if self.is_default:
                (
                    self.user.addresses.exclude(pk=self.pk)
                    .filter(is_default=True)
                    .update(is_default=False)
                )
