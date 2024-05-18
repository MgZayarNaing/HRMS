from django.contrib import admin
from django.urls import path, include
# from .views import home

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('accounts.urls')),
#     path('', home, name='home'),
#     path('', include('django.contrib.auth.urls')), 
# ]
from .views import register, user_login, user_logout, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', HomeView.as_view(), name='home'),  # HomeView defined here
]
