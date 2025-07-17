from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import UserProfile


class CustomRegisterSeriaLizer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data("first_name", "")
        data['last_name'] = self.validated_data("last_name", "")
        data['phone_number'] = self.validated_data("phone_number", "")
        return data
    
    def save(self, request):
        user = super().save(request)
        user.save()
        
        UserProfile.objects.update_or_create(
            user=user,
            defaults={
                'first_name': self.validated_data.get("first_name"),
                'last_name': self.validated_data.get("last_name"),
                'phone_number': self.validated_data.get("phone_number")
            }
        )
        
        return user
    