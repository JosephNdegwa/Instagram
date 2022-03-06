from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views 

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('signup/', views.signup, name="signup"),
    path('', include('django.contrib.auth.urls')),
    path('profile/<user_id>', views.profile, name="profile"),
    path('post/<post>', views.post, name="post"),
    path('search/', views.search_results, name="search_results"),
    path('follow/', views.profile_follow, name='follow'),
    path('unfollow/', views.profile_unfollow, name='unfollow'),
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
