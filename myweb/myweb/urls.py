from django.urls import path
from viewer.views import rental, homepage, reservation, checkout, end, order
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/<int:property_id>/', reservation, name='reservation'),
    path('checkout/<int:property_id>/', checkout, name='checkout'),
    path('order/<int:order_id>/', order, name='order'),
    path('end/', end, name='end'),
    path('<str:category>/', rental, name='rental'),
    path('', homepage, name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

