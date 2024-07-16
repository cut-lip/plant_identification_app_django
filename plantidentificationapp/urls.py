from django.urls import path
from .views import API1View, API2View

# Define API URL patterns
urlpatterns = [
    path('api/1/', API1View.as_view(), name='API1'),
    path('api/2/', API2View.as_view(), name='API2')
]
