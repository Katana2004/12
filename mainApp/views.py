from django.shortcuts import render


def contacts(request):
    return render(request, 'mainApp/contacts.html')


def about(request):
    return render(request, 'mainApp/about-us.html')
