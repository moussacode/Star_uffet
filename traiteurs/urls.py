
from django.urls import path
from . import views


urlpatterns = [
    
    
    path('', views.traiteurs, name="traiteur" ),
    path('<uuid:pk>/', views.detail_traiteurs, name="detail_traiteurs" ),
    path('devenir_traiteur/', views.inscription_traiteur, name="devenir_traiteur" ),

]