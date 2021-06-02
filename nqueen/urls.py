
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('solve', views.solution, name="solution"),
    path('showParents', views.showParent, name="showParents"),
    path('showChild', views.showChild, name="showChild")
]
