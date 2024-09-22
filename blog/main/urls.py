from django.urls import path
from .views import index, about, detail, reg, auth,logout, panel

urlpatterns = [
    path('', index),
    path('about', about),
    path('detailt/<int:id>', detail),
    path('reg', reg),
    path('auth', auth),
    path('logout', logout),
    path('panel', panel)
]