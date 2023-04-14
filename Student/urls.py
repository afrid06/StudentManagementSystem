from django.urls import path

from Student import views

urlpatterns = [
    path('', views.home),
    path('displaystudent', views.displaystudent, name='displaystudent'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('readstudent', views.readstudent),
    path('update/<int:id>', views.update_fun,name='update'),
    path('delete/<int:id>', views.delete_fun, name='delete')
]
