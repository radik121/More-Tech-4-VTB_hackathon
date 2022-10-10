from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NewsSerializer
from .models import News
from .utils import get_ids


class ShowFreshNewsView(APIView):
    pass


class ShowAllFreshNewsView(APIView):
    pass


class ShowThreeNewsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pos):
        filter_news = News.objects.filter(positions__slug=pos).select_related()
        ids = get_ids(filter_news)
        news = filter_news.filter(id__in=ids)
        serializer = NewsSerializer(instance=news, many=True)
        return Response(serializer.data)


class ShowAllNewsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pos):
        news = News.objects.filter(positions__slug=pos).select_related()
        serializer = NewsSerializer(instance=news, many=True)
        return Response(serializer.data)
