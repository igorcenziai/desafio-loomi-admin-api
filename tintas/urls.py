from django.urls import path
from .views import TintaListCreateView, TintaDetailView

urlpatterns = [
    path('', TintaListCreateView.as_view(), name='tinta-list-create'),
    path('<int:pk>/', TintaDetailView.as_view(), name='tinta-detail'),
]
