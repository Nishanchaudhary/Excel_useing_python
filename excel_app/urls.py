from django.urls import path
from .views import excel_data_view

urlpatterns = [
    path('', excel_data_view, name='excel_data'),
]