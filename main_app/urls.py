from django.contrib import admin
from django.urls import path
from .views import *


# app_nam='clinic'
urlpatterns = [
    path('index/',MainView.as_view(),name='main'),
    path('clinics/', ClinicView.as_view(), name='cliniclist'),
    path('desc/<int:id>/', description,name='description'),
    path('desc_doctor/<int:id>/', description_doctor,name='description_doctor'),
    path("ajaxify_rating/",ajaxify_rating),
    path("ajaxify_rating_doctor/",ajaxify_rating_doctor),
    path("",home,name='home'),
    path('doctors/', DoctorView.as_view(), name='doctors'),

    # path('post/<int:id>/', description, name='add_comment_to_post'),
]