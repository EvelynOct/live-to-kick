from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406365282',
        'name': 'Evelyne Octaviana Benedicta Aritonang',
        'class': 'KKI'
    }

    return render(request, "main.html", context)