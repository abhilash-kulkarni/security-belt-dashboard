from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from models import *

def employee(request):
	if request.method == 'POST':
		post = request.POST
		if post['query'] == 'employeeid':
			return redirect('employeedetails', post['employeeid'])
	else:
		return render(request, 'employee.html')

def employeedetails(request, q):
	if request.method == 'POST':
		pass
	else:
		try:
			employee = Employee.objects.get(employeeId = q)
			employeeLevelAbove = Employee.objects.filter(level__gt = employee.level).order_by('level')
			levelAbove = employee.level + 1
			return render(request, 'employeedetails.html', {'employee': employee, 'employeeLevelAbove': employeeLevelAbove, 'levelAbove': levelAbove})
		except ObjectDoesNotExist:
			return HttpResponse('Employee not found.')
