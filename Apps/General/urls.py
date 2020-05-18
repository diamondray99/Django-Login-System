from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('register/', RegisterView.as_view(), name='RegisterView'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', DashboardView.as_view(), name='DashboardView'),
    path('profile/', ProfileView.as_view(), name='ProfileView'),
    path('profile_update/', ProfileUpdateView.as_view(), name='ProfileUpdateView'),
    path('index/', index, name='index'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
