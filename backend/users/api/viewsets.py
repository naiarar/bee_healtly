from rest_framework import viewsets
from users.api import serializers
from users import models

class UsersViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializer
    queryset = models.User.objects.all()