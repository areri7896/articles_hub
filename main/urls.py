"""
URL configuration for articles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse, reverse_lazy
from django.contrib.auth import views
from . import views as main_views
from .views import (BlogUpdateView,BlogDeleteView, BlogCreateView)

urlpatterns = [
    path('', main_views.home, name='home'),
    path('logout/', main_views.logout_user, name='logout'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('detail/<int:id>/', main_views.post, name='post_details'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




#  [
#    accounts/login/ [name='login'],
#    accounts/logout/ [name='logout'],
#    accounts/password_change/ [name='password_change'],
#    accounts/password_change/done/ [name='password_change_done'],
#    accounts/password_reset/ [name='password_reset'],
#    accounts/password_reset/done/ [name='password_reset_done'],
#    accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm'],
#    accounts/reset/done/ [name='password_reset_complete'],
# ]