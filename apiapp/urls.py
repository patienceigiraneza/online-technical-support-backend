from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', views.fn_registration),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('category/', views.fn_category),
    path('category/<int:id>/', views.fn_view_category),
    path('conversation/', views.fn_conversation),
    path('conversation/<int:id>/', views.fn_view_conversation),
    path('message/', views.ViewAllMesseges.as_view() ),
    path('message/<int:id>/', views.ViewOneMessage.as_view()),
    path('subcategory/', views.fn_subcategory),
    path('subcategory/<int:id>/', views.fn_view_one_subcategory),
    path('supporter/', views.fn_supporter),
    path('article/', views.fn_article),
    path('article/<int:id>/', views.fn_view_one_article),

    # get statistics
    path('number-categories/', views.fn_number_of_category),
    path('number-subcategories/', views.fn_number_of_subcategory),
    path('number-clients/', views.fn_number_of_clients),
    path('my-conversation/', views.fn_number_of_my_conversations),

]
