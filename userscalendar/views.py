from django.http import HttpResponse
import datetime


def date_view(request):
    current_date = datetime.date.today()
    return HttpResponse(current_date)
