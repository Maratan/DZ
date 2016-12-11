from django.conf.urls import url

from .views import products, create_product, add_trash, del_trash

urlpatterns = [
    url(r'^product', products, name='Tovar'),
    url(r'^create_product$', create_product, name='create_product'),
    url(r'^add/(?P<tovar_id>\d+)$', add_trash, name='add'),
    url(r'^del/(?P<tovar_id>\d+)$', del_trash, name='del'),
]