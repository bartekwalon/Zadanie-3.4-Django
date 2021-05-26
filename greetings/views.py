from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request, name="World!"):
    return HttpResponse(f"Hello {name}")


def about(request):
    return render(
        request=request,
        template_name="greetings/about.html",
        context={}
    )


def contact(request):
    return render(
        request=request,
        template_name="greetings/contact.html",
        context={}
    )


def welcome(request):
    return render(
        request=request,
        template_name="greetings/welcome.html",
        context={}
    )
