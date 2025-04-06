from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('content.urls')),
    path('rooms/', include('rooms.urls')),
    path('wellness/', include('wellness.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('comments/', include('comments.urls')),
]
