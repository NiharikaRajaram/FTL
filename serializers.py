from rest_framework import serializers
import six
from .models import Member
from .models import Period

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['start', 'end']

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    tz = serializers.SerializerMethodField()
    activity_periods = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Member
        fields = ('mid', 'real_name', 'tz', 'activity_periods')

    def get_tz(self, obj):
        return six.text_type(obj.tz)