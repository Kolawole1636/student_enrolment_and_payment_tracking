
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('courses', views.courses, name="courses"),
    path('updatecourse/<int:id>', views.update_course, name='updatecourse'),
    path('student', views.student, name="student"),
    path('updatestudent/<int:id>', views.update_student, name='updatestudent'),
    path('students', views.students, name="students"),
    path('payment', views.payment, name="payment"),
    path('payments', views.payments, name="payments"),
    path('ptrack', views.payment_track, name="ptrack"),
    path('searchpayment', views.search_payment, name="searchpayment"),


]
