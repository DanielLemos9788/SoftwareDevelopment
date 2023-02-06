from django.http import HttpResponse
from datetime import datetime
import json

def current_time_greet(request):
    now = datetime.now().strftime("%d %b %Y - %H:%M hours")
    return HttpResponse(f"The current time is {now}".format(now=str(now)))

def greetings(request):
    return HttpResponse("Nemesis Server is Online")

def welcome(request):
    return HttpResponse("Your Grace, It is a Pleasure to Have You Today")

def retrieve_numbers(request):
    numbers = request.GET['numbers']
    data = {
        'status': 'OK',
        'numbers': numbers,
        'message': 'Integers Sorted Successfully'
    }
    return HttpResponse(json.dumps(data, indent=2), content_type='application/json')

def greet_info_added(request, name, age):

    if age < 12:
        message = 'Sorry {}, Nemesis will NOT serve you, ' \
                  'Because of your age, you are NOT ALLOWED HERE'.format(name)

    elif age >= 12:
        message = '{} of Noble Grace, Nemesis is Here to Serve You'.format(name)

    return HttpResponse(message)



