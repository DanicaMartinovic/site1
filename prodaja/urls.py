from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name='index'),
    path('home/', views.home,name='home'),
    path('shop/', views.shop, name='shop'),
    path('o_nama/', views.o_nama, name='o_nama'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('search/', views.search, name='search'),
    path('shop/voce/', views.voce, name='voce'),
    path('shop/povrce/', views.povrce, name='povrce'),
   
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

