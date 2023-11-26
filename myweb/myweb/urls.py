from django.urls import path
from viewer.views import rental,homepage, reservation
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', reservation, name='reservation'),
    path('<str:category>/', rental, name='rental'),
    path('', homepage, name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




