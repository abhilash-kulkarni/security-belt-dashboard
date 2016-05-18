from django.conf.urls import url

from pi_app import views

urlpatterns = [
    url(r'^employee/$', views.employee, name='employee'),
    url(r'^employeedetails/id=(?P<q>\w+)/$', views.employeedetails, name='employeedetails'),
]
