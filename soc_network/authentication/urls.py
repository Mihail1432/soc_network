from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register
from . import views
from django.conf import settings  # Добавьте этот импорт
from django.conf.urls.static import static  # Добавьте этот импорт
from authentication.views import profile_view, profile_edit, user_profile_view




urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/<str:username>/', user_profile_view, name='profile'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)