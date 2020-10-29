from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('add', views.add, name='add'),
    path('delete/<int:dogovor_id>', views.delete_dogovor, name='delete_dogovor'),
    path('<int:dogovor_id>/', views.detail, name='detail'),
    path('<int:dogovor_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('<int:dogovor_id>/new_kt/', views.new_kt, name='new_kt'),


    path('<int:dogovor_id>/pretenzia/', views.pretenzia, name='pretenzia'),


]
