from django.urls import path
from myapp.views import LandingView

app_name = 'myapp'
urlpatterns = [
    path('', LandingView.as_view()),
]
