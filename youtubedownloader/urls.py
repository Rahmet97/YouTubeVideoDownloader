from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="url"),
    path('download/<res>', views.download)
]
