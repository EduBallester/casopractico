from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
# Create your models here.

class ClientUser(AbstractBaseUser, PermissionsMixin):
    """Usuarios simulando los clientes"""
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'),max_length=50,default='')
    last_name = models.CharField(_('last name'),max_length=50,default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField()

class Cart(models.Model):
    user = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)