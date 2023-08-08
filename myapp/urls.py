from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loader, name="load"),
    path('contact', views.contact, name="contact"),
    path('home', views.home, name="home"),
    path('course', views.course, name="course"),
    path('upload', views.upload, name="upload"),
    path('show', views.show, name="show"),
    path('logandsin', views.logandsin, name="logandsin"),
    path('index', views.index, name="index"),
    path('cart', views.cart, name="cart"),
    path('adding', views.adding, name="adding"),
    path('addin', views.addin, name="adding"),
    path('logi', views.logi, name="logi"),
    path('sign', views.sign, name="sign"),
    path('logou', views.logou, name="logou"),
    path('verifypay',views.verifypay,name='verifypay'),
    path('paid',views.paid,name='paid'),
    path('learning',views.learning,name='learning'),
    path('dash',views.dash,name='dash'),
    path('eleventh',views.celeven,name='eleventh'),
    path('twelveth',views.ctwelve,name='twelveth'),
    path('fetch',views.fetch,name='fetch'),
    path('remove',views.remove,name='remove'),
    path('learning-12',views.learn,name='learning-12'),
    path('dpdf',views.dpdf,name='dpdf'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)