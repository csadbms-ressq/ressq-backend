from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (BloodBankDonorViewSet,DonorViewSet)

router=DefaultRouter()
router.register('blood-bank-donor',BloodBankDonorViewSet,basename='blood-bank-donor')
router.register('donor',DonorViewSet,basename='donor')

urlpatterns = [
    path('',include(router.urls)),
    
]