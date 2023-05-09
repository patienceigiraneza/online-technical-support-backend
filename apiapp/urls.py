from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', views.fn_registration),
    # path('login/', obtain_auth_token),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('category/', views.fn_category),
    path('conversation/', views.fn_conversation),
    path('conversation/<int:id>/', views.fn_view_conversation),
    path('message/', views.ViewAllMesseges.as_view() ),
    path('message/<int:id>/', views.ViewOneMessage.as_view()),
    path('subcategory/', views.fn_subcategory),
    path('subcategory/<int:id>/', views.fn_view_one_subcategory),


    path('supporter/', views.fn_supporter),



]
