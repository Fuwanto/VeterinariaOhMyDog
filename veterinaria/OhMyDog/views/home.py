from django.shortcuts import render


def home(request):
    return render(request, "home.html", {"is_staff": request.user.is_staff})
