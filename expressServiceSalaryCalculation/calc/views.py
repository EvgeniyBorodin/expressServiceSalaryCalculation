from django.shortcuts import render
from calc.models import Employee, Position, PaymentStatement, PaymentReport


def index(request):
    employees = Employee.objects.filter()
    context = {'employees': employees}
    return render(request, 'calc/index.html', context)


