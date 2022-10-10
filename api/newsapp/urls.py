from django.urls import path, include
from .views import ShowThreeNewsView, ShowAllNewsView

urlpatterns = [
    path('show2_3/<slug:pos>/', ShowThreeNewsView.as_view()),
    path('all/<slug:pos>/', ShowAllNewsView.as_view()),
]
