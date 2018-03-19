from django.db import models
import datetime


class Position(models.Model):
    name = models.CharField(max_length=100)
    salary = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Employee(models.Model):
    personnel_number = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    experience = models.FloatField(default=0.0)
    work_start_date = models.DateField()
    position = models.ForeignKey(Position, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class PaymentStatement(models.Model):
    payment_summ = models.FloatField(default=0.0)
    ndfl_tax = models.FloatField(default=0.0)
    fss_contribution = models.FloatField(default=0.0)
    ops_contribution = models.FloatField(default=0.0)
    foms_contribution = models.FloatField(default=0.0)
    date = models.DateTimeField(default = datetime.datetime.now())

    def __str__(self):
        return 'Платёжная ведомость от ' + self.date


class PaymentReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    days = models.FloatField(default=0.0)
    payment_summ = models.FloatField(default=0.0)
    ndfl_tax = models.FloatField(default=0.0)
    fss_contribution = models.FloatField(default=0.0)
    ops_contribution = models.FloatField(default=0.0)
    foms_contribution = models.FloatField(default=0.0)
    premium = models.FloatField(default=0.0)
    payment_statement = models.ForeignKey(PaymentStatement, on_delete=models.CASCADE)

    def __str__(self):
        return 'Расчетный лист - ' + self.employee.name
