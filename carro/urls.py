from django.urls import path
from .views import insert, list_carro, delete_task, update_from, update

urlpatterns = [
    path('', list_carro),  
    path("insert/", insert, name='insert'),
    path('update', update, name='update'),
    path('update/<int:task_id>/', update_from, name='update_from'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),     
]
