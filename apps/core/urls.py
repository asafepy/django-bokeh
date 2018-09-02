from django.conf.urls import url
from apps.core import views

urlpatterns = [
    url('dashboard/', views.show_dashboard),
    url('data/', views.data, name="data"),
]
