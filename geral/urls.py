from django.urls import path
from geral import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('analise/<int:pacientes>', views.analise, name='analise'),
    path('diagnostico/<int:pacientes>', views.diagnostico, name='diagnostico'),
    path('laudo/<int:pacientes>', views.laudo, name='laudo'),
]