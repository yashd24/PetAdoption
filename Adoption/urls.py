from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.user_login, name='login'),
    path('add/', views.add, name='add'),
    path('logout/', views.user_logout, name='logout'),
    path('delete/<str:animalid>', views.delete, name='delete'),
    path('update/<str:animalid>', views.update, name='update'),
    path('detail/<int:animalid>', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
