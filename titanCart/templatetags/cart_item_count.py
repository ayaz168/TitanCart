from django import template
from titanCart.models import Cart

register=template.Library()

@register.filter
def cart_items(user):
    if user.is_authenticated:
        qs=Cart.objects.filter(user=user,ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
