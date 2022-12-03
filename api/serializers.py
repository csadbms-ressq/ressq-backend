from .models import (BloodBankDonor,Donor)
from rest_framework import serializers

class BloodBankDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodBankDonor
        fields='__all__'

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields='__all__'
        