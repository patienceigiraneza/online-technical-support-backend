from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.fn_registration),
    path('login/', obtain_auth_token),
    path('category/', views.fn_category),
    path('conversation/', views.fn_conversation),
    path('conversation/<int:id>/', views.fn_view_conversation),
    path('subcategory/', views),
   

    
]
