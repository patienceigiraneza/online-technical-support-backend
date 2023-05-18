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
    path('supporter/<int:id>', views.fn_view_one_supporter),
    path('tutorial/', views.fn_article),
    path('tutorial/<int:id>/', views.fn_view_one_article),
    path('get-supporters/<int:id>/', views.fn_list_of_supporters_in_category),
    path('get-subcategory/<int:id>/', views.fn_list_of_subcategory_in_category),


    path('get-conversation/<int:id>/', views.fn_conversation_list),
    path('insert-conversation/', views.fn_insert_conversation),
    path('get-client-id/', views.fn_get_client_id),
    path('get-message-list/<int:id>/', views.fn_get_messages_list),
    path('insert-message/', views.fn_insert_messages_list),
    path('insert-message-admin/', views.fn_insert_messages_list_admin),
    path('check-supporter/', views.fn_check_supporter_if_logged_in),

    # get statistics
    path('number-categories/', views.fn_number_of_category),
    path('number-subcategories/', views.fn_number_of_subcategory),
    path('number-clients/', views.fn_number_of_clients),
    path('number-supporters/', views.fn_number_of_supporters),
    path('my-conversation/', views.fn_number_of_my_conversations),

]
