from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('reg', reg),
    path('auth', auth),
    path('panel', panel),
    path('logout', logout),
    path('edit_user_data', edit_user_data),
    path('editavatat', editavatat),
    path('addnew', addnew),
    path('news', news),
    path('new/<int:id>', newid),
    path('like/<int:id>', like),
]
