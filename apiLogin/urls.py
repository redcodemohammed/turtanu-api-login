from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.hello.as_view(), name='hello')
]
