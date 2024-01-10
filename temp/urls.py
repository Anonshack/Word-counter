from django.contrib import admin
from django.urls import path
from .views import counter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('counter', counter, name='counter'),
]
