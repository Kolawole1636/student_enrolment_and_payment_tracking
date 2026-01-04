
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('courses', views.courses, name="courses"),
    path('student', views.student, name="student"),
    path('students', views.students, name="students"),
    path('payment', views.payment, name="payment"),
    path('payments', views.payments, name="payments"),
    path('ptrack', views.payment_track, name="ptrack"),
    path('searchpayment', views.search_payment, name="searchpayment"),


]
