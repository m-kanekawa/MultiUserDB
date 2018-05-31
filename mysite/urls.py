from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
