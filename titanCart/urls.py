from django.urls import path
from . import views
from titanCart.views import CartView, CheckoutView, HomeView, PaymentView, ProductDetailedView, alterCart, initCart, minusCart, myOrder, plusCart
from django.conf.urls import include
app_name = 'titanCart'
urlpatterns = [
    path('', HomeView.as_view(),name="index"),
    path('catElectronicsindex', views.renderElectronics,name='catElectronicsindex'),
    path('catEntairtnmentindex', views.renderEntairtnment,name='catEntairtnmentindex'),
    path('catHealthandFitnessindex', views.renderHealth_and_Fitness,name='catHealthandFitnessindex'),
    path('catMens_Clothesindex', views.rendermensClothes,name='catMens_Clothesindex'),
    path('catWomens_Clothesindex', views.renderwomensClothes,name='catWomens_Clothesindex'),
    path('catKids_Clothesindex', views.renderkidClothes,name='catKids_Clothesindex'),
    path('catSecurityindex', views.renderSecurity,name='catSecurityindex'),
    path('catWatchesindex', views.renderWatches,name='catWatchesindex'),
    path('catShoesindex', views.renderShoes,name='catShoesindex'),
    path('search', views.renderSearchResults,name='search'),
    path('cart-view',CartView.as_view(),name='cart-view'),
    path('checkout',CheckoutView.as_view(),name='checkout'),
    path('product-detail/<slug>',ProductDetailedView.as_view(),name='product-detail'),
    path('payment/<payment_option>',PaymentView.as_view(),name='payment'),
    path('myOrders',myOrder.as_view(),name='myOrders'),
    path('add-to-cart/<slug>',initCart,name='add-to-cart'),
    path('remove-from-cart/<slug>',alterCart,name='remove-from-cart'),
    path('increment-quantity/<slug>',plusCart,name='increment-quantity'),
    path('decrement-quantity/<slug>',minusCart,name='decrement-quantity'),
    path('^accounts/', include('accounts.urls'))
] 