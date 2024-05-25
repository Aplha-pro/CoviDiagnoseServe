from django.urls import path
from . import views

urlpatterns = [
    path('', views.manager, name='manager'),
    path('upload-image/', views.upload_image, name='upload_image'),
]