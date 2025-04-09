from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.accounts.models.user import User
from django.db.models import Sum



class CartModel(AbstractBaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="carts"
    )
    total_price = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        default=0.00
    )
    
    def __str__(self):
        return self.user.first_name
    
        
    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "cart"
        verbose_name = _("CartModel")
        verbose_name_plural = _("CartModels")


class CartitemModel(AbstractBaseModel):
    cart = models.ForeignKey(
        CartModel,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )
    book = models.ForeignKey(
        'havasbook.BookModel',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveBigIntegerField(_("Mahsulot soni"), default=1)
    total_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00
    )
    

    def __str__(self):
        return self.book.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "cartItem"
        verbose_name = _("CartitemModel")
        verbose_name_plural = _("CartitemModels")
