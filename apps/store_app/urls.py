from django.conf.urls import url
from .views import StoreIndex, CartUpdate, CartShow, CartConfirmCheckout, StoreRemove

urlpatterns = [
    url(r'^cart/show$', CartShow.as_view(), name='cart-show'),
    url(r'^cart/update$', CartUpdate.as_view(), name='cart-update'),
    url(r'^cart/checkout$', CartConfirmCheckout.as_view(), name='cart-confirm-checkout'),
    url(r'^remove/(?P<product_id>\d+)$', StoreRemove.as_view(), name='store-remove'),
    url(r'^$', StoreIndex.as_view(), name='store-index'),
]