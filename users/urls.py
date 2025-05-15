from django.urls import path
from .views import home,index, profile, RegisterView,logout_view
from . import views

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('logout_view/',logout_view,name='logout_view'),
    path('index/', index, name='users-index'),
    path('Basic_report/',views.Basic_report,name='Basic_report'),
    path('Metrics_report/',views.Metrics_report,name='Metrics_report'),
    path('chatbot/', views.chatbot_response_view,name='chatbot'),
    path('model/',views.model,name='model'),
    
    path('model_db',views.model_db,name='model_db'),
    
    
    
    
    
    ]


 