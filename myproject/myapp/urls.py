from django.urls import path
from . import  views

urlpatterns=[path('add/', views.addastudent, name='add'),
              path("view/", views.viewdata, name="view"),
              path("update/<int:id>",views.update_student,name="updatename"),
              path("delete/<int:id>",views.deletemethod,name="delete"),
              path("python_student/",views.python_student,name="python_student"),
              path('high_marks/', views.high_marks, name='high_marks'),
              path('total/', views.total_students, name='total_students'),]