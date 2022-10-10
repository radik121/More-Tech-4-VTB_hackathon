from rest_framework import serializers
from .models import News, Insites, Trends


class InsitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insites
        fields = '__all__'


class TrendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trends
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    insites = InsitesSerializer(read_only=True)
    trends = TrendsSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('title', 'description', 'url', 'date', 'tags', 'insites', 'trends')

