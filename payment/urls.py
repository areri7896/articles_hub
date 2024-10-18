from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse, reverse_lazy
from . import views as payment_views

urlpatterns = [
    path('', payment_views.payment, name='payment'),
    path('receipt', payment_views.receipt, name='receipt'),
    # path('logout', payment_views.logout_user, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
