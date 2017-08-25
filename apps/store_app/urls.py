from django.conf.urls import url
from .views import StoreIndex, CartUpdate, CartShow

urlpatterns = [
    url(r'^cart/show$', CartShow.as_view(), name='cart-show'),
    url(r'^cart/update$', CartUpdate.as_view(), name='cart-update'),
    url(r'^$', StoreIndex.as_view(), name='store-index'),
]