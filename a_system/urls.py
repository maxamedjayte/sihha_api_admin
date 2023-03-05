from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/',views.adminLoginPage),
    path('logout/',views.adminLogoutPage),

    path('',views.dashboard),

    path('questions_mgn/',views.questionMgn),
    path('adkar_w_talo_mng/',views.adkarWithTaloMgn),
    
    path('listening_quran_cl_mng/',views.listeningQuranClMng),


    # USERS-LIST
    path('users_list/',views.usersList),
    path('user_detail/<str:pk>/',views.userDetail),

    # products
    path('product_create/',views.productCreate),
    path('products_list/',views.productsList),
    
    path('ordered_list/',views.orderedList),
    # path('all-question/',views.allQuestion),

    
    path('all-users/',views.allUsers),
    path('app_info/',views.appInfo),

    # appointnet
    
    path('appointment_list/',views.appointmentList),
    path('appointment_detail/<str:appointId>/',views.appointmentDetail),



]