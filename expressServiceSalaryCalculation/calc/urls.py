from django.conf.urls import url

from . import views

app_name = 'student_progress'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^payment_statements/$', views.payment_statements, name='payment_statements'),
    # url(r'^payment_statement/(?P<statement_code_code>[0-9]+)/$', views.payment_statement, name='payment_statement'),
    # url(r'^payment_reports/$', views.payment_reports, name='payment_reports'),
    # url(r'^payment_report/(?P<report_code_code>[0-9]+)/$', views.payment_report, name='payment_report'),
]