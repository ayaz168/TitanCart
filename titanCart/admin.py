from django.contrib import admin

#Username (leave blank to use 'ayazp'): titanCart
#Email address: master@xyz.abc
#pass=rootroot
# Register your models here.


from .models import Products
from .models import Colour
from titanCart.models import Cart, OrderItem, OrderSummary, Review, featured, pTags, productReview, recomended, sales, searchCriteria

class SnippetAdmin(admin.ModelAdmin):
    list_display=('ProductId','ProductTitle','Qty','Price')
    list_filter=('Qty','Manufacturer')
class SnippetAdmin2(admin.ModelAdmin):
    list_display=('user','item','date')
    list_filter=('date','item')


admin.site.site_header='Titan Cart Admin Page'
admin.site.register(Colour)
admin.site.register(OrderItem)
admin.site.register(featured)
admin.site.register(recomended)
admin.site.register(Cart)
admin.site.register(Products,SnippetAdmin)
admin.site.register(OrderSummary)
admin.site.register(Review)
admin.site.register(productReview)
admin.site.register(pTags)
admin.site.register(sales,SnippetAdmin2)