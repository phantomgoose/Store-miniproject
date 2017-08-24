from django.conf.urls import url
from .views import StoreIndex

urlpatterns = [
    url(r'^$', StoreIndex.as_view(), name='store-index'),
]