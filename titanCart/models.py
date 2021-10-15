from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

##Unused
class Country:
    CountryCode: int
    Country_Name: str


class Person:
    PersonId: int
    FirstName: str
    LastName: str
    CellNo: str
    Address: str
    City: str
    CountryCode: int


class PayOp:
    PayOpId: int
    PayOpId: str


class CustomerInfo:
    CustId: int
    CustEmail: str
    CustPass: str
    PayOpId: int
    PersonId: int

#used
class Colour(models.Model):
    ColId = models.AutoField(primary_key=True)
    colourdesc = models.CharField(max_length=50)


class Product:
    Desi: str
    Price: int
    Img: str

# Catagories would be managed by a Tupple as no need for a differnt table for it.


CATEGORYS= (
    ('D', 'Default'),
    ('EL', 'Electronics'),
    ('En', 'Entairtnment'),
    ('H&F', 'Health and Fitness'),
    ('M', 'Mens Clothes'),
    ('W', 'Womens Clothes'),
    ('KC', 'Kids Clothes'),
    ('SE', 'Security'),
    ('WA', 'Watches'),
    ('SH', 'Shoes')
)
ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Products(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductTitle = models.CharField(max_length=50)
    ColId = models.ForeignKey('Colour', on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORYS, max_length=4)
    Qty = models.IntegerField(default=0)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.FloatField(blank=True, null=True)
    Img = models.ImageField(upload_to='pics')
    Manufacturer = models.CharField(max_length=50)
    Desc = models.TextField()
    slug=models.SlugField()
    def __str__(self):
        return self.ProductTitle
    def get_absolute_url(self):
        return reverse("titanCart:product-detail",kwargs={
            'slug':self.slug
        })
    def add_to_cart_url(self):
        return reverse("titanCart:add-to-cart",kwargs={
            'slug':self.slug
        })
    def remove_from_cart_url(self):
        return reverse("titanCart:remove-from-cart",kwargs={
        'slug':self.slug
    })
    
class OrderItem(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} of {self.item.ProductTitle}"
    def setItem(self,Products):
        self.item=Products
    def total_item_price(self):
        return self.quantity * self.item.Price
    def discount_price(self):
        return self.quantity * self.item.discount_price
    def saved_price(self):
        return  float(self.total_item_price())-self.discount_price()
    def get_price(self):
        if self.item.discount_price:
            return  self.discount_price()
        return self.total_item_price()
class Cart(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    delivery = models.FloatField(default=10, null=True)
    OrderSummary = models.ForeignKey(
        'OrderSummary', on_delete=models.SET_NULL, blank=True, null=True)
    Delivered=models.BooleanField(default=False)
    def get_total_price(self):
        sum = 0.0
        for products in self.items.all():
            sum += float(products.get_price())
        return sum
    def get_Delivery(self):
        return self.delivery
    def delivered_price(self):
        return self.get_total_price()+self.get_Delivery()
class featured(models.Model):
    productIDs = models.ManyToManyField(Products)
class recomended(models.Model):
    productIDs = models.ManyToManyField(Products)
class OrderSummary(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Shipping_Name=models.CharField(max_length=50,blank=True, null=True)
    Shipping_Country=models.CharField(max_length=50,blank=True, null=True)
    Title=models.CharField(max_length=50,blank=True, null=True)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Shipping_Address=models.CharField(max_length=50)
    Shipping_Address_b=models.CharField(max_length=50,blank=True, null=True)
    Zip=models.CharField(max_length=50,blank=True, null=True)
    Phone=models.CharField(max_length=50)
    Alt_Phone=models.CharField(max_length=50)
    ShippingNote=models.CharField(max_length=50,blank=True, null=True)
    def __str__(self):
        return self.user.username
class Review(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    UserReview=models.CharField(max_length=100)
    ratingGiven=models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
class productReview(models.Model):
    reviewId = models.AutoField(primary_key=True)
    prodId = models.ForeignKey('Products', on_delete=models.CASCADE)
    reviewList = models.ManyToManyField(Review)
class pTags(models.Model):
    tagId = models.AutoField(primary_key=True)
    tag=models.CharField(max_length=100)
    prodId = models.ForeignKey('Products', on_delete=models.CASCADE)
class searchCriteria(models.Model):
    userID=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    tag=models.CharField(max_length=100)
class sales(models.Model):
    SalesId = models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)