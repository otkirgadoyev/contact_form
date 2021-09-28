from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


def index(request):
    if request.method == "POST":
        message = request.POST['message']
        send_mail('Contact Form',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['otkirgadoyev24@gmail.com'],
                  fail_silently=False)
    return render(request, 'index.html')
