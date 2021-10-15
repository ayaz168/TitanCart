from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from .models import Products as Prod, OrderItem,Cart
from .models import Product
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.template import context
from django.contrib import messages
from titanCart.models import OrderSummary, Review, featured, pTags, productReview, recomended, sales, searchCriteria
from .forms import CheckoutForm,ReviewForm, SearchForm
from .email import sendMail
from .makeReciepte import makeOrderTXT
from titanCart.makeReciepte import getOrderString
from titanCart.email import sendAttachMain
from django.http.response import HttpResponseRedirect
import re
# Create your views here.
#My Coding stylr for this projects is one-two app and many models as that seems best for this kind of project.
def products(request):
    context = {
        'items': Prod.objects.all()
    }
    return render(request,"index.html",context)
# Changed From function to class based view for cleaner code
CATEGORYS= (
    ('D', 'Default'),
    ('EL', 'Electronics'),
    ('En', 'Entairtnment'),
    ('H&F', 'Health and Fitness'),
    ('M', 'Mens Clothes'),
    ('W', 'Womens Clothes'),
    ('KC', 'Kids Clothes'),
    ('SE', 'Security'),
    ('W', 'Watches'),
    ('SH', 'Shoes')
)
class HomeView(ListView):
    model = Prod
    paginate_by = 6
    template_name = "index.html"
    def post(self, *args, **kwargs):
        fourm=SearchForm(self.request.POST or None)
        if fourm.is_valid():
            Search_Criteia=fourm.cleaned_data.get('Search_Criteia')
            rx=searchCriteria.objects.create(userID=self.request.user,tag=Search_Criteia)
            rx.save()
            return redirect("titanCart:search")
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)
        fourm=SearchForm
        ##Checking review Code Working
        review1=productReview.objects.filter(prodId=2)
        print("Review Start")       
        abc=review1[0].reviewList.all()
        for x in abc:
            print(x.UserReview)
        context['Sform']=fourm
        context['featured'] = featured.objects.all()[0]# No Logic for Featured and recomended decided yet so giving it test data as of yet
        context['recomended'] = recomended.objects.all()[0]
        return context
class ProductDetailedView(DetailView):
    #messages.info(self.request,'You will Recieve A confirmation Email Soon.') # After payment module it will redirect to that
    model = Prod
    template_name = "product-detail.html"
    def post(self, *args, **kwargs):
        fourm=ReviewForm(self.request.POST or None)
        pX=self.get_object()
        print(pX)
        if fourm.is_valid():
            ReviewX=fourm.cleaned_data.get('Review')
            RatingsX=fourm.cleaned_data.get('Ratings')
            if int(RatingsX)>=0 and int(RatingsX)<=5:
                r3=Review.objects.create(user=self.request.user,UserReview=ReviewX,ratingGiven=int(RatingsX))
                if not productReview.objects.filter(prodId=pX):
                    r2=productReview.objects.create(prodId=pX)
                else:
                    r2=productReview.objects.filter(prodId=pX)
                    r2=r2[0]
                r2.reviewList.add(r3)
                r2.save()
                messages.info(self.request,'Thank You For Your Input.')
                return HttpResponseRedirect(self.request.path_info)
            else:
                messages.info(self.request,'Invalid Rating.Try Again, Please.')
                return HttpResponseRedirect(self.request.path_info)
    def get_context_data(self, **kwargs):
        context = super(ProductDetailedView, self).get_context_data(**kwargs)
        fourm=ReviewForm
        ##Getting reviews
        pX=self.get_object()
        review1=productReview.objects.filter(prodId=pX)
        if review1:  
            reviewsX=review1[0].reviewList.all()
            context['rReviews']=reviewsX
        context['rform']=fourm
        return context
#functions based view for catagories
def renderElectronics(request):
    context={
        'Title':"Electronics",
        'obj':Prod.objects.filter(category='EL'),
        'featured' : featured.objects.all()[0],
        'recomended' : recomended.objects.all()[0]
        }  
    return render(request,'catindex.html',context)
def renderEntairtnment(request):
    context={
        'Title':"Entairtnment",
        'obj':Prod.objects.filter(category='En'),
        'featured' : featured.objects.all()[0],
        'recomended' : recomended.objects.all()[0]
        }  
    return render(request,'catindex.html',context)
def renderHealth_and_Fitness(request):
    context={
        'Title':"Health and Fitness",
        'obj':Prod.objects.filter(category='H&F'),
        'featured' : featured.objects.all()[0],
        'recomended' : recomended.objects.all()[0]
        }  
    return render(request,'catindex.html',context)
def rendermensClothes(request):
    context={
        'Title':"Men's Clothes",
        'obj':Prod.objects.filter(category='M'),
        'featured' : featured.objects.all()[0],
        'recomended' : recomended.objects.all()[0]
        }  
    return render(request,'catindex.html',context)
def renderwomensClothes(request):
    context={
        'Title':"Women's Clothes",
        'obj':Prod.objects.filter(category='W'),
        'featured' : featured.objects.all()[0],
        'recomended' : recomended.objects.all()[0]
        }
    return render(request,'catindex.html',context)
def renderkidClothes(request):
    context={
        'Title':"Kid's Clothes",
        'obj':Prod.objects.filter(category='KC'),
        'featured' : featured.objects.all()[0],
        'recomended' : recomended.objects.all()[0]
        }  
    return render(request,'catindex.html',context)
def renderSecurity(request):
    context={
        'Title':"Security",
        'obj':Prod.objects.filter(category='SE'),
        'featured' : featured.objects.all()[0],
        'recomended' : recomended.objects.all()[0]
        }  
    return render(request,'catindex.html',context)
def renderWatches(request):
    context={
        'Title':"Watches",
        'obj':Prod.objects.filter(category='WA'),
        'featured' : featured.objects.all()[0],
        'recomended' : recomended.objects.all()[0]
        }  
    return render(request,'catindex.html',context)
def renderShoes(request):
    context={
        'Title':"Shoes",
        'obj':Prod.objects.filter(category='SH'),
        'featured' : featured.objects.all()[0],
        'recomended' : recomended.objects.all()[0]
        }  
    return render(request,'catindex.html',context)
def getSearcgItems(criteria):
    tag=pTags.objects.filter(tag=criteria)
    sResult=[]
    for x in tag:
        sResult.append(x.prodId)
    print(sResult)
    return sResult
def renderSearchResults(request):
    serach=searchCriteria.objects.filter(userID=request.user)
    criteria=serach[0].tag
    print(criteria)
    context={
        'Title':"Result",
        'obj':getSearcgItems(criteria),
        'featured' : featured.objects.all()[0],
        'recomended' : recomended.objects.all()[0]
        }
    print("Here1")
    print(criteria) 
    searchCriteria.objects.filter(userID=request.user).delete()
    return render(request,'catindex.html',context)

class CartView(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        try:
            cart=Cart.objects.get(user=self.request.user,ordered=False)
            context = {
                'object': cart
            }
            return render(self.request,'cart.html',context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")
@login_required
def initCart(request,slug):  
    if request.user.is_authenticated:
        print("hehrere")
        product=get_object_or_404(Prod,slug=slug)#gets a particular product
        order_item,created=OrderItem.objects.get_or_create(item=product,user=request.user,ordered=False) #created added as tupple is returned
        cart_set=Cart.objects.filter(user=request.user,ordered=False)
        if cart_set.exists():
            cart=cart_set[0]
            if cart.items.filter(item__slug=product.slug).exists():
                if order_item.quantity<5:
                    order_item.quantity+=1
                    order_item.save()
                    messages.info(request,"Cart Updated.")
                else:
                    messages.info(request,"Quantity Limit for One Order reached.")
            else:
                cart.items.add(order_item)
                messages.info(request,"Item Added.")
            return redirect("/",slug=slug)
        else:
            date=timezone.now()
            cart=Cart.objects.create(user=request.user,ordered_date=date)
            cart.items.add(order_item)
            messages.info(request,"Item Added.")
            return redirect("/",slug=slug)
    else:
        messages.info(request,"Please Login and Try Again.")
        return redirect("/",slug=slug)
@login_required
def alterCart(request,slug):#deletes item from cart just delete for now
    product=get_object_or_404(Prod,slug=slug)#gets a particular product
    cart_set=Cart.objects.filter(user=request.user,ordered=False)#get the order
    if cart_set.exists():
        cart=cart_set[0]
        if cart.items.filter(item__slug=product.slug).exists():#checks if product is in the order
            order_item=OrderItem.objects.filter(item=product,user=request.user,ordered=False)[0]
            cart.items.remove(order_item)
            messages.info(request,"Done.!!!")
            return redirect("titanCart:cart-view")
        else:
            messages.info(request,"Item Doesn't Exist In Cart!!!")
            return redirect("titanCart:cart-view")
    else:
        #Order Doesnt Exists
        messages.info(request,"Order Doesnt Exists!!!")
        return redirect("titanCart:cart-view")
@login_required
def plusCart(request,slug):#deletes item from cart 
    product=get_object_or_404(Prod,slug=slug)#gets a particular product
    cart_set=Cart.objects.filter(user=request.user,ordered=False)#get the order
    if cart_set.exists():
        cart=cart_set[0]
        if cart.items.filter(item__slug=product.slug).exists():#checks if product is in the order
            order_item=OrderItem.objects.filter(item=product,user=request.user,ordered=False)[0]
            if order_item.quantity<5:
                order_item.quantity+=1
                order_item.save()
                messages.info(request,"Cart Updated")
                return redirect("titanCart:cart-view")
            else:
                messages.info(request,"Quantity Limit for One Order Reached")
                return redirect("titanCart:cart-view")
    else:
        #Wont happen unnecessary condition
        messages.info(request,"Order Doesnt Exists!!!")
        return redirect("titanCart:cart-view")
@login_required
def minusCart(request,slug):#deletes single item from cart 
    product=get_object_or_404(Prod,slug=slug)#gets a particular product
    cart_set=Cart.objects.filter(user=request.user,ordered=False)#get the order
    if cart_set.exists():
        cart=cart_set[0]
        if cart.items.filter(item__slug=product.slug).exists():#checks if product is in the order
            order_item=OrderItem.objects.filter(item=product,user=request.user,ordered=False)[0]
            if order_item.quantity>1:
                order_item.quantity-=1
                order_item.save()
                messages.info(request,"Cart Updated")
                return redirect("titanCart:cart-view")
            else:
                cart.items.remove(order_item)
                messages.info(request,"Done.!!!")
                return redirect("titanCart:cart-view")
    else:
        #Wont happen unnecessary condition
        messages.info(request,"Order Doesnt Exists!!!")
        return redirect("titanCart:cart-view")
class myOrder(View):
    def get(self, *args, **kwargs):
        cart_set=Cart.objects.filter(user=self.request.user,ordered=True,Delivered=False)#get the order
        if cart_set.exists():
            context={
                'orders':cart_set,
            }
            return render(self.request,'myOrder.html',context)
        else:
                messages.info(self.request,'No Order') 
                return redirect("/")

class CheckoutView(View):
    def get(self, *args, **kwargs):
        fourm=CheckoutForm
        context={
            'form':fourm,
        }

        return render(self.request,'checkout.html',context)     
    def checkData(self,Shipping_Name,Shipping_Country,First_Name,Last_Name,Zip,Phone,Alt_Phone):
        sName_error=not(re.search(r'\d+', Shipping_Name) is None)
        sCountry_error=not(re.search(r'\d+', Shipping_Country) is None)
        sFName_error=not(re.search(r'\d+', First_Name) is None)
        sLName_error=not(re.search(r'\d+', Last_Name) is None)
        zip_error=not(Zip.isdigit())
        phone_error =re.search(r"^03\d{9}$|^00923\d{9}$|^[+]923\d{9}", Phone) is None
        altphone_error=re.search(r"^03\d{9}$|^00923\d{9}$|^[+]923\d{9}", Alt_Phone) is None
        if  sName_error or sCountry_error or sFName_error or sLName_error or zip_error or phone_error or altphone_error:
            return False #returns false if invalid
        return True
    def getError(self,Shipping_Name,Shipping_Country,First_Name,Last_Name,Zip,Phone,Alt_Phone):
        sName_error=not(re.search(r'\d+', Shipping_Name) is None)
        sCountry_error=not(re.search(r'\d+', Shipping_Country) is None)
        sFName_error=not(re.search(r'\d+', First_Name) is None)
        sLName_error=not(re.search(r'\d+', Last_Name) is None)
        zip_error=not(Zip.isdigit())
        phone_error =re.search(r"^03\d{9}$|^00923\d{9}$|^[+]923\d{9}", Phone) is None
        altphone_error=re.search(r"^03\d{9}$|^00923\d{9}$|^[+]923\d{9}", Alt_Phone) is None
        Message="Invalid Entry : "
        if sName_error:
            Message+=', Wrong Shipping Name. No digits allowed '
        if sCountry_error:
            Message+=', Wrong Country Name. No digits allowed  '
        if sFName_error:
            Message+=', Wrong First Name. No digits allowed '
        if sLName_error:
            Message+=', Wrong Last Name. No digits allowed  '
        if zip_error:
            Message+=', Wrong Zip Code. Only digits allowed '
        if phone_error:
            Message+=', Wrong Phone. Use(03xxxxxxxxx or 00923xxxxxxxxx or +923xxxxxxxxx) '
        if altphone_error:
            Message+=', Wrong Alt Phone Format '
        Message=list(Message)
        if Message[16]==',':
            print("abx")
            Message[16]=''
        return ''.join(Message)
    def post(self, *args, **kwargs):
        fourm=CheckoutForm(self.request.POST or None)
        try:
            cart=Cart.objects.get(user=self.request.user,ordered=False)
            if fourm.is_valid():
                Shipping_Name =fourm.cleaned_data.get('Shipping_Name')
                Shipping_Country =fourm.cleaned_data.get('Shipping_Country')
                Title = fourm.cleaned_data.get('Title')
                First_Name = fourm.cleaned_data.get('First_Name')
                Last_Name = fourm.cleaned_data.get('Last_Name')
                Shipping_Address = fourm.cleaned_data.get('Shipping_Address')
                Shipping_Address_b = fourm.cleaned_data.get('Shipping_Address_b')
                Zip = fourm.cleaned_data.get('Zip')
                Phone = fourm.cleaned_data.get('Phone')
                Alt_Phone = fourm.cleaned_data.get('Alt_Phone')
                Same_Billing_Address = fourm.cleaned_data.get('Same_Billing_Address')
                Shipping_Note=fourm.cleaned_data.get('Shipping_Note')
                payment_option = fourm.cleaned_data.get('payment_option')
                if Shipping_Country !=  "Pakistan":
                        Shipping_Country="Pakistan"
                if self.checkData(Shipping_Name,Shipping_Country,First_Name,Last_Name,Zip,Phone,Alt_Phone):
                    orderSummary=OrderSummary(
                        user=self.request.user,
                        Shipping_Name=Shipping_Name,
                        Shipping_Country=Shipping_Country,
                        Title=Title,
                        First_Name=First_Name,
                        Last_Name=Last_Name,
                        Shipping_Address=Shipping_Address,
                        Shipping_Address_b=Shipping_Address_b,
                        Zip=Zip,
                        Phone=Phone,
                        Alt_Phone=Alt_Phone,
                        ShippingNote=Shipping_Note
                    )
                    orderSummary.save() #saves billing info
                    cart.OrderSummary=orderSummary #links current user info from django form to the order he placed
                    cart.ordered_date=timezone.now()
                    cart.save()
                    orderId="PP00X12"
                    orderId+=str(cart.id)
                    Name=cart.user.username
                    iList=cart.items.all()
                    TotalPrice=cart.delivered_price()               
                    if payment_option=='S':
                        #makeOrderTXT(orderId,Name,TotalPrice,iList,orderSummary,True)
                        #dataString=getOrderString(orderId)
                        #sendAttachMain(orderId,dataString)
                        saleX=sales(
                            user=self.request.user,
                            item=cart,
                            date=timezone.now()
                        )
                        saleX.save()
                        return redirect("titanCart:payment",payment_option='stripe')
                    elif payment_option=='J':
                        messages.info(self.request,'AccountId:014567893, Name:TitanCart. Please pay and you will recieve confirmation email')
                        makeOrderTXT(orderId,Name,TotalPrice,iList,orderSummary,True)
                        dataString=getOrderString(orderId)
                        #sendMail(orderId,dataString)
                        sendAttachMain(orderId,dataString)
                        cart.ordered=True
                        saleX=sales(
                            user=self.request.user,
                            item=cart,
                            date=timezone.now()
                        )
                        saleX.save()
                        ##Reducing Inventory By item
                        for i in iList:
                            x=Prod.objects.filter(ProductId=i.item.ProductId)
                            if x[0].Qty>=i.quantity:
                                x[0].Qty-=i.quantity
                            cart.save()
                        return redirect("/")
                    elif payment_option=="C":
                        messages.info(self.request,'You will Recieve A confirmation Email Soon.') # After payment module it will redirect to that
                        makeOrderTXT(orderId,Name,TotalPrice,iList,orderSummary,False)
                        dataString=getOrderString(orderId)
                        sendAttachMain(orderId,dataString)
                        cart.ordered=True
                        saleX=sales(
                            user=self.request.user,
                            item=cart,
                            date=timezone.now()
                        )
                        saleX.save()
                        ##Reducing Inventory By item
                        for i in iList:
                            x=Prod.objects.filter(ProductId=i.item.ProductId)
                            if x[0].Qty>=i.quantity:
                                x[0].Qty-=i.quantity
                        cart.save()
                        return redirect("/")
                    else:
                        messages.info(self.request,'Invalid') # After payment module it will redirect to that
                        return redirect("/")
                else:
                    errorX=self.getError(Shipping_Name,Shipping_Country,First_Name,Last_Name,Zip,Phone,Alt_Phone)
                    messages.info(self.request,errorX)
                    return redirect("titanCart:checkout")
        except ObjectDoesNotExist:
            messages.info(self.request,'Checkout Failed!')
            return redirect("titanCart:checkout")

class PaymentView(View):
    def get(self, *args, **kwargs):
        return render(self.request,"payment.html")
    def post(self, *args, **kwargs):
          pass;
