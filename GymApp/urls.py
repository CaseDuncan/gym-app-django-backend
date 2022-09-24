from django.urls import path
from GymApp import views

urlpatterns = [
    path('api/customers/', views.customer_list),
    path('api/customers/<str:pk>/', views.customers_details),
    path('api/services/', views.services_list),
    path('api/services/<str:pk>/', views.service_detail)

]