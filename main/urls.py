from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse, reverse_lazy
from django.contrib.auth import views
from . import views as main_views
from .views import (BlogUpdateView,BlogDeleteView, BlogCreateView, SignupPageView)

urlpatterns = [
    path('', main_views.home, name='home'),
    path('pay/', main_views.mpay, name='pay'),
    path('receipt/', main_views.receipt, name='receipt'),
    path('clb/', main_views.handle_callback, name='callback'),
    path('logout/', main_views.logout_user, name='logout'),
    path('accounts/profile/', main_views.profile, name='Profile'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('detail/<int:id>/', main_views.post, name='post_details'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

