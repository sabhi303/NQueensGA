from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('log.urls')),
    path('nqueens/',include('nqueen.urls')),
    path('admin/', admin.site.urls),
]
