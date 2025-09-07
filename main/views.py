from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406400524',
        'name': 'Samuel Indriano',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)