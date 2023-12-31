from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentification/',include('authentification.urls')),
    path('dashboard/',include('dashboard_settings.urls')),
    path('articles/',include('article.urls')),
]
