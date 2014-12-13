from django.shortcuts import render

# Create your views here.

def home(request):
    if request.user.is_authenticated():
        username_is = "Marius"
        context =  {"username_is": request.user}
    else:
        context = {"username_is": request.user}

    gigi = 'Marius'
    template = 'home.html'

    return render(request, template, context)