from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.view_home, name='view_home'),
    path('', views.login_view, name='login'),
    path('', views.log_out, name='log_out'),
    path('pythonbasic/', views.view_pythonbasic, name='view_pythonbasic'),
    path('pythonintermediate/', views.view_pythonintermediate, name='view_pythonintermediate'),
    path('sqldatabases/', views.view_sql, name='view_sql'),
    path('frontend/', views.view_frontend, name='view_frontend'),
    path('backend/', views.view_backend, name='view_backend'),
    path('view_schedule/', views.view_schedule, name='view_schedule'),
    path('add_student/', views.create_view, name='create_view'),
    path('update_student/<id>', views.update_view, name='update_view'),
    path('delete_student/<id>', views.delete_view, name='delete_view'),
    path('view_student/<id>', views.info_view, name='info_view'),
    path('add_grades/', views.add_grades, name='add_grades'),
    path('delete_row/<id>', views.delete_row, name='delete_row'),

]