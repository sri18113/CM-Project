#urls.py
from django.contrib import admin  
from myApp import views  
from django.urls import path
 
urlpatterns = [
    path('', views.home_page, name='home_page'),
    
    path('cable_matrix/', views.cb_home, name='cb_home'),
    path('cable_matrix/form/', views.cb_static_form, name='cb_static_form'),
    path('cable_matrix/submit_form/', views.submit_cb_static_form, name='submit_cb_static_form'),
    path('cable_matrix/delete_form/', views.delete_cb_form, name='delete_cb_form'),
    path('cable_matrix/form/<int:pk>/edit/', views.edit_cb_static_form, name='edit_cb_static_form'),
    path('cable_matrix/device/<int:pk>/', views.device_detail, name='device_detail'),
    
    path('cable_matrix/dcs_request', views.dcs_request, name='dcs_request'),
    path('cable_matrix/dcs_requests/<int:pk>/edit/', views.edit_dcs_request, name='edit_dcs_request'),
    path('cable_matrix/dcs_requests_/<int:pk>/edit/', views.edit_dcs_request_copy, name='edit_dcs_request_copy'),
    
    path('cable_matrix/cable_trace', views.cable_trace, name='cable_trace'),
    path('cable_matrix/cable_trace/<int:pk>/edit/', views.edit_cable_trace, name='edit_cable_trace'),
    path('cable_matrix/cable_trace_/<int:pk>/edit/', views.edit_cable_trace_copy, name='edit_cable_trace_copy'),

    path('cable_matrix/network_design', views.network_design, name='network_design'),
    path('cable_matrix/network_design/<int:pk>/edit/', views.edit_network_design, name='edit_network_design'),
    path('cable_matrix/network_design_/<int:pk>/edit/', views.edit_network_design_copy, name='edit_network_design_copy'),

    path('cable_matrix/cm', views.cm, name='cm'),
    path('cable_matrix/cm/<int:pk>/edit/', views.edit_cm, name='edit_cm'),
    path('cable_matrix/cm_/<int:pk>/edit/', views.edit_cm_copy, name='edit_cm_copy'),

    path('cable_matrix/dis', views.dis, name='dis'),
    path('cable_matrix/dis/<int:pk>/edit/', views.edit_dis, name='edit_dis'),
    path('cable_matrix/dis_/<int:pk>/edit/', views.edit_dis_copy, name='edit_dis_copy'),

    path('cable_matrix/port_assign', views.port_assign, name='port_assign'),
    path('cable_matrix/port_assign/<int:pk>/edit/', views.edit_port_assign, name='edit_port_assign'),
    path('cable_matrix/port_assign_/<int:pk>/edit/', views.edit_port_assign_copy, name='edit_port_assign_copy'),

    path('cable_matrix/cable_measurement', views.cable_measurement, name='cable_measurement'),
    path('cable_matrix/cable_measurement/<int:pk>/edit/', views.edit_cable_measurement, name='edit_cable_measurement'),
    path('cable_matrix/cable_measurement/<int:pk>/edit/', views.edit_port_assign_copy, name='edit_cable_measurement'),
    
]

# urlpatterns = [
#     path('', views.home_page, name='home_page'),
#     path('cable_matrix/', views.cb_home, name='cb_home'),
#     path('dcs_request/', views.dcs_request, name='dcs_request'),
#     path('cable_trace/', views.cable_trace, name='cable_trace'),
#     path('static_form/', views.submit_cb_static_form, name='cb_static_form'),
#     path('cable_matrix/delete_form/', views.delete_cb_form, name='delete_cb_form'),
#     path('cable_matrix/form/<int:pk>/edit/', views.edit_cb_static_form, name='edit_cb_static_form'),
#     path('cable_matrix/device/<int:pk>/', views.device_detail, name='device_detail'),
#     # Add other URL patterns here
    
#     path('cable_matrix/dcs_request', views.dcs_request, name='dcs_request'),
#     path('dcs_requests/<int:pk>/edit/', views.edit_dcs_request, name='edit_dcs_request'),
#     path('dcs_requests_/<int:pk>/edit/', views.edit_dcs_request_copy, name='edit_dcs_request_copy'),
#     # path('dcs_requests/<int:pk>/edit/', views.edit_dcs_request_from_details, name='edit_dcs_request_from_details'),
# ]

