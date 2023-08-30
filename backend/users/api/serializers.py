from rest_framework import serializers
from users import models

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'