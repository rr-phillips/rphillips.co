from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="blog_index"),
]
