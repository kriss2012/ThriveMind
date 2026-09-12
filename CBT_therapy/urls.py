from django.urls import path, re_path, include  # Updated import
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from CBT import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('depression-test/', views.screen_test, name='screen_test'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Updated for Django 4.x
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Updated for Django 4.x
    path('locate/', views.locate, name='locate'),
    path('CBT_therapy/', views.viewCBT, name='viewCBT'),
    path('Register_for_therapy/', views.registerCBT, name='registerCBT'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Use re_path for URLs with regex
    re_path(r'^session/(\d+)/', views.session, name='session'),
    re_path(r'^draw/(\d+)/', views.draw, name='draw'),
    re_path(r'^sample-draw/(\d+)/', views.sampleDraw, name='sampledraw'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
