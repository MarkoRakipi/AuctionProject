from django.shortcuts import render


def homepage(request):
    template_name = 'homepage.html'
    return render(request, template_name)
