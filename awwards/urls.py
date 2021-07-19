from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
