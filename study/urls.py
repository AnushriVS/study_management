from django.urls import path
from.import views

urlpatterns=[
    path('',views.index, name='index'),
    path('<int:id>',views.view_study, name='view_study'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
]