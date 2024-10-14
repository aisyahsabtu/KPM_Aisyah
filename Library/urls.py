from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='index'),
    path('view/', views.view, name='view'),
    path('book/', views.book, name='book'),
    path('student/', views.student, name='student'),
    path('borrow/', views.borrow, name='borrow'),
    path('course/', views.course, name = 'course'),
    path('mentor/', views.mentor, name = 'mentor'),
    path('course/update_course/<str:code>', views.update_course, name = 'update_course'),
    path('course/update_course/save_update_course/<str:code>', views.save_update_course, name = 'save_update_course'),
    path('course/delete_course/<str:code>', views.delete_course,name='delete_course'),
    path('search_course/', views.search_course, name='search_course')
]