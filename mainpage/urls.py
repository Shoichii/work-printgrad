from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    # path('calculator/',views.calculator,name='calculator'),
    path('form_data/', views.form_data, name='form_data'),
    path('form_was_send/', views.form_was_send, name='form_was_send')
]