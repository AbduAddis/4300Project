from django.urls import path
from . import views 


urlpatterns = [
    path('',views.loginPage,name="home"),
    path('contact/',views.contact,name="contact" ),
    path('customer/<str:pk>/',views.customer,name="customerpage"),
    path('company/<str:pk>/',views.company,name="companypage"),
    path('create_order/<str:pk>',views.createOrder,name="create_order"),
    path('update_order/<str:pk>',views.updateOrder,name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    path('create_customer/<str:pk>',views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>',views.updateCustomer,name="update_customer"),
    path('delete_customer/<str:pk>',views.deleteCustomer,name="delete_customer"),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('profile/',views.profilePage,name="profile"),
    path('logout/',views.logoutUser,name="logout"),
    path('create_company',views.createCompany,name="create_company"),
    path('about',views.aboutPage,name="about")
]   