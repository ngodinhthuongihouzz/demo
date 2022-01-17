from . import views
from django.urls import path


app_name = 'price_estimate'

urlpatterns = [
    path('', views.PriceEstimateView.as_view(), name='price_estimate'),
]
