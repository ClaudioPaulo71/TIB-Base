from django.urls import path
from . import views

urlpatterns = [
    # Ex: /review/1/ -> Abre o painel do registro 1
    path('review/<int:record_id>/', views.review_dashboard, name='review_dashboard'),
]