import requests
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Activity
from .serializers import UserSerializer, ActivitySerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# 🌦️ Third-party API integration
@api_view(['GET'])
def weather_api(request):
    city = request.GET.get('city', 'Mumbai')
    api_key = 'YOUR_OPENWEATHER_API_KEY'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return Response(response.json())
