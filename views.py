from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import ItemSerializer, TrackSerializer
from .models import Member, Period
from rest_framework import serializers

class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all().order_by("mid")
    serializer_class = ItemSerializer


