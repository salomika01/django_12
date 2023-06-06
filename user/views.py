from django.http import HttpResponse
import datetime


def user_view(request):
    user = User.objects.first()
    birth_date = user.birth_date
    current_date = datetime.date.today()
    age = current_date.year - birth_date.year
    return HttpResponse(f"Name: {user.first_name} {user.last_name}, Age: {age}")
