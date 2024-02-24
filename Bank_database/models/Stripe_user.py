from django.db import models
from django.conf import settings


class UserPayment(models.Model):
    app_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default = False)
    stripe_checkout_id = models.CharField(max_length = 500)


